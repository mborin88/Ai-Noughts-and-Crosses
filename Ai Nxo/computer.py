#
# Computers brain
#
"""
Issue with forks not being able to be blocked only can see winning moves tries to emulate doesn't know how
to emulate a blocking commands e.g. if player goes on edge have to play centre. To stop corner forks
Possible solution: randomise computer starting or player starting, which will have to change the code to say who started.
this could then see the player block the computers attempted fork. Then need to analyse the losing half of the data and
see what it could do different. Need algorithm to take into consideration winning position and desire to get there and
 block player but also the factor that made it lose, to avoid doing that again.
"""
import random
import sys


def countGrid(GridToCount, positionsToCheck, check):    # counts grid for x's or o's in a particular set of positions
    count = 0
    for i in range(len(positionsToCheck)):
        if GridToCount[int(positionsToCheck[i])] == check:
            count += 1

    return count


def imperative(playerCom, theGrid3, potentials):    # Finds which moves need to be blocked utmost importance
    imperativeMoves = []
    if playerCom:
        NxO = 'x'
    elif playerCom == 2:
        NxO = 'o'

    for i in range(len(potentials)):
        numOfTakenPlaces = countGrid(theGrid3, potentials[i], NxO)
        position = -1
        if numOfTakenPlaces+1 == len(potentials[i]):
            for j in range(len(potentials[i])):
                if theGrid3[int(potentials[i][j])] == '':
                    position = j

            if position > 0:
                imperativeMoves.append(potentials[i][position])

    return imperativeMoves


def awardWeight(theGrid2, popPossibleMovesDict, losingPositions, superMove, blockAdvance):
    weight = 5
    imperativeWeight = (len(losingPositions) * 5 * weight) + blockAdvance   # weight to say we must move here
    if len(superMove) > 0:
        for n in range(len(superMove)):
            popPossibleMovesDict.update(
                {str(superMove[n]): popPossibleMovesDict.get(str(superMove[n])) + imperativeWeight})
    else:
        for i in range(len(losingPositions)):
            for j in range(len(losingPositions[i])):
                if theGrid2[int(losingPositions[i][j])] == '':
                    popPossibleMovesDict.update(
                        {losingPositions[i][j]: popPossibleMovesDict.get(losingPositions[i][j]) + weight})
    return popPossibleMovesDict


def BlockPlayer(theGrid2, winningPositions):
    block = []
    for i in range(len(winningPositions)):
        potentialDanger = False
        for j in range(len(winningPositions[i])):
            if (theGrid2[int(winningPositions[i][j])] == 'x') and (potentialDanger == False):
                potentialDanger = True
                block.append(i)
            elif (theGrid2[int(winningPositions[i][j])] == 'o') and (potentialDanger == True):
                if i in block:
                    block.remove(i)  # Wont block forks

                # Need to double position for if its the last piece required

    AILose = [0] * len(block)
    for i in range(len(block)):
        AILose[i] = winningPositions[block[i]]

    special = imperative(1, theGrid2, AILose)
    return AILose, special


def AdvanceCom(theGrid2, theData2):

    win = []
    for i in range(len(theData2)):
        valid = True
        potentialWin = False
        for j in range(len(theData2[i])):
            if (theGrid2[int(theData2[i][j])] == 'o') and (potentialWin == False) and (valid == True):
                potentialWin = True
                win.append(i)
            elif theGrid2[int(theData2[i][j])] == 'x':
                if i in win:
                    win.remove(i)
                valid = False

    AIWin = [0] * len(win)
    for i in range(len(win)):
        AIWin[i] = theData2[win[i]]

    special = imperative(2, theGrid2, AIWin)
    return AIWin, special


def AnalyseWinningPositions(theGrid2, winningPositions):
    potentialMovesDict = {'0': 0,
                          '1': 0,
                          '2': 0,
                          '3': 0,
                          '4': 0,
                          '5': 0,
                          '6': 0,
                          '7': 0,
                          '8': 0}

    for i in range(len(winningPositions)):
        for j in range(len(winningPositions[i])):
            numAvailable = winningPositions[i][j]
            if theGrid2[int(numAvailable)] == '':
                potentialMovesDict.update({numAvailable: potentialMovesDict.get(numAvailable) + 1})

    return potentialMovesDict


def SplitChoice(theSplitPositions):
    if len(theSplitPositions) == 1:
        choice = 0
    else:
        choice = random.randint(0, len(theSplitPositions) - 1)    # random.randint breaks with 0 range e.g. (0,0)
    chosenPosition = theSplitPositions[choice]

    return chosenPosition


def ChooseCOMPos(popPossibleMovDict):
    highest = 0
    keys = []

    for i in range(9):
        x = popPossibleMovDict.get(str(i))
        if x > highest:
            highest = x

    listOfKeys = popPossibleMovDict.items()
    for item in listOfKeys:
        if item[1] == highest:
            keys.append(item[0])

    position = SplitChoice(keys)

    return position


def validData(myGrid, myData, blockAdvance):    # Gets rid of data that has already been blocked by player or COM
    validDataList = []
    if blockAdvance == "block":
        testCase = 'o'
    elif blockAdvance == "advance":
        testCase = 'x'
    else:
        print("Error in sifting data expected 'block' or 'advance' received: ", blockAdvance)
        sys.exit()

    for i in range(len(myData)):
        closedSpaces = countGrid(myGrid, myData[i], testCase)
        if closedSpaces == 0:
            validDataList.append(myData[i])

    return validDataList


def COMMove2(COMMoveH, NoFile, theGrid, theData):
    if not NoFile:
        validMovesDict = AnalyseWinningPositions(theGrid, theData)
        blockDataMoves = validData(theGrid, theData, "block")
        AILoss, specialBlock = BlockPlayer(theGrid, blockDataMoves)
        validMovesDict = awardWeight(theGrid, validMovesDict, AILoss, specialBlock, 0)

        advanceDataMoves = validData(theGrid, theData, "advance")
        AIWin, specialWin = AdvanceCom(theGrid, advanceDataMoves)
        if COMMoveH != '':
            validMovesDict = awardWeight(theGrid, validMovesDict, AIWin, specialWin, 1)

        position = int(ChooseCOMPos(validMovesDict))
    else:
        position = random.randint(0, 8)
        while theGrid[position] != '':
            position = random.randint(0, 8)

    if theGrid[position] == '':
        theGrid[position] = 'o'
        COMMoveH = COMMoveH + str(position)
    else:
        COMMove2(COMMoveH, NoFile, theGrid, theData)

    return COMMoveH
