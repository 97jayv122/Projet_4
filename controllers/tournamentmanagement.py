from models.players import Players
from controllers.controllertournament import ControllerTournament
from models.management import Management, FOLDER_TOURNAMENT
from models.tournament import Tournament
from view.utils import Utils
import os


class ConstantTournamentManagement:
    CREATE_A_TOURNAMENT = "1"
    SELECT_TOURNAMENT = "2"
    SELECT_PLAYER = "3"
    START_TOURNAMENT = "4"
    DELETE_TOURNAMENT = "5"
    RETURN_MAIN_MENU = "x"

class TournamentManagement:
    def __init__(self, view):
        self.view = view
        management = Management()
        self.management = management 
        self.tournament = ''

    def get_tournament_name(self):
        if len(self.management.list_tournaments) > 1:    
            return [[tournament["name"]] for tournament in self.management.list_tournaments]
        elif len(self.management.list_tournaments) == 1:
            return [[self.management.list_tournaments[0]["name"]]]
        else:
            self.view.display_string("Vous n'avez pas de tournoi enregistré")
            return None

    def select_tournament(self, index):
        return self.management.list_tournaments[index]

    def delete_tournament(self, index):
        tournament_deleted = self.management.list_tournaments.pop(index)
        self.view.display_string(
            f"Le tournoi: {tournament_deleted["name"]}, à été supprimé."
            )
  
    def run(self):
        while True:
            Utils.clear()
            action = self.view.tournamament_management_menu()
            self.management.load()
            match action:
                case ConstantTournamentManagement.CREATE_A_TOURNAMENT:
                    self.create_tournament()
                    # self.player_selection()

                case ConstantTournamentManagement.SELECT_TOURNAMENT:
                    names_tournaments = self.get_tournament_name()
                    if names_tournaments is not None:
                        index = self.view.select_tournament(names_tournaments)
                        self.tournament = self.select_tournament(index)
                    else:
                        breakpoint

                case ConstantTournamentManagement.SELECT_PLAYER:
                    self.player_selection()

                case ConstantTournamentManagement.START_TOURNAMENT:
                    self.run_controller_tournament()

                case ConstantTournamentManagement.DELETE_TOURNAMENT:
                    names_tournaments = self.get_tournament_name()
                    if names_tournaments is not None:
                        index = self.view.select_tournament(names_tournaments)
                        self.delete_tournament(index)
                        self.management.save()
                    else:
                        breakpoint

                case ConstantTournamentManagement.RETURN_MAIN_MENU:
                    break

                case _:
                    print("Choix inconnue.")
                    input("Appuyer sur entrée pour continuer...")

    def create_tournament(self):
        info_tournament = self.view.request_create_tournament()
        tournament = Tournament.from_dict(info_tournament)
        tournament_dict = tournament.to_dict()
        self.management.create_or_update(tournament.name, tournament_dict)
        self.management.save()
        self.management.instance_clear()
        tournament.instance_clear()

    def player_selection(self):
        if self.tournament:
            tournament = Tournament.from_dict(self.tournament)
            Players.instances_load()
            if Players.list_of_player:
                prompt = "Liste des joueurs de la base de donnée"
                data_players = [player.to_dict() for player in Players.list_of_player]
                self.view.display_table(data_players, prompt)
                try:
                    tournament.list_player = self.view.select_player(Players.list_of_player)
                    Players.clear_instances()
                except ValueError:
                    self.view.display_string("Veuillez entrer un bon format.")
                tournament_dict = tournament.to_dict()
                self.management.create_or_update(tournament.name, tournament_dict)
                self.management.save()
                self.management.instance_clear()
                tournament.instance_clear()
                Players.clear_instances()
            else:
                self.view.display_string("Pas de joueur rentré dans la base de donnée")
                breakpoint
        else:
            self.view.display_string("Pas de tournoi sélectionner")
            breakpoint

    def check_player_number(self):
        tournament = Tournament.load(self.tournament)
        if len(tournament.list_player) == 4:
            return True
        
        elif len(tournament.list_player) < 4:
            missing = 4 - len(tournament.list_player)
            self.view.display_string(f"Veuillez ajouter {missing} joueurs")
            return False
        
        elif len(tournament.list_player) > 4:
            extra = len(tournament.list_player) - 4
            self.view.display_string(f"Veuillez retirer {extra} joueurs")
            return False
        else:
            return False

    def remove_players_from_tournament(self):
        tournament = Tournament.load(self.tournament)
        self.view.display_table(tournament.list_player)
        user_input = self.view.choose_player_to_remove()
        tournament.list_player.pop(user_input)

    def run_controller_tournament(self):
        """
        Run the tournament controller.
        """
        if self.tournament:
            if self.check_player_number():
                controllertournament = ControllerTournament(self.view, self.tournament, self.management)
                controllertournament.run()
        else:
            self.view.display_string(
                "Veuillez sélectiionner ou créer un nouveau tournoi"
                )
