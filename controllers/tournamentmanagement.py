from models.players import Players
from controllers.controllertournament import ControllerTournament
from models.tournament import Tournaments, FOLDER_TOURNAMENT
from view.utils import Utils
import os



class ConstantTournamentManagement:
    CREATE_A_TOURNAMENT = "1"
    SELECT_PLAYER = "2"
    DELETE_PLAYER = "3"
    START_TOURNAMENT = "4"
    DELETE_TOURNAMENT = "5"
    RETURN_MAIN_MENU = "x"

class TournamentManagement:
    def __init__(self, view):
        self.view = view
        tournaments = Tournaments.load()
        self.tournaments = tournaments 
        self.tournament = None
        self.players = Players.load()


    def run(self):
        while True:
            action = self.view.tournamament_management_menu()
            self.tournaments = Tournaments.load()
            match action:
                case ConstantTournamentManagement.CREATE_A_TOURNAMENT:
                    self.create_tournament()
                    # self.player_selection()

                case ConstantTournamentManagement.SELECT_PLAYER:
                    self.select_tournament()
                    self.player_selection()

                case ConstantTournamentManagement.DELETE_PLAYER:
                    self.select_tournament()
                    self.remove_players_from_tournament()

                case ConstantTournamentManagement.START_TOURNAMENT:
                    self.select_tournament()
                    self.run_controller_tournament()

                case ConstantTournamentManagement.DELETE_TOURNAMENT:
                    self.select_tournament()
                    names_tournaments = self.get_tournament_name()
                    if names_tournaments is not None:
                        index = self.view.select_tournament(names_tournaments)
                        del self.tournaments[index]
                        Tournaments.save_all(self.tournaments)
                    else:
                        breakpoint

                case ConstantTournamentManagement.RETURN_MAIN_MENU:
                    break

                case _:
                    print("Choix inconnue.")
                    input("Appuyer sur entrée pour continuer...")

    def get_tournament_name(self):
        if len(self.tournaments) > 1:    
            return [[tournament.name, len(tournament.list_player)] for tournament in self.tournaments]
        elif len(self.tournaments) == 1:
            return [[self.tournaments[0].name, len(self.tournaments[0].list_player)]]
        else:
            self.view.display_string("Vous n'avez pas de tournoi enregistré")
            return None
        
    def create_tournament(self):
        """
        Creates a new tournament based on user input.

        This method requests tournament information from the view layer,
        constructs a tournament instance using the provided data via the
        Tournaments.from dict() method, and saves the new tournament to
        persistant storeage
        """
        info_tournament = self.view.request_create_tournament()
        tournament = Tournaments.from_dict(info_tournament)
        tournament.save()

    def select_tournament(self):
        names_tournaments = self.get_tournament_name()
        if names_tournaments is not None:
            index = self.view.select_tournament(names_tournaments)
            self.tournament = self.tournaments[index]
        else:
            self.view.display_string("Aucun tournoi disponible.")

    def player_selection(self):
        if self.tournament is not None:
            # Players.load()
            if self.players:
                prompt = "Liste des joueurs de la base de donnée"
                data_players = [player.to_dict() for player in self.players]
                self.view.display_table(data_players, prompt)
                try:
                    self.tournament.list_player = self.view.select_player(self.players)
                    # Players.clear_instances()
                except ValueError:
                    self.view.display_string("Veuillez entrer un bon format.")
                # self.tournament.update(self.tournament.name)
                Tournaments.save_all(self.tournaments)
                self.tournament = None
                # Players.clear_instances()
            else:
                self.view.display_string("Pas de joueur rentré dans la base de donnée")
                
        else:
            self.view.display_string("Pas de tournoi sélectionner")

    def check_player_number(self):
        tournament = self.tournament
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
        if self.tournament is not None:
            tournament = self.tournament
            if tournament.list_player:
                players = Players.load_info_players_by_id(*tournament.list_player)
                index = [range(1, len(players))]
                print(players)
                input()
                prompt = "Liste des joueurs du tournoi"
                self.view.display_table(players, prompt)
                user_input = self.view.choose_player_to_remove()
                tournament.list_player.pop(user_input)
            else:
                self.view.display_string("Pas de joueur dans la liste du tournoi.")
                
        else:
            self.view.display_string("Pas de tournoi sélectionner")      

    def run_controller_tournament(self):
        """
        Run the tournament controller.
        """

        if self.tournament is not None:
            if self.check_player_number():
                controllertournament = ControllerTournament(self.view, self.tournament, self.tournaments)
                controllertournament.run()
        else:
            self.view.display_string(
                "Veuillez sélectiionner ou créer un nouveau tournoi"
                )

    def delete_tournament(self, index):
        """_summary_

        Args:
            index (_type_): _description_
        """
        self.tournament = None
        tournament_deleted = self.tournaments.pop(index)
        self.view.display_string(
            f"Le tournoi: {tournament_deleted["name"]}, à été supprimé."
            )
