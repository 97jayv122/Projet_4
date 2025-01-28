from models.players import Players
from controllers.controllertournament import ControllerTournament
from models.tournament import Tournament, FOLDER_TOURNAMENT
from view.utils import Utils
import os


class ConstantTournamentManagement:
    CREATE_A_TOURNAMENT = "1"
    SELECT_TOURNAMENT = "2"
    SELECT_PLAYER = "3"
    START_TOURNAMENT = "4"
    RETURN_MAIN_MENU = "x"

class TournamentManagement:
    def __init__(self, view):
        self.view = view
        self.tournament = ""

    def list_files_in_directory(self, directory):
        try:
            if not os.path.isdir(directory):
                print(f"Erreur : '{directory}' n'est pas un répertoire vzlide.")
                return[]
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            return files
        except Exception as e:
            print(f"Erreur lors de la lecture du répertoire : {e}")
            return []
  
    def run(self):
        while True:
            Utils.clear()
            action = self.view.tournamament_management_menu()
            match action:
                case ConstantTournamentManagement.CREATE_A_TOURNAMENT:
                    self.create_tournament()
                    self.player_selection()

                case ConstantTournamentManagement.SELECT_TOURNAMENT:
                    list_files = self.list_files_in_directory(FOLDER_TOURNAMENT)
                    formated_list_files = [[index + 1, file] for index, file in enumerate(list_files)]
                    self.tournament = self.view.select_of_list_file(formated_list_files)

                case ConstantTournamentManagement.SELECT_PLAYER:
                    self.player_selection()

                case ConstantTournamentManagement.START_TOURNAMENT:
                    self.run_controller_tournament()

                # case "5":
                #     tournament.save()

                # case "6":
                #     tournament = Tournament.load()
                case ConstantTournamentManagement.RETURN_MAIN_MENU:
                    break

                case _:
                    print("Choix inconnue.")
                    input("Appuyer sur entrée pour continuer...")

    def create_tournament(self):
        info_tournament = self.view.request_create_tournament()
        tournament = Tournament.from_dict(info_tournament)
        tournament.save()
        self.tournament = tournament.name
        tournament.instance_clear()

    def player_selection(self):
        tournament = Tournament.load(self.tournament)
        Players.instances_load()
        data_players = [player.to_dict() for player in Players.list_of_player]
        self.view.display_table(data_players)
        try:
            tournament.list_player = self.view.select_player(Players.list_of_player)
            Players.clear_instances()
        except ValueError:
            print("Veuillez entrer un bon format.")
        print('cei est un test')
        tournament.save()
        tournament.instance_clear()
        Players.clear_instances()

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
                controllertournament = ControllerTournament(self.view, self.tournament)
                controllertournament.run()
        else:
            self.view.display_string(
                "Veuillez sélectiionner ou créer un nouveau tournoi"
                )
