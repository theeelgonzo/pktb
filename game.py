# start game
# called from main

import varStore as vs

def startGame():
    print('Would you like to play a game?')
    newGame = input('Would you like to\n1.Start A New Game?')
    if newGame == '1':
        newGame()
    else:
        vs.doof()

def newGame():
