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
        self.tours = None
        self.tour = None
        self.matchs = None
        self.match =  None

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
        score_player_1, score_player_2 = self.view.requests_score(
            player_1, player_2
            )
        match.score_update(score_player_1, score_player_2)

    def generate_first_matchs(self, tour):
        """
        Génère des paires de joueurs pour le tour et crée les matchs.
        """
        shuffle(self.tournament.list_player)  # Mélange aléatoire des joueurs
        tour.matchs_list_by_round = []
        for i in range(0, len(self.tournament.list_player), 2):
            if i + 1 < len(self.tournament.list_player):
                player_1 = self.tournament.list_player[i]
                player_2 = self.tournament.list_player[i + 1]
                self.match = Matchs(player_1, player_2)
                self.match.assign_random_colors()
                self.match.score_update(0, 0)
                self.view.display_string(self.match.color_of_player)
                self.matchs.append(self.match)

    def start_tour(self):
        try:
            self.view.display_string(self.tournament)
            print(self.tournament.current_tour)
            input()
            self.tournament.add_1_to_current_tour()
            self.tour = Tours(self.tournament.current_tour)
            self.generate_first_matchs(self.tour)
            self.tournament.list_of_tours.append(self.tour.__dict__)
            tournament_dict = self.tournament.__dict__
            # self.tournament.update(self.tournament.name, tournament_dict)
            Tournaments.clear_json_tournament
            [tournament.save() for tournament in self.tournaments]
            print(tournament_dict)
            # self.tour.start()
        except UnboundLocalError:
            self.view.display_string("Pas de tournois créé")
        except AttributeError:
            self.view.display_string("pas de tournoi créé")

    def end_tour(self):
        """  """
        try:
            # self.tour.end()
            [self.update_score(match, match.player_1, match.player_2)
                for match in self.matchs]
        except UnboundLocalError:
            print("Pas de matchs commencé")
        Tournaments.clear_json_tournament
        [tournament.save() for tournament in self.tournaments]

        # tour.recovery_list_of_matchs(Matchs.list_of_matchs)
        # tournament.add_tour(tour)

    def generate_pairs(players):
        """
        Generate pairs of players from a list, sorting them by descending points.

        Args:
            players (list): A list of player objects, each having a `points` attribute.

        Returns:
            list: Alist of tuples,where each tuple contains two paired players
        """
        players = sorted(players, key=lambda x: x.points, reverse=True)
        pairs = []
        while players: 
            player1 = players.pop(0)
            player2 = players.pop(0)
            pairs.append((player1, player2))
        return pairs
    
    def get_name_by_id(self):
        if self.tournament.list_player:
            players_name_list = Players.load_info_players_by_id(
                self.tournament.list_player
            )
        return players_name_list
    
    def next_tour(self):
        try:
            self.view.display_string(self.tournament)
            print(self.tournament.current_tour)
            input()
            self.tournament.add_1_to_current_tour()
            tour = Tours(self.tournament.current_tour)
            tour.rename_as_round()
            self.generate_pairs(tour)
            self.tournament.list_of_tours.append(tour.__dict__)
            tournament_dict = self.tournament.__dict__
            # self.tournament.update(self.tournament.name, tournament_dict)
            Tournaments.clear_json_tournament
            [tournament.save() for tournament in self.tournaments]
            print(tournament_dict)
            
            tour.start()
        except UnboundLocalError:
            self.view.display_string("Pas de tournois créé")
        except AttributeError:
            self.view.display_string("pas de tournoi créé")