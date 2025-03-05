from models.players import Players
from models.tournament import Tournaments
from controllers.controllertournamentreport import ControllerTournamentReport


class ConstantReport:
    """
    Constants representing the report menu options.
    """
    TOURNAMENTS = "1"
    TOURNAMENT_SELECT = "2"
    PLAYERS = "3"
    RETURN_MAIN_MENU = "x"


class ControllerReport:
    """
    Controller for generating reports.

    Provides functionality for viewing tournaments, selecting a tournament report,
    and displaying sorted player lists.
    """
    def __init__(self, view):
        """
        Initialize the report controller with a view.

        Parameters:
            view: The view instance used for displaying menus and tables.
        """
        self.view = view
        self.tournaments = None

    def run(self):
        """
        Run the report menu loop.

        Processes user actions to view tournaments, tournament reports, or players.
        """
        while True:
            action = self.view.report_menu()
            match action:
                case ConstantReport.TOURNAMENTS:
                    self.get_tournaments_name()
                    self.view.press_enter()

                case ConstantReport.TOURNAMENT_SELECT:
                    self.get_tournaments_name()
                    index = self.view.select_tournament(self.tournaments)
                    # Subtract 1 from index because list indices start at 0
                    self.run_tournament_report(self.tournaments[int(index) - 1])

                case ConstantReport.PLAYERS:
                    self.get_player_sorted()
                    self.view.press_enter()

                case ConstantReport.RETURN_MAIN_MENU:
                    break

    def get_player_sorted(self):
        """
        Display a sorted list of players alphabetically.
        """
        prompt = "Liste des joueurs par ordre alphabétique."
        players = Players.load()
        players_sorted = sorted(players, key=lambda x: (x.last_name.capitalize(), x.first_name.capitalize()))
        players_dict_sorted = [player.to_dict() for player in players_sorted]
        self.view.display_table(players_dict_sorted, prompt)

    def get_tournaments_name(self):
        """
        Display a list of tournaments.
        """
        prompt = "Liste des tournois."
        tournaments = Tournaments.load()
        self.tournaments = tournaments
        tournaments_dict = [
            {
                "Nom du tournoi": tournament.name,
                "Date de début": tournament.date_start,
                "Date de fin": tournament.date_end,
            }
            for tournament in tournaments
        ]
        self.view.display_table(tournaments_dict, prompt)

    def run_tournament_report(self, tournament):
        """
        Launch the tournament report for the given tournament.

        Parameters:
            tournament: The tournament object for which to run the report.
        """
        controllertournamentreport = ControllerTournamentReport(self.view, tournament)
        controllertournamentreport.run()
