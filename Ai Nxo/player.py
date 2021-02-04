#
# Players moves
#


def move(PlayerMoveH, theGrid):
    x = int(input('Where would you like to put your cross??'))
    if (0 <= x <= 8) and (theGrid[x] == ''):
        theGrid[x] = 'x'
        # MoveHistory.append(x)
        PlayerMoveH = PlayerMoveH + str(x)
    else:
        PlayerMoveH = move(PlayerMoveH, theGrid)

    return PlayerMoveH
