import random
from models.players import Players
COLOR_WHITE = "blanc"
COLOR_BLACK = "noir"


class Matchs:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result = ()
        self.color_of_player = {}
        self.score_player_1 = 0.0
        self.score_player_2 = 0.0

    def score_update(self, score_player_1, score_player_2):
        """
        Met à jour les scores des joueurs pour ce match.

        Args:
            score_player_1 (int): Score du joueur 1.
            score_player_2 (int): Score du joueur 2.

        Returns:
            tuple: deux listes contenant chacune le joueur et son score.
        """
        self.result = (
            [self.player_1, score_player_1],
            [self.player_2, score_player_2]
        )
        return self.result

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
        # print(self)
        return {
            "result": self.result,
            "color_of_player": self.color_of_player
        }
    @classmethod
    def from_dict(cls, data):
        """
        Recrée un objet Matchs à partir d'un dictionnaire.
        """
        player_1, score_1 = data["result"][0]
        player_2, score_2 = data["result"][1]
        match = cls(player_1, player_2)
        match.result = data["result"]
        match.color_of_player = data["color_of_player"]
        return match

    def __repr__(self):
        return f"Match: {Players.load_by_ids(self.player_1)[0]} vs {Players.load_by_ids(self.player_2)[0]}"
