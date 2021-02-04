#
# AI Noughts and Crosses
#
#
# To make an imperative block higher weighted if its the last one
# If it cant see a winning position that it has started see if there is an new winning formula that is still available
# also do one away from winning is an imperative move

import startGame
import endGame
import display
import player
import computer

Grid = ['', '', '', '', '', '', '', '', '']

MoveHistory = ''
PlayerHistory = ''
COMHistory = ''
# Data is of the winning positions

while endGame.PlayAgain:
    currentPath = ''
    COMHistory = ''
    PlayerHistory = ''
    GameOver = False
    Grid = startGame.StartGame(Grid)
    EmptyFile, Data = startGame.GetWinningPositions()
    display.ShowGrid(Grid)
    while not GameOver:
        PlayerHistory = player.move(PlayerHistory, Grid)
        GameOver = endGame.HasGameEnded(Grid, GameOver)
        print(GameOver)
        if not GameOver:
            COMHistory = computer.COMMove2(COMHistory, EmptyFile, Grid, Data)
        GameOver = endGame.HasGameEnded(Grid, GameOver)
        display.ShowGrid(Grid)

    MoveHistory = COMHistory + '-' + PlayerHistory
    endGame.GameOverMessage()
    endGame.StoreDetails(GameOver, MoveHistory, EmptyFile)

    endGame.PlayAgain = endGame.newGame()
