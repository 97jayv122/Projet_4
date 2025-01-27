import json
from tabulate import tabulate
from controllers.maincontroller import Constant
from controllers.tournamentmanagement import ConstantTournamentManagement
from controllers.controllertournament import ConstantTournament
from controllers.controllerplayer import ConstantPlayer
from view.utils import Utils
WRONG_DATE = "Veuillez entrer un bon format de date"


class View:
    def home_menu(self):
        print("-" * 10 + " Menu principal " + "-" * 10)
        print()
        print(Constant.PLAYER_MENU + ". pour entrer dans le menu joueurs.")
        print(Constant.TOURNAMENT_MENU + ". pour entrer dans le gestionnaire de tournoi.")
        print(Constant.DISPLAY_REPORTS + ". pour voir les rapports.")
        print(Constant.EXIT_PROGRAM + ". pour quitter le programme.")
        print()
        return input("Entrer votre choix : ")

    def player_menu(self):
        print("-" * 10 + " Menu Joueurs " + "-" * 10)
        print()
        print(ConstantPlayer.ADD_PLAYER + ". pour entrer des joueur")
        print(ConstantPlayer.DISPLAY_PLAYER + ". pour lister les joueurs")
        print(ConstantPlayer.MODIFY_PLAYER + ". pour modifier un joueur.")
        print(ConstantPlayer.SUPPRESS_PLAYER + ". pour supprimer un joueur.")
        print(ConstantPlayer.RETURN_MAIN_MENU + ". pour retourner au menu principal.")
        print()
        return input("Entrer votre choix : ")
    
    def tournamament_management_menu(self):
        print("-" * 10 + " Menu Tournois " + "-" * 10)
        print()
        print(ConstantTournamentManagement.CREATE_A_TOURNAMENT + ". Nouveau tournoi")
        print(ConstantTournamentManagement.SELECT_TOURNAMENT + ". Sélectionner un tournoi")
        print(ConstantTournamentManagement.SELECT_PLAYER + ". Sélection des joueurs")
        print(ConstantTournamentManagement.START_TOURNAMENT + ". Commencé le tournoi")
        print(ConstantTournamentManagement.RETURN_MAIN_MENU + ". pour retourner au menu principal.")
        print()
        return input("Entrer votre choix : ")

    def tournament_menu(self):
        print("-" * 10 + " Menu Tournois " + "-" * 10)
        print()
        print(ConstantTournament.START_A_TOUR + ". Commencer un tour")
        print(ConstantTournament.END_A_TOUR + ". Terminer un tour")
        print("5. Sauvegarder le tournoi")
        print("6. Charger le tournoi")
        print(ConstantTournament.RETURN_MAIN_MENU + ". pour retourner au menu gestionnaire de tournoi.")
        print()
        return input("Entrer votre choix : ")

    def select_player(self, players):
        player_tournament = []
        print("")
        print("Sélectionnez les joueurs pour le tournoi")
        for i, player in enumerate(players):
            print(f"{i + 1}. {player}")
            print("=" * 10)
        players_enter = input(
            "Entrer les numéros des joueurs séparés par une virgule : "
            )
        split_players = players_enter.split(",")
        for player in split_players:
            player_tournament.append(players[int(player) - 1])
        return player_tournament

    def request_create_tournament(self):
        file_tournament = {}
        file_tournament["name"] = input("Entrer le nom du tournoi : ")
        file_tournament["location"] = input("Entrer le lieu du tournoi : ")
        file_tournament["date_start"] = Utils.get_valid_date(
            "Entrer la date de début du tournoi : ",
            WRONG_DATE
        )
        file_tournament["date_end"] = Utils.get_valid_date(
            "Entrer la date de fin du tournoi : ",
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
                if number <= 0:
                    print("Veuillez entrer un nombre supérieur à 0")
                    input("Appuyer sur entrée pour continuer...")
                    continue
                return number
            except ValueError:
                print("Entrée invalide. Veuillez entrer un chiffre.")
                input("Appuyer sur entrée pour continuer...")

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
                f"Entrez l'identifiant national d'échecs du joueur à {action}"
                 " ou taper 'x' pour annuler : "
                 )
            if chess_id.lower() == "x":
                print("action annulé")
                return None
            if Utils.valide_national_chess_identifier(chess_id):
                return chess_id
            else:
                print("Identifiant est invalide")
                input("Appuyer sur entrée pour continuer...")

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
        input("Appuyer sur entrée pour continuer...")

    def display_json(self, datas):
        print(json.dumps(datas, indent=4))
        input("Appuyer sur entrée pour continuer...")

    def display_table(self, datas):
        Utils.clear()
        print(tabulate(datas, headers="keys", tablefmt="fancy_grid"))
        input("Appuyer sur entrée pour continuer...")

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
                    input("Appuyer sur entrée pour continuer...")
            except ValueError:
                print("Veuillez entrer un chiffre")
                input("Appuyer sur entrer pour continuer...")

    def display_choice_color(self):
        pass
    
    def select_of_list_file(self, datas):
        headers = ['Index', 'File']
        print(tabulate(datas, headers=headers, tablefmt='grid'))
        while True:
            try:
                user_input = int(input("\nEntrez l'index de l'élément que vous souhaitez sélectionner : "))
                if 1 <= user_input < len(datas):
                    return datas[user_input - 1][1]
                else:
                    print(f"Index invalide. Veuillez entrer un nombre entre 1 et {len(datas) - 1}.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    
    def display_string(self, datas):
        print(datas)
        print("Le tournoi à été correctement chargé.")
        input("Appuyé sur une touche pour continuer")

        