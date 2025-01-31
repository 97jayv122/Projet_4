from random import shuffle
from models.players import Players
from models.tournament import Tournament
from models.tours import Tours
from models.matchs import Matchs
from view.utils import Utils


class ConstantTournament:

    START_A_TOUR = "1"
    END_A_TOUR = "2"
    RETURN_MAIN_MENU = "x"

class ControllerTournament:

    def __init__(self, view, name_tournament):
        self.view = view
        self.name_tournament = name_tournament

    def run(self):
        while True:
            Utils.clear()
            action = self.view.tournament_menu()
            match action:

                case ConstantTournament.START_A_TOUR:
                    self.start_tour()

                case ConstantTournament.END_A_TOUR:
                    self.end_tour()

                case "5":
                    tournament.save()

                case "6":
                    tournament = Tournament.load(self.name_tournament)
                case ConstantTournament.RETURN_MAIN_MENU:
                    
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
        shuffle(tour.list_player_of_tournament)  # Mélange aléatoire des joueurs
        tour.matchs_list_by_round = []
        for i in range(0, len(tour.list_player_of_tournament), 2):
            if i + 1 < len(tour.list_player_of_tournament):
                player_1 = tour.list_player_of_tournament[i]
                player_2 = tour.list_player_of_tournament[i + 1]
                match = Matchs(player_1, player_2)
                match.assign_random_colors()
                match.score_update(0, 0)
                self.view.display_string(match.color_of_player)
                tour.matchs_list_by_round.append(match.to_dict())

    def start_tour(self):
        try:
            tournament = Tournament.load(self.name_tournament)
            self.view.display_string(tournament)
            tour = Tours(tournament.list_player)
            self.generate_first_matchs(tour)
            tournament.save()
            
            # tour.start()
        except UnboundLocalError:
            print("Pas de tournois créé")
        except AttributeError:
            print("pas de tournoi créé")

    def end_tour(self):
        """  """
        try:
            # tours.end()
            [self.update_score(match, match.player_1, match.player_2)
                for match in Matchs.list_of_matchs]
        except UnboundLocalError:
            print("Pas de matchs commencé")

        tour.recovery_list_of_matchs(Matchs.list_of_matchs)
        tournament.add_tour(tour)


    def generate_pairs(players):
        players = sorted(players, key=lambda x: x.points, reverse=True)
        pairs = []
        while players: 
            player1 = players.pop(0)
            player2 = players.pop(0)
            pairs.append((player1, player2))
        return pairs
