
# define monster class

class Monster:
    def __init__(self, name, primType, subType, hp, level, movesRoster, hmComp, tmComp):
        self.name = name
        self.primType = primType
        self.subType = None
        self.hp = 10
        self.level = 1
        self.movesRoster = []
        # the following arrays define which moves a monster can learn
        self.hmComp = []
        self.tmComp = []

# define trainer class


class Trainer:
    def __init__(self, name, pkRoster):
        self.name = name
        self.pkRoster = []
