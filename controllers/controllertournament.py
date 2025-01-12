from models.players import Players
from models.tournament import Tournament
from models.tours import Tours
from models.matchs import Matchs


class ControllerTournament:
    def __init__(self, view):
        self.view = view
  
    def run(self):
        while True:
            action = self.view.tournament_menu()
            match action:
                case "1":
                    player = Players.load_data_player()
                    info_tournament = self.view.request_create_tournament()
                    tournament = Tournament.from_dict(info_tournament)
                    tournament.save_tournament()
                    try:
                        tournament.list_player = self.view.select_player(
                            Players.list_of_player
                            )
                    except ValueError:
                        print("Veuillez entrer un bon format.")
                    tournament.save_tournament()

                case "2":
                    try:
                        tournament = Tournament.load_tournament()
                        tours = Tours(tournament.list_player)
                        tours.make_first_tour()
                        self.view.display(tours.group_by_two)
                        match = [Matchs(
                            player_1, player_2
                            )
                            for player_1, player_2 in tours.group_by_two]
                        [match.random_color() for match in Matchs.list_of_matchs]
                        tours.start_tour()
                    except UnboundLocalError:
                        print("Pas de tournois créé")
                    except AttributeError:
                        print("pas de tournoi créé")
                

                case "3":
                    """  """
                    try:
                        tours.end_tour()
                        [match.score_update()
                         for match in Matchs.list_of_matchs]
                    except UnboundLocalError:
                        print("Pas de matchs commencé")

                case "4":
                    tournament.save_tournament()

                case "5":
                    player = Players.load_data_player()
                    tournament = Tournament.load_tournament()
                case "x":
                    break

                case _:
                    print("Choix inconnue.")
