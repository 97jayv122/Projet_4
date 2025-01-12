import random
COLOR_1 = "blanc"
COLOR_2 = "noir"


class Matchs:
    list_of_matchs = []

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.info_match = ()
        self.score_1 = []
        self.score_2 = []
        self.color_of_player = []
        Matchs.list_of_matchs.append(self)

    def score_update(self):
        print(f"{self.player_1} VS {self.player_2}")
        score_player_1 = int(input(f"Entrer le score {self.player_1} : "))
        self.score_1.append(score_player_1)
        self.score_1.insert(0, self.player_1)
        score_player_2 = int(input(f"Entrer le score {self.player_2} : "))
        self.score_2.append(score_player_2)
        self.score_2.insert(0, self.player_2)
        self.info_match = (self.score_1, self.score_2)
        return self.info_match

    def random_color(self):
        group_player = [self.player_1, self.player_2]
        random.shuffle(group_player)
        self.color_of_player = [
            (group_player[0], COLOR_1), (group_player[1], COLOR_2)
            ]
        return self.color_of_player

    def __repr__(self):
        return f"{self.player_1} VS {self.player_2}"

# match = Matchs("jérémie", "pierre")

# match = match.score_update()
# print(match)
