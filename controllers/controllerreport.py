from models.players import Players
from models.tournament import Tournaments
from models.tours import Tours
from controllers.controllertournamentreport import ControllerTournamentReport
from models.matchs import Matchs



class ConstantReport:

    TOURNAMENTS = "1"
    TOURNAMENT_SELECT = "2"
    PLAYERS = "3"
    RETURN_MAIN_MENU = "x"

class ControllerReport:
    def __init__(self, view):
        self.view = view
        self.tournaments = None

    def run(self):
        while True:
            action = self.view.report_menu()
            match action:
                case ConstantReport.TOURNAMENTS:
                    self.get_tournaments_name()

                case ConstantReport.TOURNAMENT_SELECT:
                    self.get_tournaments_name()
                    index =  self.view.select_tournament(self.tournaments)
                    self.run_tournament_report(self.tournaments[int(index) - 1])

                case ConstantReport.PLAYERS:
                    self.get_player_sorted()

    def get_player_sorted(self):
        prompt = 'Liste des joueurs par ordre alphabétique(nom).'
        players =  Players.load()
        players_sorted = sorted(players, key=lambda x: (x.last_name).capitalize())
        players_dict_sorted = [player.to_dict() for player in players_sorted]
        self.view.display_table(players_dict_sorted, prompt)
        self.view.press_enter()

    def get_tournaments_name(self):
        prompt = "Liste des tournois."
        tournaments = Tournaments.load()
        self.tournaments = tournaments
        tournaments_dict = [
            {
                "Nom du tournoi": tournament.name,
                "Date de début": tournament.date_start,
                "Date de fin": tournament.date_end
                }
                for tournament in tournaments
                ]
        self.view.display_table(tournaments_dict, prompt)
        self.view.press_enter()

    def run_tournament_report(self, tournament):
        controllertournamentreport = ControllerTournamentReport(self.view, tournament)
        controllertournamentreport.run()
