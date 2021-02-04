#
# Functions for endOfGame
#
import sys

playerWinValue = 1
comPlayerValue = 2
draw = 0

PlayAgain = True
winner = draw


def HasGameEnded(theGrid, IsGameOver):
    gridFull = True
    global winner
    for i in range(9):
        if theGrid[i] == '':
            gridFull = False

    winner = draw

    if (theGrid[0] == 'x') and (theGrid[1] == 'x') and (theGrid[2] == 'x'):
        winner = playerWinValue
        IsGameOver = True
    elif (theGrid[0] == 'x') and (theGrid[3] == 'x') and (theGrid[6] == 'x'):
        winner = playerWinValue
        IsGameOver = True
    elif (theGrid[0] == 'x') and (theGrid[4] == 'x') and (theGrid[8] == 'x'):
        winner = playerWinValue
        IsGameOver = True
    elif (theGrid[1] == 'x') and (theGrid[4] == 'x') and (theGrid[7] == 'x'):
        winner = playerWinValue
        IsGameOver = True
    elif (theGrid[2] == 'x') and (theGrid[5] == 'x') and (theGrid[8] == 'x'):
        winner = playerWinValue
        IsGameOver = True
    elif (theGrid[2] == 'x') and (theGrid[4] == 'x') and (theGrid[6] == 'x'):
        winner = playerWinValue
        IsGameOver = True
    elif (theGrid[3] == 'x') and (theGrid[4] == 'x') and (theGrid[5] == 'x'):
        winner = playerWinValue
        IsGameOver = True
    elif (theGrid[6] == 'x') and (theGrid[7] == 'x') and (theGrid[8] == 'x'):
        winner = playerWinValue
        IsGameOver = True

    elif (theGrid[0] == 'o') and (theGrid[1] == 'o') and (theGrid[2] == 'o'):
        winner = comPlayerValue
        IsGameOver = True
    elif (theGrid[0] == 'o') and (theGrid[3] == 'o') and (theGrid[6] == 'o'):
        winner = comPlayerValue
        IsGameOver = True
    elif (theGrid[0] == 'o') and (theGrid[4] == 'o') and (theGrid[8] == 'o'):
        winner = comPlayerValue
        IsGameOver = True
    elif (theGrid[1] == 'o') and (theGrid[4] == 'o') and (theGrid[7] == 'o'):
        winner = comPlayerValue
        IsGameOver = True
    elif (theGrid[2] == 'o') and (theGrid[5] == 'o') and (theGrid[8] == 'o'):
        winner = comPlayerValue
        IsGameOver = True
    elif (theGrid[2] == 'o') and (theGrid[4] == 'o') and (theGrid[6] == 'o'):
        winner = comPlayerValue
        IsGameOver = True
    elif (theGrid[3] == 'o') and (theGrid[4] == 'o') and (theGrid[5] == 'o'):
        winner = comPlayerValue
        IsGameOver = True
    elif (theGrid[6] == 'o') and (theGrid[7] == 'o') and (theGrid[8] == 'o'):
        winner = comPlayerValue
        IsGameOver = True

    if gridFull:
        IsGameOver = True

    return IsGameOver


def GameOverMessage():
    print('------------------------------------------------------------------------------')
    if winner == 2:
        print('\t\t\tYou Lost :(')
    elif winner == 1:
        print('\t\tYou win!!!!')
    elif winner == 0:
        print("\t\t\t It's a draw...")
    print('------------------------------------------------------------------------------')


def DuplicateData(appendData):
    DataFile = open('NxOData.txt', 'r')
    Data = DataFile.readlines()
    Duplicate = False
    appendData = appendData + "\n"

    for RawData in Data:
        if appendData == RawData:
            Duplicate = True
            return Duplicate

    return Duplicate


def StoreDetails(GameEnded, HistoryOfMoves, NoFile):  # Don't store duplicates of the same game shouldn't happen once complete but check.
    if GameEnded:
        data = ''
        duplicate = False
        # for i in range(len(MoveHistory)):
        #    data = data + str(MoveHistory[i])

        data = HistoryOfMoves + '-' + str(winner)
        if not NoFile:
            duplicate = DuplicateData(data)
        if not duplicate:
            DataFile = open('NxOData.txt', 'a')
            DataFile.write(data + '\n')
            DataFile.close()


def newGame():
    newGameAnswer = input('Do you want to play again?\t')

    if (newGameAnswer == 'y') or (newGameAnswer == 'Y'):
        return True
    else:
        return False
        print('Thanks for playing with me till next time!!')
        sys.exit()
