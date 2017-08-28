from abc import ABCMeta, abstractmethod


class Character():
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.name = "a"
        # self.hp = None
        # self.xp = None
        # self.dmg = None
        # self.defense = None
        # self.location_x = None
        # self.location_y = None

hans = Character()

print(hans.name)