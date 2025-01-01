import calendar
import json
import random
import time
import uuid 

FOLDER = "data/tournaments"

class Tournament:
    def __init__(self, name, place, date_start, date_end,
                 number_of_turns=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.number_of_turns = number_of_turns
        self.list_player = []
        self.list_of_tours = []
        self.current_tour = 0
        self.description = ""

    

class Players:
    list_of_player = []
    def __init__(self, first_name, name, date_of_birth,
                 national_chess_identifier):
        self.first_name = first_name
        self.name = name
        self.date_of_birth = date_of_birth
        self.national_chess_identifier = national_chess_identifier
        self.id = str(uuid.uuid4())
        Players.list_of_player.append(self)


    def __repr__(self):
        return str(self.first_name) + "." + str(self.name)
    
    def to_dict(self):
        return {"first_name":self.first_name,
                "name": self.name,
                "date_of_birth": self.date_of_birth,
                "national_chess_identifier": self.national_chess_identifier,
                "id": self.id}
    
    def save_player(self):
        with open(FOLDER + "/players.json", "w") as file:
            json.dump([player.to_dict() for player in self.list_of_player], file)

    def load_data_player(self,):
        with open(FOLDER + "/players.json", "r") as file:
            data = json.load(file)
            self.list_of_player = []
            
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data.get("first_name"),
            name=data.get("name"),
            date_of_birth=data.get("date_of_birth"),
            national_chess_identifier=data.get("national_chess_identifier")
        )
    
class Matchs:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.info_match = ()
        self.score_1 = []
        self.score_2 = []
        self.color_1 = "blanc"
        self.color_2 = "noir"
        self.color_of_player = []

    def score_update(self):
        score_player_1 = int(input(f"Entrer le score {self.player_1} : "))
        self.score_1.append(score_player_1)
        self.score_1.insert(0, self.player_1)
        score_player_2 = int(input(f"Entrer le score {self.player_2} : "))
        self.score_2.append(score_player_2)
        self.score_2.insert(0, self.player_2)
        self.info_match = (self.score_1, self.score_2)
        print(self.info_match)
        return self.info_match 

    def random_color(self):
        group_player = random.shuffle([self.player_1, self.player_2])
        self.color_of_player = [(group_player[0], self.color_1),
                           (group_player[1], self.color_2)]
        return self.color_of_player
# match = Matchs("jérémie", "pierre")
# match = match.score_update()
# print(match)

class Tours:
    def __init__(self, list_player_of_tournament):
        self.list_player_of_tournament = list_player_of_tournament
        self.time_start = time()
        self.time_end = time()
        self.group_by_two = []
        self.match_list_by_round = []

    

    def make_first_tour(self):
        random.shuffle(self.list_player_of_tournament)
        self.group_by_two = [[self.list_player_of_tournament[i], 
                              self.list_player_of_tournament[i + 1]]
                              for i in range(0, len(self.list_player_of_tournament) - 1, 2)]
        if len(self.list_player_of_tournament) % 2 == 0 :
            self.group_by_two.append([self.list_player_of_tournament[-1], "Sans adversaire"])
        return self.group_by_two
    def add_a_round(self):
        pass