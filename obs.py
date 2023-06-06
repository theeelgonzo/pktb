
# define monster class

class Monster:
    def __init__(self, name, primType, subType, hp, level, movesRoster, hmComp, tmComp):
        self.name = name
        self.primType = primType
        self.subType = None
        self.hp = 10
        self.level = 1
        self.movesRoster = []
        self.hmComp = []
        self.tmComp = []

# define trainer class

class Trainer:
    def __init__(self, name):
        self.name = name
