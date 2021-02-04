#
# Computers brain
#
import random


def AwardBlockWeight(theGrid2, popPossibleMovesDict, losingPositions):
    blockingWeight = 5
    for i in range(len(losingPositions)):
        for j in range(len(losingPositions[i])):
            if theGrid2[int(losingPositions[i][j])] == '':
                popPossibleMovesDict.update({losingPositions[i][j]: popPossibleMovesDict.get(losingPositions[i][j]) + blockingWeight})
    return popPossibleMovesDict


def AwardAdvanceWeight(popPossibleMovesDict, AIWin):
    advancingWeight = 5
    for i in range(len(AIWin)):
        for j in range(len(AIWin[i])):
            popPossibleMovesDict.update({AIWin[i][j]: popPossibleMovesDict.get(AIWin[i][j]) + advancingWeight})

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

    return AILose


def AdvanceCom(theGrid2, theData2):
    """win = []
    for i in range(len(AIDataW)):
        potentialWin = 0
        for j in range(len(AIDataW[i])):
            if Grid[j] == 'o':
                potentialWin += 1
            elif Grid[j] == '':
                popPossibleMovesDict.update({AIDataW[i][j]: popPossibleMovesDict.get(AIDataW[i][j]) + 1})"""

    win = []
    for i in range(len(theData2)):
        valid = True
        winWeight = 0
        potentialWin = False
        for j in range(len(theData2[i])):
            if (theGrid2[int(theData2[i][j])] == 'o') and (potentialWin == False) and (valid == True):
                potentialWin = True
                winWeight += 1
                win.append(i)
            elif theGrid2[int(theData2[i][j])] == 'x':
                if i in win:
                    win.remove(i)
                valid = False

    AIWin = [0] * len(win)
    for i in range(len(win)):
        AIWin[i] = theData2[win[i]]

    return AIWin


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

    return potentialMovesDict, winningPositions


def SplitChoice(theSplitPositions):
    choice = random.randint(0, len(theSplitPositions) - 1)
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


def COMMove2(COMMoveH, NoFile, theGrid, theData):

    if not NoFile:
        validMovesDict, theData = AnalyseWinningPositions(theGrid, theData)
        AILoss = BlockPlayer(theGrid, theData)
        validMovesDict = AwardBlockWeight(theGrid, validMovesDict, AILoss)
        AIWin = AdvanceCom(theGrid, theData)
        if COMMoveH != '':
            validMovesDict = AwardAdvanceWeight(validMovesDict, AIWin)

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
