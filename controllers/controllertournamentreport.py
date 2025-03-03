from models.players import Players
from models.tournament import Tournaments
from models.tours import Tours
from models.matchs import Matchs


class ConstantTournamentReport:

    PLAYERS_TOURNAMENT = "1"
    TOURNAMENT_INFO = "2"
    RETURN_REPORT_MAIN_MENU = "x"

class ControllerTournamentReport:
    def __init__(self, view, tournament):
        self.view = view
        self.tournament = tournament

    def run(self):
        while True:
            action = self.view.report_menu_tournament()
            match action:
                case ConstantTournamentReport.PLAYERS_TOURNAMENT:
                    self.get_player_tournament_sorted()

                case ConstantTournamentReport.TOURNAMENT_INFO:
                    self.get_tournament_info()


    def get_player_tournament_sorted(self):
        message = 'Liste des joueurs du tournoi par ordre alphabétique(nom).'
        players =  Players.load_by_ids(*self.tournament.list_player)
        players_sorted = sorted(players, key=lambda x: (x.last_name).capitalize())
        players_dict_sorted = [player.to_dict() for player in players_sorted]
        self.view.display_table(players_dict_sorted, message)
        self.view.press_enter()

    def get_tournament_info(self):
        self.view.display_report("\nRappport du tournoi.\n")
        self.view.display_report(f"Lieu du tournoi: {self.tournament.place}")
        self.view.display_report(f"Nombre de joueurs: {self.tournament.number_player}")
        self.view.display_report(f"Nom du tournoi: {self.tournament.name}")
        self.view.display_report(f"Date de début: {self.tournament.date_start}")
        self.view.display_report(f"Date de fin: {self.tournament.date_end}")
        self.view.display_report(f"Nombre de tours: {self.tournament.number_of_turns}")
        self.view.display_report(f"Description: {self.tournament.description}")
        self.view.display_report(f"Statut: {self.tournament.stat}\n")

        self.view.display_report("Informations sur les tours.")
        for tour in self.tournament.list_of_tours:
            self.view.display_report(f"\nTour {tour.tour_number}.\n")
            self.view.display_report(f"Date de début: {tour.time_start}")
            self.view.display_report(f"Date de fin: {tour.time_end}")
            self.view.display_report(f"Statut: {tour.stat}\n")
            self.view.display_report("Matchs.")
            for match in tour.matchs:
                self.view.display_report(f"Joueur 1: {Players.load_by_ids(match[0][0])[0]} score: {match[0][1]}")
                self.view.display_report(f"Joueur 2: {Players.load_by_ids(match[1][0])[0]} score: {match[1][1]}")
        input()
        


