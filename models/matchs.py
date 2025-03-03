from models.players import Players


class Matchs:

    def __init__(self, player_1, player_2):
        self.result = ([player_1, 0.0], [player_2, 0.0])
        self.player_1 = player_1
        self.player_2 = player_2

    def score_update(self, score_player_1, score_player_2):
        """
        Met à jour les scores des joueurs pour ce match.

        Args:
            score_player_1 (int): Score du joueur 1.
            score_player_2 (int): Score du joueur 2.

        Returns:
            tuple: deux listes contenant chacune le joueur et son score.
        """
        self.result[0][1] = score_player_1
        self.result[1][1] = score_player_2
        

    # def assign_random_colors(player_1, player_2):
    #     """
    #     Attribue aléatoirement des couleurs aux joueurs.

    #     Returns:
    #         dict: Dictionnaire associant chaque joueur à une couleur.
    #     """
    #     if random.choice([True, False]):
    #         color_of_player = {player_1: COLOR_WHITE, player_2: COLOR_BLACK}
    #     else:
    #         color_of_player = {player_1: COLOR_BLACK, player_2: COLOR_WHITE}

    def to_dict(self):
        # print(self)
        return self.result
            

        
    @classmethod
    def from_dict(cls, data):
        """
        Recrée un objet Matchs à partir d'un dictionnaire.
        """
        player_1 = data["result"][0][0]
        player_2 = data["result"][1][0]
        match = cls(player_1, player_2)
        match.result = data["result"]
        return match

    def __repr__(self):
        return f"Match: {Players.load_by_ids(self.player_1)[0]} vs {Players.load_by_ids(self.player_2)[0]}"


# match1 = Matchs("eva", "bob")
# print(match1.result)
# match1.score_update(1, 0)
# print(match1.to_dict())
# match2 = Matchs.from_dict(match1.to_dict())