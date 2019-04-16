#
#Modelis

class Player(object):
    def __init__(self, name, lastname, points, height):
        self.name = name
        self.lastname = lastname
        self.points = points
        self.height = height
        print('beda')

    def cm_to_meters (self):
        return str(self.height/100)+"m"


class BasketballPlayer(Player):
    def __init__(self, rebounds, turnovers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rebounds = rebounds
        self.turnovers = turnovers

class FootballPlayer(Player):
    def __init__(self, assist, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assist = assist


#Objektas
lebronius = BasketballPlayer(15, 40, 'Lebron', 'James', height=220, points=2000)
messi = FootballPlayer(assist=165, height=150, lastname='Messi', points=650, name='Leo')

print(lebronius.name)
print(messi.name)
