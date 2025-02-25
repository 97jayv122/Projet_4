from models.players import Players
from models.tournament import Tournaments
from models.tours import Tours
from models.matchs import Matchs


class ConstantTournamentReport:

    PLAYERS_TOURNAMENT = "1"
    TOURNAMENT_INFO = "2"
    RETURN_TOURNAMENT_MANAGEMENT_MENU = "x"

class ControllerTournamentRepport:
    def __init__(self, view, tournament):
        self.view = view
        self.tournament = tournament
    def run(self):
        while True:
            action = self.view.report_menu()
            match action:
                case ConstantTournamentReport.TOURNAMENT_INFO:
                    pass

                case ConstantTournamentReport.PLAYERS_TOURNAMENT:
                    self.get_player_tournament_sorted()

    def get_player_Tournament_sorted(self):
        prompt = 'Liste des joueurs du tournoi par ordre alphabétique(nom).'
        players =  Players.load()
        players_sorted = sorted(players, key=lambda x: (x.name).capitalize())
        players_dict_sorted = [player.to_dict() for player in players_sorted]
        self.view.display_table(players_dict_sorted, prompt)

    def get_tournaments_name(self):
        prompt = "Liste des tournois."
        tournaments = Tournaments.load()
        tournaments_dict = [
            {
                "Nom du tournoi": tournament.name,
                "Date de début": tournament.date_start,
                "Date de fin": tournament.date_end
                }
                for tournament in tournaments
                ]
        self.view.display_table(tournaments_dict, prompt)
