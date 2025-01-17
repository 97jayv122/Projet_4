from models.players import Players
from models.tournament import Tournament
from models.tours import Tours
from models.matchs import Matchs
from view.utils import Utils


class ControllerTournament:
    def __init__(self, view):
        self.view = view
  
    def run(self):
        while True:
            Utils.clear()
            action = self.view.tournament_menu()
            match action:
                case "1":
                    Players.instances_load()
                    info_tournament = self.view.request_create_tournament()
                    tournament = Tournament.from_dict(info_tournament)
                    tournament.save()
                    try:
                        tournament.list_player = self.view.select_player(
                            Players.list_of_player
                            )
                    except ValueError:
                        print("Veuillez entrer un bon format.")
                    tournament.save()

                case "2":
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
                

                case "3":
                    """  """
                    try:
                        tours.end()
                        [match.score_update()
                         for match in Matchs.list_of_matchs]
                    except UnboundLocalError:
                        print("Pas de matchs commencé")

                case "4":
                    tournament.save()

                case "5":
                    Players.load_data()
                    tournament = Tournament.load()
                case "x":
                    break

                case _:
                    print("Choix inconnue.")
