import random
from random import shuffle
from models.players import Players
from models.tours import Tours
from models.matchs import Matchs

COLOR_WHITE = "blanc"
COLOR_BLACK = "noir"


class ConstantTournament:
    """
    Constants representing tournament menu options.
    """
    START_A_TOUR = "1"
    LOAD_PREVIOUS_TOUR = "2"
    RETURN_TOURNAMENT_MANAGEMENT_MENU = "x"


class ControllerTournament:
    """
    Controller for managing tournament rounds.

    Handles the creation of rounds, pairing players, updating scores,
    and loading previous match pairings.
    """
    def __init__(self, view, tournament):
        """
        Initialize the tournament controller.

        Parameters:
            view: The view instance for user interactions.
            tournament: The tournament object being managed.
        """
        self.view = view
        self.tournament = tournament
        self.players = Players.load()
        self.tours = []
        self.tour = None
        self.matchs = []
        self.match = None
        self.previous_matches = set()

    def run(self):
        """
        Run the tournament management loop.

        Processes user actions for starting rounds, loading previous pairings,
        or returning to the management menu.
        """
        while True:
            action = self.view.tournament_menu()
            match action:

                case ConstantTournament.START_A_TOUR:
                    self.start_tour()

                case ConstantTournament.LOAD_PREVIOUS_TOUR:
                    self.load_previous_pairs()

                case ConstantTournament.RETURN_TOURNAMENT_MANAGEMENT_MENU:
                    break

                case _:
                    self.view.display_unknow_choice_message()

    def update_score(self, match, player_1, player_2):
        """
        Update the score for a match based on user input.

        Parameters:
            match: The match object to update.
            player_1: ID of the first player.
            player_2: ID of the second player.
        """
        # Reload player objects by their IDs
        player_1, player_2 = Players.load_by_ids(player_1, player_2)
        # Request scores from the view
        score_player_1, score_player_2 = self.view.requests_score(player_1, player_2)
        # Update the match with the provided scores
        match.score_update(score_player_1, score_player_2)
        # Update the tournament's score records for each player
        for joueur, score in ((player_1, score_player_1), (player_2, score_player_2)):
            self.tournament.update_player_score(joueur, score)

    def generate_pairs(self, tour, players):
        """
        Generate player pairs for the round and create the matches.

        Parameters:
            tour: The current round (Tours object).
            players: The list of players to be paired.
        """
        tour.matchs = []
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                player_1 = players[i]
                player_2 = players[i + 1]
                pair_ids = tuple(sorted([player_1.id, player_2.id]))
                # If this pair has already played, try to find an alternative pairing
                if pair_ids in self.previous_matches:
                    for p in range(i + 2, len(players)):
                        player_2_alt = players[p]
                        pair_ids_alt = tuple(sorted([player_1.id, player_2_alt.id]))
                        if pair_ids_alt not in self.previous_matches:
                            # Swap the players to get a new pairing
                            players[i + 1], players[p] = players[p], players[i + 1]
                            player_2 = players[i + 1]
                            break
                pair_ids = tuple(sorted([player_1.id, player_2.id]))
                self.previous_matches.add(pair_ids)
                match = Matchs(player_1.id, player_2.id)
                # Assign random colors to the players for this match
                color_of_player = ControllerTournament.assign_random_colors(
                    player_1, player_2
                )
                self.view.display_color_player(color_of_player)
                tour.matchs.append(match)
        self.matchs = tour.matchs

    def start_tour(self):
        """
        Start a new round (tour) in the tournament.

        Checks if any rounds remain, shuffles or sorts players, generates pairs,
        updates scores, and ends the round.
        """
        # Check if all rounds have been played
        if self.tournament.current_tour == self.tournament.number_of_turns:
            self.view.display_end_tournament_message()
            return

        # --- Start of the round ---
        self.tournament.start()
        self.tournament.add_1_to_current_tour()

        # Determine the order of players
        if self.tournament.current_tour == 1:
            players = self.tournament.list_player.copy()
            shuffle(players)
        else:
            players = self.sorted_by_score()
            players = Players.load_by_ids(*players)

        # Create the round and generate player pairs
        tour = Tours(self.tournament.current_tour)
        self.view.display_start_round_message(tour.name)
        self.generate_pairs(tour, players)
        self.tournament.list_of_tours.append(tour)
        tour.start()
        self.tournament.update(self.tournament.id)
        self.tour = tour

        # --- End of the round ---
        self.tour.end()

        # Update scores for each match in the round
        for match in self.matchs:
            self.update_score(match, match.player_1, match.player_2)
        if self.tournament.current_tour == self.tournament.number_of_turns:
            self.view.display_end_tournament_message()
            self.tournament.end()
        self.tournament.update(self.tournament.id)

    def sorted_by_score(self):
        """
        Sort players based on their scores.

        Returns:
            list: List of player IDs sorted by score.
        """
        player_score_item = self.tournament.player_scores.items()
        # Sort by score
        player_score_item_sorted = sorted(player_score_item, key=lambda x: x[1])
        player_sorted = [player[0] for player in player_score_item_sorted]
        return player_sorted

    def load_previous_pairs(self):
        """
        Load and display previous match pairings if available.
        """
        if self.tournament.current_tour > 0:
            if not self.previous_matches:
                previous_list_matchs = [
                    match
                    for tour in self.tournament.list_of_tours
                    for match in tour.matchs
                ]
                flat_previous_list_matchs = [
                    player for matchs in previous_list_matchs for player in matchs
                ]
                previous_pair = [
                    tuple(
                        sorted(
                            [
                                flat_previous_list_matchs[i][0],
                                flat_previous_list_matchs[1 + i][0],
                            ]
                        )
                    )
                    for i in range(0, len(flat_previous_list_matchs), 2)
                ]
                self.previous_matches = set()
                [self.previous_matches.add(item) for item in previous_pair]
                tour = self.tournament.list_of_tours[-1]
                self.tour = tour
                self.view.display_matchs_pairs_properly_loaded_message(tour.name)
            else:
                self.view.display_matchs_pairs_already_load_message()
        else:
            self.view.display_request_start_tournament_message()

    @staticmethod
    def assign_random_colors(player_1, player_2):
        """
        Randomly assign colors to the players.

        Parameters:
            player_1: The first player.
            player_2: The second player.

        Returns:
            dict: A dictionary mapping each player to a color.
        """
        if random.choice([True, False]):
            color_of_player = {player_1: COLOR_WHITE, player_2: COLOR_BLACK}
        else:
            color_of_player = {player_1: COLOR_BLACK, player_2: COLOR_WHITE}
        return color_of_player
