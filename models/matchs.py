from models.players import Players


class Matchs:
    """
    Class representing a match between two players.

    Holds the result for each player and provides methods to update scores
    and convert match data to/from dictionary format.
    """

    def __init__(self, player_1, player_2):
        """
        Initialize a match with two players.

        Parameters:
            player_1: The ID to the first player.
            player_2: The ID to the second player.
        """
        # Initialize match results as a list of two entries: [player, score]
        self.result = ([player_1, 0.0], [player_2, 0.0])
        self.player_1 = player_1
        self.player_2 = player_2

    def score_update(self, score_player_1, score_player_2):
        """
        Update the scores for both players in the match.

        Parameters:
            score_player_1 (float): Score for player 1.
            score_player_2 (float): Score for player 2.
        """
        self.result[0][1] = score_player_1
        self.result[1][1] = score_player_2

    def to_dict(self):
        """
        Convert the match result to a dictionary format.

        Returns:
            The match result as a dictionary.
        """
        return self.result

    @classmethod
    def from_dict(cls, data):
        """
        Recreate a Matchs object from a dictionary.

        Parameters:
            data (dict): Dictionary containing match data.

        Returns:
            Matchs: A new Matchs instance with data populated.
        """
        player_1 = data["result"][0][0]
        player_2 = data["result"][1][0]
        match = cls(player_1, player_2)
        match.result = data["result"]
        return match

    def __repr__(self):
        """
        Return a string representation of the match.

        Returns:
            str: A string showing the two players in the match.
        """
        # Loads player objects to display their names
        player1_obj = Players.load_by_ids(self.player_1)[0]
        player2_obj = Players.load_by_ids(self.player_2)[0]
        return f"Match: {player1_obj} vs {player2_obj}"
