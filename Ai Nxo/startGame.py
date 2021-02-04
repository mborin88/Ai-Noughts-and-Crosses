#
# Starting game
#
playerWinValue = 1
comPlayerValue = 2
draw = 0


def StartGame(theGrid):
    for i in range(9):
        theGrid[i] = ''

    return theGrid


def GetWinningPositions():
    AIWinningData = []
    winningTurns = []
    NoFile = False
    try:
        AIFile = open('NxOData.txt', 'r')
        Line = AIFile.readlines()
        for RawNoteOldGame in Line:
            if (RawNoteOldGame != '') or (RawNoteOldGame != '\n'):
                storedGameH = RawNoteOldGame[:len(RawNoteOldGame) - 1]  # Gets rid of the /n from raw note
                hyphenFind = storedGameH.find('-')
                if storedGameH[len(storedGameH) - 1] == str(comPlayerValue):
                    AIWinningData.append(storedGameH[:hyphenFind])
                elif storedGameH[len(storedGameH) - 1] == str(playerWinValue):
                    AIWinningData.append(storedGameH[hyphenFind + 1:len(storedGameH) - 2])
    except IOError:
        print('No data file found...')
        print('File will be created at end of game\n')
        NoFile = True

    return NoFile, AIWinningData
