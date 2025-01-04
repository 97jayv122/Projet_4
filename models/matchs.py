    
import random

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
        return self.info_match 

    def random_color(self):
        group_player = random.shuffle([self.player_1, self.player_2])
        self.color_of_player = [(group_player[0], self.color_1),
                           (group_player[1], self.color_2)]
        return self.color_of_player
# match = Matchs("jérémie", "pierre")
# match = match.score_update()
# print(match)
