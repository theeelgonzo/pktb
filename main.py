import json
import sqlite3
from datetime import datetime
import varStore as vs
import pdfunc as pf
import game as g

# initialize pokedex

""" con = sqlite3.connect('pokedex.db')
con.execute("CREATE TABLE pokedex (id int, name nvarchar, primaryType nvarchar, secondaryType nvarchar, description nvarchar);")

with open('poke.json', 'r') as poke:
    data = json.load(poke)
    for item in data:
        con.execute("INSERT INTO pokedex(id, name, primaryType, secondaryType, description) VALUES(?, ?, ?, ?, ?)", (item["id"], item["name"], item["primaryType"], item["secondaryType"], item["description"]))
con.commit()
con.close() """


# main loop
while True:

    # get time
    now = datetime.now()
    currHour = int(now.strftime("%H"))

    # check for time of day
    if currHour < 12:
        dayTime = 'morning'
    elif currHour >= 12 and currHour < 17:
        dayTime = 'afternoon'
    else:
        dayTime = 'evening'

    # greet trainer

    print(vs.border)
    print(f'Good {dayTime}, Trainer. It is hour {currHour} of the day.')
    tName = input('What is your name? \n')
    print(f'How may I be of assistance, {tName}?')
    print(vs.border)
    choice = input(
        f'1. View My Pokedex\n2. Start A New Game\nor\n3. Nothing For Now, Thanks!\n{vs.border}\n')

    # either access pokedex or break loop/exit program
    if choice == '1':
        pChoice = input(
            f'Great choice, {tName}! Do you\n1. Want to See A Specific Pokemon\nor\n2. Want To See A List Of Pokemon?\n{vs.border}')
        if pChoice == '1':
            dChoice = input(
                f'Would you like to\n1. Search By ID\nor\n2. Search By Name?\n{vs.border}\n')
            if dChoice == '1':
                pf.findByID()
                continue
            elif dChoice == '2':
                pf.findByName()
                continue
            else:
                vs.doof()
        elif pChoice == '2':
            lChoice = input(
                'Do you want to\n1. Search by elemental type\nor\n2. Search in order?')
            if lChoice == '1':
                pf.listByType()
            elif lChoice == '2':
                # initialize variables to be used in sql query
                xId = 1
                yId = 10
                while yId < 151:
                    pf.listInOrder(xId, yId)

                    # allows user to continue browsing, incrementing the id vars and returning the next ten results from db

                    keepGoing = input(
                        'Would you like to\n1. View More Pokemon?\nor\n2. Go Back?\n')
                    if keepGoing == '1':
                        xId += 10
                        yId += 10
                        pf.listInOrder(xId, yId)
                    elif keepGoing == '2':
                        break
                    else:
                        vs.doof()

            else:
                vs.doof()
        else:
            vs.doof()
            continue
    elif choice == '2':
        print('Sure! We will start a new game!')
        g.newGame()

    elif choice == '3':
        print(
            f'Very well, {tName}! Have a marvelous {dayTime}!\n{vs.border}\n')
        break
    else:
        vs.doof()
        continue
