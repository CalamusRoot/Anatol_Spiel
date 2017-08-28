class Player():
    def __init__(self, name):
        self.name = name
        self.location_x = 0
        self.dmg = 10
        self.location_y = 0
        self.iventar = ["gold:15","fäuste"]
        self.hp = 150
        self.gewonnen = False
        
    def am_leben(self):
        return self.hp > 0
    
    def zeige_inventar(self):
        for item in self.iventar:
            print(item, '\n')
    
    def get_name(self):
        return self.name
    
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
    