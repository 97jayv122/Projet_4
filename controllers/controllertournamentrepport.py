from models.players import Players
from models.tournament import Tournaments
from models.tours import Tours
from models.matchs import Matchs


class ConstantTournamentRepport:

    PLAYERS_TOURNAMENT = "1"
    TOURNAMENT_INFO = "2"
    RETURN_TOURNAMENT_MANAGEMENT_MENU = "x"

class ControllerTournamentRepport:
    def __init__(self, view, tournament):
        self.view = view
        self.tournament = tournament

    def run(self):
        while True:
            action = self.view.repport_menu_tournament()
            match action:
                case ConstantTournamentRepport.PLAYERS_TOURNAMENT:
                    self.get_player_tournament_sorted()

                case ConstantTournamentRepport.TOURNAMENT_INFO:
                    pass


    def get_player_tournament_sorted(self):
        prompt = 'Liste des joueurs du tournoi par ordre alphabétique(nom).'
        players =  Players.load_by_ids(*self.tournament.list_player)
        players_sorted = sorted(players, key=lambda x: (x.name).capitalize())
        players_dict_sorted = [player.to_dict() for player in players_sorted]
        self.view.display_table(players_dict_sorted, prompt)


