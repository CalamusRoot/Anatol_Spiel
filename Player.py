from Character import Character


class Player(Character):
    def __init__(self, name):
        self.won = False
        self.hp = 100
        self.xp = 0
        self.dmg = 1
        self.defense = 5
        self.location_x = 0
        self.location_y = 0
        super().__init__(name, self.hp, self.xp, self.dmg, self.defense, self.location_x, self.location_y)
        
        def get_name(self):
            return self.name
        
        def am_leben(self):
            return self.hp > 0

        def zeige_inventar(self):
            for item in self.iventar:
                print(item, '\n')

        def bewege(self, dx, dy):
            self.location_x += dx
            self.location_y += dy

        def bewege_norden(self):
            self.bewege(dx=0, dy=-1)

        def bewege_süden(self):
            self.bewege(dx=0, dy=1)

        def bewege_osten(self):
            self.bewege(dx=1, dy=0)

        def bewege_westen(self):
            self.bewege(dx=-1, dy=0)
        
        
hans = Player("hans")

print(hans.name)
print(hans.dmg)
 
        

