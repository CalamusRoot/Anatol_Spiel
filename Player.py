from Character import Character


class Player(Character):
    def __init__(self, name, hp, xp, dmg, defense, x, y):
        self.won = False
        super().__init__(name, hp, xp, dmg, defense, x, y)
        
        
hans = Player()

print(hans.name)
 
        

    # def am_leben(self):
    #     return self.hp > 0
    #
    # def zeige_inventar(self):
    #     for item in self.iventar:
    #         print(item, '\n')
    #
    # def get_name(self):
    #     return self.name
    #
    # def bewege(self, dx, dy):
    #     self.location_x += dx
    #     self.location_y += dy
    #
    # def bewege_norden(self):
    #     self.bewege(dx=0, dy=-1)
    #
    # def bewege_süden(self):
    #     self.bewege(dx=0, dy=1)
    #
    # def bewege_osten(self):
    #     self.bewege(dx=1, dy=0)
    #
    # def bewege_westen(self):
    #     self.bewege(dx=-1, dy=0)