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
                    info_tournament = self.view.request_create_tournament()
                    tournament = Tournament.from_dict(info_tournament)
                    tournament.save_tournament()
                    tournament.list_player = self.view.select_player(
                        Players.list_of_player
                        )
                    tournament.save_tournament()

                case "2":
                    tours = Tours(tournament.list_player)
                    tours.make_first_tour()
                    self.view.display(tours.group_by_two)
                    match = [Matchs(
                        player_1, player_2
                        )
                        for player_1, player_2 in tours.group_by_two]
                    [match.random_color() for match in Matchs.list_of_matchs]
                    tours.start_tour()
                case "3":
                    """  """
                    try:
                        tours.end_tour()
                        [match.score_update()
                         for match in Matchs.list_of_matchs]
                    except ValueError:
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
