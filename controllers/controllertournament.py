import random
from random import shuffle
from models.players import Players
from models.tournament import Tournaments
from models.tours import Tours
from models.matchs import Matchs
from view.utils import Utils

COLOR_WHITE = "blanc"
COLOR_BLACK = "noir"


class ConstantTournament:

    START_A_TOUR = "1"
    END_A_TOUR = "2"
    LOAD_PREVIOUS_TOUR = "3"
    RETURN_TOURNAMENT_MANAGEMENT_MENU = "x"


class ControllerTournament:

    def __init__(self, view, tournament):
        self.view = view
        self.tournament = tournament
        self.players = Players.load()
        self.tours = []
        self.tour = None
        self.matchs = []
        self.match = None
        self.previous_matches = set()

    def run(self):
        while True:
            action = self.view.tournament_menu()
            match action:

                case ConstantTournament.START_A_TOUR:
                    self.start_tour()
                case ConstantTournament.END_A_TOUR:
                    # self.end_tour()
                    pass
                case ConstantTournament.LOAD_PREVIOUS_TOUR:
                    self.load_previous_pairs()

                case ConstantTournament.RETURN_TOURNAMENT_MANAGEMENT_MENU:
                    break

                case _:
                    print("Choix inconnue.")
                    input("Appuyer sur entrée pour continuer...")

    def update_score(self, match, player_1, player_2):
        """ """
        player_1, player_2 = Players.load_by_ids(player_1, player_2)
        score_player_1, score_player_2 = self.view.requests_score(player_1, player_2)
        match.score_update(score_player_1, score_player_2)
        for joueur, score in ((player_1, score_player_1), (player_2, score_player_2)):
            self.tournament.update_player_score(joueur, score)

    def generate_pairs(self, tour, players):
        """
        Génère des paires de joueurs pour le tour et crée les matchs.
        """
        tour.matchs = []
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                player_1 = players[i]
                player_2 = players[i + 1]
                pair_ids = tuple(sorted([player_1.id, player_2.id]))
                if pair_ids in self.previous_matches:
                    input("pair detected : ")
                    swapped = False
                    for p in range(i + 2, len(players)):
                        player_2_alt = players[p]
                        pair_ids_alt = tuple(sorted([player_1.id, player_2_alt.id]))
                        if pair_ids_alt not in self.previous_matches:
                            players[i + 1], players[p] = players[p], players[i + 1]
                            player_2 = players[i + 1]
                            swapped = True
                            break
                pair_ids = tuple(sorted([player_1.id, player_2.id]))
                self.previous_matches.add(pair_ids)
                match = Matchs(player_1.id, player_2.id)
                color_of_player = ControllerTournament.assign_random_colors(
                    player_1, player_2
                )
                self.view.display_color_player(color_of_player)
                tour.matchs.append(match)
        self.matchs = tour.matchs

    def start_tour(self):
        """_summary_"""
        # Vérifier s'il reste des tours à jouer
        if self.tournament.current_tour == self.tournament.number_of_turns:
            self.view.display_string("Tournoi terminé.")
            return

        # --- Début du tour ---
        self.tournament.start()
        self.tournament.add_1_to_current_tour()

        # Définir l'ordre des joueurs
        if self.tournament.current_tour == 1:
            players = self.tournament.list_player.copy()
            shuffle(players)
        else:
            players = self.sorted_by_score()
            players = Players.load_by_ids(*players)

        # Création du tour et génération des paires
        tour = Tours(self.tournament.current_tour)
        self.view.display_string(f"Début du {tour.name}")
        self.generate_pairs(tour, players)
        self.tournament.list_of_tours.append(tour)
        tour.start()
        self.tournament.update(self.tournament.id)
        self.tour = tour

        # --- Fin du tour ---
        self.tour.end()

        # Mise à jour des scores pour chaque match
        for match in self.matchs:
            self.update_score(match, match.player_1, match.player_2)
        if self.tournament.current_tour == self.tournament.number_of_turns:
            self.view.display_string("Fin du tournoi")
            self.tournament.end()
        self.tournament.update(self.tournament.id)

    def sorted_by_score(self):
        player_score_item = self.tournament.player_scores.items()
        player_score_item_sorted = sorted(player_score_item, key=lambda x: x[1])
        player_sorted = [player[0] for player in player_score_item_sorted]
        return player_sorted

    def load_previous_pairs(self):
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
                self.view.display_string(f"Les précédentes paire de match\n{tour.name} terminé")
            else:
                self.view.display_string("Les précédentes paires de matchs on déjas été chargé.")
        else:
            self.view.display_string("Veuillez commencer un tournoi.")


    @staticmethod
    def assign_random_colors(player_1, player_2):
        """
        Attribue aléatoirement des couleurs aux joueurs.

        Returns:
            dict: Dictionnaire associant chaque joueur à une couleur.
        """
        if random.choice([True, False]):
            color_of_player = {player_1: COLOR_WHITE, player_2: COLOR_BLACK}
        else:
            color_of_player = {player_1: COLOR_BLACK, player_2: COLOR_WHITE}
        return color_of_player
