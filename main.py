import json
import sqlite3

con = sqlite3.connect('pokedex.db')
con.execute("CREATE TABLE pokedex (id int, name nvarchar, primaryType nvarchar, secondaryType nvarchar, description nvarchar);")

with open('poke.json', 'r') as poke:
    data = json.load(poke)
    for item in data:
        con.execute("INSERT INTO pokedex(id, name, primaryType, secondaryType, description) VALUES(?, ?, ?, ?, ?)", (item["id"], item["name"], item["primaryType"], item["secondaryType"], item["description"]))
con.commit()
con.close()
