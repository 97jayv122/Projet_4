from models.players import Players
from models.tournament import Tournament
from models.tours import Tours
from models.matchs import Matchs
from view.utils import Utils


class ControllerTournament:
    CREATE_A_TOURNAMENT = "1"
    SELECT_PLAYER = "2"
    START_A_TOUR = "3"
    END_A_TOUR = "4"
    RETURN_MAIN_MENU = "x"
    def __init__(self, view):
        self.view = view
  
    def run(self):
        while True:
            Utils.clear()
            action = self.view.tournament_menu()
            match action:
                case ControllerTournament.CREATE_A_TOURNAMENT:
                    self.create_tournament()

                case ControllerTournament.SELECT_PLAYER:
                    self.player_selection()

                case ControllerTournament.START_A_TOUR:
                    self.start_tour()

                case ControllerTournament.END_A_TOUR:
                    self.end_tour()

                case "5":
                    tournament.save()

                case "6":
                    Players.load_data()
                    tournament = Tournament.load()
                case ControllerTournament.RETURN_MAIN_MENU:
                    break

                case _:
                    print("Choix inconnue.")
                    input("Appuyer sur entrée pour continuer...")

    def create_tournament(self):
        info_tournament = self.view.request_create_tournament()
        tournament = Tournament.from_dict(info_tournament)
        tournament.save()
        tournament.instance_clear()

    def player_selection(self):
        tournament = Tournament.load()
        Players.instances_load()
        try:
            tournament.list_player = self.view.select_player(
                Players.list_of_player
                )
            Players.clear_instances()
        except ValueError:
            print("Veuillez entrer un bon format.")
        tournament.save()
        tournament.instance_clear()
        Players.clear_instances()

    def update_score(self, match, player_1, player_2):
        """ """
        score_player_1, score_player_2 = self.view.requests_score(
            player_1, player_2
            )
        match.score_update(score_player_1, score_player_2)

    def start_tour(self):
        try:
            tournament = Tournament.load()
            tours = Tours(tournament.list_player)
            tours.make_first_tour()
            self.view.display(tours.group_by_two)
            match = [Matchs(
                player_1, player_2
                )
                for player_1, player_2 in tours.group_by_two]
            [match.random_color() for match in Matchs.list_of_matchs]
            tours.start()
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