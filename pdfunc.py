import sqlite3


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
