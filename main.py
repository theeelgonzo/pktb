import json
import sqlite3
from datetime import datetime
import varStore as vs

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
        f'1. View My Pokedex \n2. Nothing For Now, Thanks!\n{vs.border}\n')

    # either access pokedex or break loop/exit program
    if choice == '1':
        pChoice = input(
            f'Great choice, {tName}! Do you\n1. Want to See A Specific Pokemon\nor\n2. Want To See A List Of Pokemon?\n{vs.border}')
        if pChoice == '1':
            pass
        elif pChoice == '2':
            pass
        else:
            vs.doof()
            continue
    elif choice == '2':
        print(
            f'Very well, {tName}! Have a marvelous {dayTime}!\n{vs.border}\n')
        break
    else:
        vs.doof()
        continue
