import random
COLOR_WHITE = "blanc"
COLOR_BLACK = "noir"


class Matchs:
    list_of_matchs = []

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.info_match = {}
        self.color_of_player = {}
        self.score_player_1 = []
        self.score_player_2 = []
        Matchs.list_of_matchs.append(self)
        
    def score_update(self, score_player_1, score_player_2):
        """
        Met à jour les scores des joueurs pour ce match.

        Args:
            score_player_1 (int): Score du joueur 1.
            score_player_2 (int): Score du joueur 2.

        Returns:
            dict: Dictionnaire contenant les informations du match.
        """
        self.info_match = {
            self.player_1: score_player_1,
            self.player_2: score_player_2
        }
        return self.info_match
    # def score_update(self):
    #     print(f"{self.player_1} VS {self.player_2}")
    #     score_player_1 = int(input(f"Entrer le score {self.player_1} : "))
    #     self.score_player_1.append(score_player_1)
    #     self.score_player_1.insert(0, self.player_1)
    #     score_player_2 = int(input(f"Entrer le score {self.player_2} : "))
    #     self.score_player_2.append(score_player_2)
    #     self.score_player_2.insert(0, self.player_2)
    #     self.info_match = (self.score_player_1, self.score_player_2)
    #     return self.info_match

    def assign_random_colors(self):
        """
        Attribue aléatoirement des couleurs aux joueurs.

        Returns:
            dict: Dictionnaire associant chaque joueur à une couleur.
        """
        players = [self.player_1, self.player_2]
        random.shuffle(players)
        self.color_of_player = {
            players[0]: COLOR_WHITE,
            players[1]: COLOR_BLACK
        }
        return self.color_of_player

    def __repr__(self):
        return f"{self.player_1} VS {self.player_2}"

# match = Matchs("jérémie", "pierre")

# match = match.score_update()
# print(match)
