# #
# #Modelis
# us_cities_list = ["Boston", "New York", "Los Angeles", "San Francisco"]
# emails_dict = {"john.smith@yahoo.com": "John Smith", "janedoe@gmail.com": "Jane Doe", "fluffy-pony@hotmail.com": "Riccardo Spagni"}
# class Player(object):
#     def __init__(self, name, lastname, points, height):
#         self.name = name
#         self.lastname = lastname
#         self.points = points
#         self.height = height
#         print('beda')
#
#     def cm_to_meters (self):
#         return str(self.height/100)+"m"
#
#
# class BasketballPlayer(Player):
#     def __init__(self, rebounds, turnovers, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.rebounds = rebounds
#         self.turnovers = turnovers
#
# class FootballPlayer(Player):
#     def __init__(self, assist, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.assist = assist
#
#
# #Objektas
# lebronius = BasketballPlayer(15, 40, 'Lebron', 'James', height=220, points=2000)
# messi = FootballPlayer(assist=165, height=150, lastname='Messi', points=650, name='Leo')
#
# print(lebronius.name)
# print(messi.name)
# ============================================================================================
# class BasketballPlayer():
#     def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.height_cm = height_cm
#         self.weight_kg = weight_kg
#         self.points = points
#         self.rebounds = rebounds
#         self.assists = assists
#     # Metodas
#     def weight_to_lbs(self):
#         pounds = self.weight_kg * 2.20462262
#         return pounds
#
#
# lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)
# kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)
#
# # list of players
# bball_players = [lebron, kev_dur]
#
# for player in bball_players:
#     print(player.last_name + ", " + player.first_name)
#
# lebron_dict = {"first_name": "Lebron", "last_name": "James", "height_cm": 203, "weight_kg": 113, "points": 27.2, "rebounds": 7.4, "assists": 7.2}
#
# print(lebron_dict["first_name"])
# print(lebron_dict["height_cm"])
# print(lebron.weight_to_lbs())

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

print(kev_dur.last_name)
print(kev_dur.rebounds)
print(kev_dur.weight_to_lbs())

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

print(messi.first_name)
print(messi.goals)
print(messi.weight_to_lbs())