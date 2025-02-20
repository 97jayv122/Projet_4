from random import shuffle
from models.players import Players
from models.tournament import Tournaments
from models.tours import Tours
from models.matchs import Matchs
from view.utils import Utils


class ConstantTournament:

    START_A_TOUR = "1"
    NEXT_TOUR = "2"
    END_A_TOUR = "3"
    RETURN_TOURNAMENT_MANAGEMENT_MENU = "x"

class ControllerTournament:

    def __init__(self, view, tournament, tournaments):
        self.view = view
        self.tournament = tournament
        self.tournaments = tournaments
        self.players = Players.load()
        self.tours = []
        self.tour = None
        self.matchs = []
        self.match =  None
        self.previous_matches = set()

    def run(self):
        while True:
            action = self.view.tournament_menu()
            match action:

                case ConstantTournament.START_A_TOUR:
                    self.start_tour()
                case ConstantTournament.NEXT_TOUR:
                    self.next_tour()
                case ConstantTournament.END_A_TOUR:
                    self.end_tour()

                case ConstantTournament.RETURN_TOURNAMENT_MANAGEMENT_MENU:
                    break

                case _:
                    print("Choix inconnue.")
                    input("Appuyer sur entrée pour continuer...")

    def update_score(self, match, player_1, player_2):
        """ """
        player_1, player_2 = Players.load_by_ids(player_1, player_2)
        score_player_1, score_player_2 = self.view.requests_score(
            player_1, player_2
            )
        match.score_update(score_player_1, score_player_2)

    def generate_pairs(self, tour, players):
        """
        Génère des paires de joueurs pour le tour et crée les matchs.
        """ 
        pairs = []
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
                print(pair_ids)
                self.previous_matches.add(pair_ids)
                match = Matchs(player_1.id, player_2.id)
                match.assign_random_colors()
                match.score_update(0, 0)
                self.view.display_string(match.color_of_player)
                tour.matchs.append(match)
        self.matchs = tour.matchs


    def start_tour(self):
        # try:
        self.view.display_string(self.tournament)
        self.tournament.add_1_to_current_tour()
        if self.tournament.current_tour == 1:
            players = self.tournament.list_player.copy()
            shuffle(players)  # Mélange aléatoire des joueurs
        else:
            players = self.sorted_by_score()
            print(players)
            players = Players.load_by_ids(*players)
            print(players)
            input()
        tour = Tours(self.tournament.current_tour)
        self.generate_pairs(tour, players)
        self.tournament.list_of_tours.append(tour)
        # self.tournament.update(self.tournament.name, tournament_dict)
        Tournaments.save_all(self.tournaments)
            # self.tour.start()
        # except UnboundLocalError:
        #     self.view.display_string("Pas de tournois créé")
        # except AttributeError:
        #     self.view.display_string("pas de tournoi créé")

    def end_tour(self):
        """  """
        try:
            # self.tour.end()
            print(self.matchs)
            input()
            [self.update_score(match, match.player_1, match.player_2)
                for match in self.matchs]
            input()
        except UnboundLocalError:
            print("Pas de matchs commencé")
        Tournaments.save_all(self.tournaments)
        # tournament.add_tour(tour)

    def sorted_by_score(self):
        player_score = []
        for match in self.matchs:
            player_score.append(match.result)
        player_score = [player for match in player_score for player in match]
        player_score_sorted = sorted(player_score, key=lambda x: x[1])
        print(player_score_sorted)
        player_sorted = [player[0] for player in player_score_sorted]
        print(player_sorted)
        input()
        return player_sorted