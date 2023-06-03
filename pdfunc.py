import sqlite3
import varStore as vs


def findByID():

    con = sqlite3.connect('pokedex.db')
    cur = con.cursor()
    pkid = input('Which ID would you like to search for?\n')
    res = cur.execute("SELECT * FROM pokedex WHERE id = ?", (pkid,))
    print(res.fetchall())


def findByName():
    con = sqlite3.connect('pokedex.db')
    cur = con.cursor()
    pkName = input('Which name would you like to search for?\n')
    pkName = pkName.lower()
    print(f'{pkName}')
    res = cur.execute("SELECT * FROM pokedex WHERE LOWER(name) = ?", (pkName,))
    print(res.fetchall())


def listByType():
    # capture user element search option and store in variable
    elType = input("What element would you like to see?\n1. Grass?\n2. Water?\n3. Fire?\n4. Poison\n5. Bug?\n6. Normal?\n7. Fighting?\n8. Flying?\n9. Ground?\n10. Electric?\n11. Psychic?\n12. Rock?\n13. Ghost?\n14. Ice?\n 15.Dragon?")
    if elType == '1':
        typeChoice = 'Grass'
    elif elType == '2':
        typeChoice = 'Water'
    elif elType == '3':
        typeChoice = 'Fire'
    elif elType == '4':
        typeChoice = 'Poison'
    elif elType == '5':
        typeChoice = 'Bug'
    elif elType == '6':
        typeChoice = 'Normal'
    elif elType == '7':
        typeChoice = 'Fighting'
    elif elType == '8':
        typeChoice = 'Flying'
    elif elType == '9':
        typeChoice = 'Ground'
    elif elType == '10':
        typeChoice = 'Electric'
    elif elType == '11':
        typeChoice = 'Psychic'
    elif elType == '12':
        typeChoice = 'Rock'
    elif elType == '13':
        typeChoice = 'Ghost'
    elif elType == '14':
        typeChoice = 'Ice'
    elif elType == '15':
        typeChoice = 'Dragon'
    else:
        vs.doof()

    # use choice variable as binding in db search, filter by element primary and sub type
    con = sqlite3.connect('pokedex.db')
    cur = con.cursor()
    res = cur.execute(
        "SELECT * FROM pokedex WHERE primaryType = ? OR secondaryType = ?", (typeChoice, typeChoice))
    print(res.fetchall())


def listInOrder():
    pass
