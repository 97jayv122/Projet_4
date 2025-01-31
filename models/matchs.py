import random
COLOR_WHITE = "blanc"
COLOR_BLACK = "noir"


class Matchs:
    list_of_matchs = []

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.info_match = ()
        self.color_of_player = {}
        self.score_player_1 = 0
        self.score_player_2 = 0
        Matchs.list_of_matchs.append(self)
        
    def score_update(self, score_player_1, score_player_2):
        """
        Met à jour les scores des joueurs pour ce match.

        Args:
            score_player_1 (int): Score du joueur 1.
            score_player_2 (int): Score du joueur 2.

        Returns:
            tuple: deux listes contenant lchacune le joueur et son score.
        """
        self.info_match = (
            [self.player_1, score_player_1],
            [self.player_2, score_player_2]
        )
        return self.info_match

    def assign_random_colors(self):
        """
        Attribue aléatoirement des couleurs aux joueurs.

        Returns:
            dict: Dictionnaire associant chaque joueur à une couleur.
        """
        if random.choice([True, False]):
            self.color_of_player = {self.player_1: COLOR_WHITE, self.player_2: COLOR_BLACK}
        else:
            self.color_of_player = {self.player_1: COLOR_BLACK, self.player_2: COLOR_WHITE}

    def to_dict(self):
        return {
            "info_match": self.info_match,
            "color_of_player": self.color_of_player
        }
    @classmethod
    def from_dict(cls, data):
        """
        Recrée un objet Matchs à partir d'un dictionnaire.
        """
        player_1, score_1 = data["info_match"][0]
        player_2, score_2 = data["info_match"][1]
        match = cls(player_1, player_2)
        match.info_match = data["info_match"]
        match.color_of_player = data["color_of_player"]
        return match

    def __repr__(self):
        return f"Match: {self.player_1} vs {self.player_2} - Scores: {self.info_match}"

# match = Matchs("jérémie", "pierre")
# match.assign_random_colors()
# match.score_update(0, 0)
# # print(match.color_of_player)
# # print(match.info_match)
# # print(match)
# data = (match.to_dict())
# print(data)
# match1 = Matchs.from_dict(data)
# print(match1.to_dict())