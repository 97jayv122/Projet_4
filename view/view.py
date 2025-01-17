from controllers.maincontroller import Controller
from view.utils import Utils
from tabulate import tabulate
import json
WRONG_DATE = "Veuillez entrer un bon format de date"


class View:
    def home_menu(self):
        print("-" * 10 + " Menu principal " + "-" * 10)
        print()
        print(Controller.PLAYER_MENU + ". pour entrer dans le menu joueurs.")
        print(Controller.TOURNAMENT_MENU + ". pour entrer dans le menu tournois.")
        print(Controller.DISPLAY_REPORTS + ". pour voir les rapports.")
        print(Controller.EXIT_PROGRAM + ". pour quitter le programme.")
        print()
        return input("Entrer votre choix : ")

    def player_menu(self):
        print("-" * 10 + " Menu Joueurs " + "-" * 10)
        print()
        print("1 pour entrer des joueur")
        print("2 pour lister les joueurs")
        print("3 pour modifier un joueur.")
        print("4 pour supprimer un joueur.")
        print("x pour retourner au menu principal.")
        print()
        return input("Entrer votre choix : ")

    def tournament_menu(self):
        print("-" * 10 + " Menu Tournois " + "-" * 10)
        print()
        print("1 créer un tournoi")
        print("2 Commencer un tour")
        print("3 Rentrer les scores des joueurs")
        print("4 Sauvegarder le tournoi")
        print("5 Charger le tournoi")
        print("x pour retourner au menu principal.")
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
        chess_id = input(
            f"Entrer l'identiant national d' échecs du joueur à {action} : "
            )
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
        # player_data["national_chess_identifier"] = Utils.get_chess_identifier(
        #     "Enter l'identiant national d' échecs : ",
        #     False
        # )
        return player_data


    def display(self, datas):
        for data in datas:
            print(data)
        input("Appuyer sur entrée pour continuer...")

    def display_json(self, datas):
        print(json.dumps(datas, indent=4))
        input("Appuyer sur entrée pour continuer...")

    def display_table(self, data):
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
        input("Appuyer sur entrée pour continuer...")
