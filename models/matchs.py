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

    def to_dict(self):
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
