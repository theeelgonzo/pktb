
# define monster class

class Monster:
    def __init__(self, name, primType, subType, hp, level):
        self.name = name
        self.primType = primType
        self.subType = None
        self.hp = 10
        self.level = 1

# define trainer class

class Trainer:
    def __init__(self, name):
        self.name = name
