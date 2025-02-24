import json
from tabulate import tabulate
from controllers.maincontroller import Constant
from controllers.tournamentmanagement import ConstantTournamentManagement
from controllers.controllertournament import ConstantTournament
from controllers.controllerrepport import ConstantReport
from controllers.controllerplayer import ConstantPlayer
from view.utils import Utils

VALIDATE_CHOICE = "\nEntré votre choix : "
WRONG_DATE = "\nVeuillez entrer un bon format de date"
PRESS_ENTER =  "\nAppuyer sur entrée pour continuer..."


class View:
    def home_menu(self):
        Utils.clear()
        print("-" * 10 + " Menu principal " + "-" * 10)
        print()
        print("\n" + Constant.PLAYER_MENU + ". pour entrer dans le menu joueurs.")
        print("\n" + Constant.TOURNAMENT_MENU + ". pour entrer dans le gestionnaire de tournoi.")
        print("\n" + Constant.DISPLAY_REPORTS + ". pour voir les rapports.")
        print("\n" + Constant.EXIT_PROGRAM + ". pour quitter le programme.")
        print()
        return input(VALIDATE_CHOICE)

    def player_menu(self):
        Utils.clear()
        print("-" * 10 + " Menu Joueurs " + "-" * 10)
        print()
        print("\n" + ConstantPlayer.ADD_PLAYER + ". pour entrer des joueur")
        print("\n" + ConstantPlayer.DISPLAY_PLAYER + ". pour lister les joueurs")
        print("\n" + ConstantPlayer.MODIFY_PLAYER + ". pour modifier un joueur.")
        print("\n" + ConstantPlayer.SUPPRESS_PLAYER + ". pour supprimer un joueur.")
        print("\n" + ConstantPlayer.RETURN_MAIN_MENU + ". pour retourner au menu principal.")
        print()
        return input(VALIDATE_CHOICE)
    
    def tournamament_management_menu(self):
        Utils.clear()
        print("-" * 10 + " Menu Tournois " + "-" * 10)
        print()
        print("\n" + ConstantTournamentManagement.CREATE_A_TOURNAMENT + ". Nouveau tournoi")
        print("\n" + ConstantTournamentManagement.SELECT_PLAYER + ". Sélection des joueurs")
        print("\n" + ConstantTournamentManagement.DELETE_PLAYER + ". Retirer des joueurs")
        print("\n" + ConstantTournamentManagement.START_TOURNAMENT + ". Commencé le tournoi")
        print("\n" + ConstantTournamentManagement.DELETE_TOURNAMENT + ". Supprimer un tournoi")
        print("\n" + ConstantTournamentManagement.RETURN_MAIN_MENU + ". pour retourner au menu principal.")
        print()
        return input(VALIDATE_CHOICE)

    def tournament_menu(self):
        Utils.clear()
        print("-" * 10 + " Menu Tournois " + "-" * 10)
        print()
        print(ConstantTournament.START_A_TOUR + ". Commencer le premier tour")
        print(ConstantTournament.END_A_TOUR + ". Terminer un tour")
        print(ConstantTournament.LOAD_PREVIOUS_TOUR + ". Charger les paires précédentes")
        print(ConstantTournament.RETURN_TOURNAMENT_MANAGEMENT_MENU + ". pour retourner au menu gestionnaire de tournoi.")
        print()
        return input("Entrer votre choix : ")
    
    def report_menu(self):
        Utils.clear()
        print("-" * 10 + " Menu Rapport " + "-" * 10)
        print()
        print(ConstantReport.TOURNAMENTS + ". Rapport tournoi")
        print(ConstantReport.PLAYERS + ". Rapport joueur")
        print(ConstantReport.RETURN_TOURNAMENT_MANAGEMENT_MENU + ". pour retourner au menu gestionnaire de tournoi.")
        print()
        return input("Entrer votre choix : ")

    def select_player(self):
        print("\nSélectionnez les joueurs pour le tournoi\n")
        index_players = input(
            "\nEntrer les numéros des joueurs séparés par une virgule : "
            )
        index_players = index_players.split(",")
        return index_players

    def request_create_tournament(self):
        Utils.clear()
        file_tournament = {}
        file_tournament["name"] = input("Entrer le nom du tournoi : ")
        file_tournament["location"] = input("\nEntrer le lieu du tournoi : ")
        file_tournament["date_start"] = Utils.get_valid_date(
            "\nEntrer la date de début du tournoi(ex:01/02/2022) : ",
            WRONG_DATE
        )
        file_tournament["date_end"] = Utils.get_valid_date(
            "\nEntrer la date de fin du tournoi(ex:01/02/2022) : ",
            WRONG_DATE
        )
        return file_tournament

    def number_add_player(self):
        """
        Prompts the user to enter the number of participants to add.

        Returns:
            int: _The number of participants entered by the user,
              which must be a positive integer.
        """        
        while True:
            Utils.clear()
            try:
                number = int(input(
                    "Entrez le nombre de participants en chiffre : "
                    ))
                if number < 0:
                    print("Veuillez entrer un nombre supérieur à 0")
                    input(PRESS_ENTER)
                    continue
                return number
            except ValueError:
                print("Entrée invalide. Veuillez entrer un chiffre.")
                input(PRESS_ENTER)

    def request_add_player(self):
        file_player = {}
        file_player["first_name"] = input("Entrer le prénom du joueur : ")
        file_player["name"] = input("Entrer le nom du joueur : ")
        file_player["date_of_birth"] = Utils.get_valid_date(
            "Entrer la date de naissance du joueur(01/12/2003) : ",
            WRONG_DATE
        )
        file_player["national_chess_identifier"] = Utils.get_chess_identifier(
            "Enter l'identiant national d' échecs : "
        )
        return file_player
    
    def request_player_id(self, action):
        while True:
            chess_id = input(
                f"\nEntrez l'identifiant national d'échecs du joueur à {action}"
                 " ou taper 'x' pour annuler : "
                 )
            if chess_id.lower() == "x":
                print("\naction annulé")
                return None
            if Utils.valide_national_chess_identifier(chess_id):
                return chess_id
            else:
                print("\nIdentifiant est invalide")
                input(PRESS_ENTER)

    def request_modify_player(self):
        player_data = {}
        player_data["first_name"] = input("Entrer le prénom du joueur : ")
        player_data["name"] = input("Entrer le nom du joueur : ")
        player_data["date_of_birth"] = Utils.get_valid_date(
            "Entrer la date de naissance du joueur(01/12/2003) : ",
            WRONG_DATE
        )

        return player_data

    def display(self, datas):
        for data in datas:
            print(data)
        input(PRESS_ENTER)

    def display_json(self, datas):
        print(json.dumps(datas, indent=4))
        input(PRESS_ENTER)

    def display_table(self, datas, prompt):
        Utils.clear()
        print(tabulate(datas, headers="keys", tablefmt="fancy_grid", showindex='always'))
        print(prompt)
        input(PRESS_ENTER)

    def requests_score(self, player_1, player_2):
        """
        Requests the scores for a match between two players with validation.
        
        Args:
            player_1 (str): The name of the first player 
            player_2 (str): The name of the second player 

        Returns:
            tuple: The scores of player_1 and player_2
        """        
        while True:
            Utils.clear()
            print(f"{player_1} VS {player_2}")
            try:
                score_player_1 = float(input(f"Entrer le score {player_1} : "))
                score_player_2 = Utils.check_score(score_player_1)
                if score_player_2 != None:
                    return score_player_1, score_player_2
                else:
                    print("Score invalide. Veuillez entrer 1, 0.5 ou 0.")
                    input(PRESS_ENTER)
            except ValueError:
                print("Veuillez entrer un chiffre")
                input(PRESS_ENTER)

    def display_choice_color(self):
        pass
    
    def select_tournament(self, datas):
        print(tabulate(datas, showindex='always', tablefmt='grid'))
        while True:
            try:
                user_input = int(input("\nEntrez l'index de l'élément que vous souhaitez sélectionner : "))
                if 0 <= user_input <= len(datas) - 1:
                    return user_input
                else:
                    print(f"Index invalide. Veuillez entrer un nombre entre 1 et {len(datas)}.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    
    def display_string(self, datas):
        Utils.clear()
        print(datas)
        input(PRESS_ENTER)

    def choose_player_to_remove(self):
        input("")
        pass