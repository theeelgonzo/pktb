# start game
# called from main

import varStore as vs
import obs as o

def startGame():
    print('Would you like to play a game?')
    newGame = input('Would you like to\n1.Start A New Game?')
    if newGame == '1':
        newGame()
    else:
        vs.doof()

def newGame():
    pcName = input('What would you like to name your character?\n')
    startMon = input('What element type would you like your first Pokemon to be?\n1. Fire?\n2. Water?\n3. Grass?\n')
    if startMon == '1':
        startPK = 'Charmander'
    elif startMon == '2':
        startPK = 'Squirtle'
    elif startMon == '3':
        startPK =='Bulbasaur'
    else:
        vs.doof()

    pc = new o.Trainer(pcName, startPK)
    pc.introduce()
