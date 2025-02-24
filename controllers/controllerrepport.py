from models.players import Players
from models.tournament import Tournaments
from models.tours import Tours
from models.matchs import Matchs


class ConstantReport:

    TOURNAMENTS = "1"
    PLAYERS = "2"
    RETURN_TOURNAMENT_MANAGEMENT_MENU = "x"

class ControllerRepport:
    def __init__(self, view):
        self.view = view

    def run(self):
        while True:
            action = self.view.report_menu()
            match action:
                case ConstantReport.TOURNAMENTS:
                    self.get_tournaments_name()
                case ConstantReport.PLAYERS:
                    self.get_player_sorted()

    def get_player_sorted(self):
        players =  Players.load()
        print(players)
        # players = [player.name for player in players]
        # print(players)
        # players_sorted = sorted(players)
        # print(players_sorted)
        # input()
        players_sorted = sorted(players, key=lambda x: (x.name).capitalize())
        print(players_sorted)
        players.sort()
        print(players)
        input()
        # players.sort()
        # print(players)
        # print(players.sort())
        # input()
    def get_tournaments_name(self):
        tournaments = Tournaments.load()
        