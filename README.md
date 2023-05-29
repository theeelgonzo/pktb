# pktb

A text-based Pokemon game in Python

To be developed as a Pokedex first with the original Generation I pokemon. Users
will have the ability to search the pokedex.

The game will develop from there.

## Design

Here proceeds a rough draft of the building process.

### Database/Pokedex

We will develop the pokedex from a JSON file. JSON is being utilized at first instead of hard coding a database, so users can incorporate their own creatures for endless customization. Upon initialization of the program, the code will check to see if pokedex.db is present, and if not it will parse the JSON file data and create pokedex.db. SQLite will be used initially for portability and Python's standard library integration.

Once the database is initialized, the main program loop will begin. Phase One involves strictly viewing the data as a pokedex. The program main function will give users options to view Pokemon from the entire list, or to select them specifically by ID, or by "genres" such as element. There will also be an option to exit the pokedex, which effectively terminates the program.
