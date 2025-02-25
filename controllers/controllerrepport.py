from models.players import Players
from models.tournament import Tournaments
from models.tours import Tours
from controllers.controllertournamentrepport import ControllerTournamentRepport
from models.matchs import Matchs



class ConstantRepport:

    TOURNAMENTS = "1"
    TOURNAMENT_SELECT = "2"
    PLAYERS = "3"
    RETURN_TOURNAMENT_MANAGEMENT_MENU = "x"

class ControllerRepport:
    def __init__(self, view):
        self.view = view
        self.tournaments = None

    def run(self):
        while True:
            action = self.view.repport_menu()
            match action:
                case ConstantRepport.TOURNAMENTS:
                    self.get_tournaments_name()

                case ConstantRepport.TOURNAMENT_SELECT:
                    self.get_tournaments_name()
                    index =  self.view.select_tournament(self.tournaments)
                    self.run_tournament_repport(self.tournaments[int(index) - 1])

                case ConstantRepport.PLAYERS:
                    self.get_player_sorted()

    def get_player_sorted(self):
        prompt = 'Liste des joueurs par ordre alphabétique(nom).'
        players =  Players.load()
        players_sorted = sorted(players, key=lambda x: (x.name).capitalize())
        players_dict_sorted = [player.to_dict() for player in players_sorted]
        self.view.display_table(players_dict_sorted, prompt)

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

    def run_tournament_repport(self, tournament):
        controllertournamentrepport = ControllerTournamentRepport(self.view, tournament)
        controllertournamentrepport.run()
