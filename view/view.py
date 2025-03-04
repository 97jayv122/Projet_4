from tabulate import tabulate
from datetime import datetime
from controllers.maincontroller import Constant
from controllers.tournamentmanagement import ConstantTournamentManagement
from controllers.controllertournament import ConstantTournament
from controllers.controllerreport import ConstantReport
from controllers.controllerplayer import ConstantPlayer
from controllers.controllertournamentreport import ConstantTournamentReport
from view.utils import Utils

VALIDATE_CHOICE = "\nEntré votre choix : "
WRONG_DATE = "\nVeuillez entrer un bon format de date"
PRESS_ENTER = "\nAppuyer sur entrée pour continuer..."


class View:
    def home_menu(self):
        """
        Display the main menu of the application and prompts the useer to make a choice.

        The main menu contains the following options:
            - Enter the player menu.
            - Enter the tournament manager.
            - View reports.
            - Exit program.

        Returns:
            str: The validated user choice.
        """
        Utils.clear()
        print("-" * 10 + " Menu principal " + "-" * 10)
        print("\n" + Constant.PLAYER_MENU + ". pour entrer dans le menu joueurs.")
        print(
            "\n"
            + Constant.TOURNAMENT_MENU
            + ". pour entrer dans le gestionnaire de tournoi."
        )
        print("\n" + Constant.DISPLAY_REPORTS + ". pour voir les rapports.")
        print("\n" + Constant.EXIT_PROGRAM + ". pour quitter le programme.")
        return input(VALIDATE_CHOICE)

    def player_menu(self):
        """
        Display the player menu of the application and prompts the user to make a choice.

        The player menu contains the following options:
            - Add a player.
            - List players.
            - Modify player.
            - Delete a player.
            - Return to the main menu.

        Returns:
            str: The validated user choice.
        """
        Utils.clear()
        print("-" * 10 + " Menu Joueurs " + "-" * 10)
        print("\n" + ConstantPlayer.ADD_PLAYER + ". pour entrer des joueur")
        print("\n" + ConstantPlayer.DISPLAY_PLAYER + ". pour lister les joueurs")
        print("\n" + ConstantPlayer.MODIFY_PLAYER + ". pour modifier un joueur.")
        print("\n" + ConstantPlayer.SUPPRESS_PLAYER + ". pour supprimer un joueur.")
        print(
            "\n"
            + ConstantPlayer.RETURN_MAIN_MENU
            + ". pour retourner au menu principal."
        )
        return input(VALIDATE_CHOICE)

    def tournamament_management_menu(self):
        """
        Displays the tournament management menu of the application and prompts the user to make a

        The tournament menu contains the followinng options:
            - Create a new tournament.
            - Selecet players.
            - Remove players.
            - Start the tournament.
            - Delete the tournament.
            - Return to the main menu.

        Returns:
            str: The valadated user choice.
        """
        Utils.clear()
        print("-" * 10 + " Menu Tournois " + "-" * 10)
        print(
            "\n"
            + ConstantTournamentManagement.CREATE_A_TOURNAMENT
            + ". Nouveau tournoi"
        )
        print(
            "\n"
            + ConstantTournamentManagement.SELECT_PLAYER
            + ". Sélection des joueurs"
        )
        print(
            "\n" + ConstantTournamentManagement.DELETE_PLAYER + ". Retirer des joueurs"
        )
        print(
            "\n"
            + ConstantTournamentManagement.START_TOURNAMENT
            + ". Commencé le tournoi"
        )
        print(
            "\n"
            + ConstantTournamentManagement.DELETE_TOURNAMENT
            + ". Supprimer un tournoi"
        )
        print(
            "\n"
            + ConstantTournamentManagement.ADD_DESCRIPTION
            + ". Ajouter une description à un tournoi."
        )
        print(
            "\n"
            + ConstantTournamentManagement.RETURN_MAIN_MENU
            + ". pour retourner au menu principal."
        )
        return input(VALIDATE_CHOICE)

    def tournament_menu(self):
        """
        Display the tournament menu of the application and prompts the user to make a choice.

        The tournament menu contains the following options:
            - Start a round.
            - End a round.
            -Load previous pairs.
            -Return to the tournament management menu.

        Returns:
            str: The validated user choice.
        """
        Utils.clear()
        print("-" * 10 + " Menu Tournois " + "-" * 10)
        print("\n" + ConstantTournament.START_A_TOUR + ". Commencer un tour")
        # print(
        #     "\n" + ConstantTournament.END_A_TOUR +
        #     ". Terminer le tour"
        #     )
        print(
            "\n"
            + ConstantTournament.LOAD_PREVIOUS_TOUR
            + ". Charger les paires précédentes"
        )
        print(
            "\n"
            + ConstantTournament.RETURN_TOURNAMENT_MANAGEMENT_MENU
            + ". pour retourner au menu gestionnaire de tournoi."
        )
        return input(VALIDATE_CHOICE)

    def report_menu(self):
        """
        Displays the report menu of the application and proompts the user to make a choice.

        The report menu contains the following options:
            - Display tournaments.
            - Tournament report.
            - Report of players in the database.
            - Return to the main menu.

        Returns:
            str: The validate user choice.
        """
        Utils.clear()
        print("-" * 10 + " Menu Rapport " + "-" * 10)
        print("\n" + ConstantReport.TOURNAMENTS + ". Afficher les tournois")
        print("\n" + ConstantReport.TOURNAMENT_SELECT + ". Rapport d'un tournoi")
        print(
            "\n" + ConstantReport.PLAYERS + ". Rapport des joueurs de la base de donnée"
        )
        print(
            "\n"
            + ConstantReport.RETURN_MAIN_MENU
            + ". pour retourner au menu principal."
        )
        return input(VALIDATE_CHOICE)

    def report_menu_tournament(self):
        """
        Displays the report tournament menu of the application and prompts the user to make a choice.

        The report tournament menu contains the following options:
            - Report tournament players.
            - Report of tournament.
            - Return to main menu report.

        Returns:
            str: The validate user choice.
        """
        Utils.clear()
        print("-" * 10 + " Menu Rapport tournoi" + "-" * 10)
        print(
            "\n"
            + ConstantTournamentReport.PLAYERS_TOURNAMENT
            + ". Rapport des joueurs du tournoi"
        )
        print("\n" + ConstantTournamentReport.TOURNAMENT_INFO + ". Rapport du tournoi")
        print(
            "\n"
            + ConstantTournamentReport.RETURN_REPORT_MAIN_MENU
            + ". pour retourner au menu gestionnaire de tournoi."
        )
        return input(VALIDATE_CHOICE)

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
        file_tournament["place"] = input("\nEntrer le lieu du tournoi : ")
        # Récupération et stockage de la date de début
        date_start = Utils.get_valid_date(
            "\nEntrer la date de début du tournoi (ex: 01/02/2022) : ", WRONG_DATE
        )
        file_tournament["date_start"] = date_start
        while True:
            date_end = Utils.get_valid_date(
                "\nEntrer la date de fin du tournoi (ex: 01/02/2022) : ", WRONG_DATE
            )
            if date_end == "":
                # Autoriser une date vide si c'est souhaité
                file_tournament["date_end"] = date_end
                break

            # Conversion des dates en objets datetime pour la comparaison
            start_dt = datetime.strptime(date_start, "%d/%m/%Y")
            end_dt = datetime.strptime(date_end, "%d/%m/%Y")
            if end_dt >= start_dt:
                file_tournament["date_end"] = date_end
                break
            else:
                print(
                    "La date de fin doit être supérieure à la date de début. Veuillez réessayer."
                )

        file_tournament["number_player"] = Utils.get_number_integrer(
            "\nEntrer le nombre de joueur du tournoi :"
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
                number = int(input("Entrez le nombre de participants en chiffre : "))
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
        file_player["last_name"] = input("Entrer le nom du joueur : ")
        file_player["date_of_birth"] = Utils.get_valid_date(
            "Entrer la date de naissance du joueur(01/12/2003) : ", WRONG_DATE
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
        player_data["last_name"] = input("Entrer le nom du joueur : ")
        player_data["date_of_birth"] = Utils.get_valid_date(
            "Entrer la date de naissance du joueur(01/12/2003) : ", WRONG_DATE
        )

        return player_data

    def display_table(self, datas, prompt=""):
        Utils.clear()
        index = [index for index in range(1, len(datas) + 1)]
        print(tabulate(datas, headers="keys", tablefmt="fancy_grid", showindex=index))
        print(prompt)

    def display_color_player(self, color_player):
        Utils.clear()
        table = []
        for player, color in color_player.items():
            table.append([player, color])
        print(tabulate(table, headers=["Joueur", "couleur"], tablefmt="fancy_grid"))
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

            print(f"Fin ! du match de {player_1} VS {player_2}\n")
            try:
                score_player_1 = float(input(f"Entrer le score de {player_1} : "))
                score_player_2 = Utils.check_score(score_player_1)
                if score_player_2 is not None:
                    return score_player_1, score_player_2
                else:
                    print("Score invalide. Veuillez entrer 1, 0.5 ou 0.")
                    input(PRESS_ENTER)
            except ValueError:
                print("Veuillez entrer un chiffre")
                input(PRESS_ENTER)

    def select_tournament(self, datas):
        while True:
            try:
                user_input = int(
                    input(
                        "\nEntrez l'index de l'élément que vous souhaitez sélectionner : "
                    )
                )
                if 1 <= user_input <= len(datas):
                    return user_input
                else:
                    print(
                        f"Index invalide. Veuillez entrer un nombre entre 1 et {len(datas)}."
                    )
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def display_string(self, datas):
        Utils.clear()
        print(datas)
        input(PRESS_ENTER)

    def choose_player_to_remove(self):
        input("")

    def press_enter(self):
        input(PRESS_ENTER)

    def display_tournament_info_table(self, tournament_info):
        Utils.clear()
        # Affichage des infos générales du tournoi
        general_keys = [
            "Nom du tournoi", "Lieu du tournoi", "Nombre de joueurs",
            "Date de début", "Date de fin", "Nombre de tours",
            "Description", "Statut"
        ]
        general_table = []
        for key in general_keys:
            value = tournament_info.get(key, "")
            general_table.append([key, value])

        print(tabulate(general_table, headers=["Champ", "Valeur"], tablefmt="fancy_grid"))

        # Affichage des infos de chaque tour
        tours = tournament_info.get("Tours", [])
        for tour in tours:
            print("\nTour n°", tour.get("Tour"))
            # Conversion des timestamps en dates lisibles
            date_start = tour.get("Date de début")
            date_end = tour.get("Date de fin")
            date_start = datetime.fromtimestamp(date_start).strftime('%Y-%m-%d %H:%M:%S')
            date_end = datetime.fromtimestamp(date_end).strftime('%Y-%m-%d %H:%M:%S')

            tour_table = [
                ["Tour", tour.get("Tour", "")],
                ["Date de début", date_start],
                ["Date de fin", date_end],
                ["Statut", tour.get("Statut", "")]
            ]
            print(tabulate(tour_table, headers=["Champ", "Valeur"], tablefmt="fancy_grid"))

            # Affichage des matchs pour ce tour
            print("Matchs:")
            match_table = []
            matchs = tour.get("Matchs", [])
            for match in matchs:
                joueur1 = match.get("Joueur 1", {})
                joueur2 = match.get("Joueur 2", {})
                ligne = [
                    f"{joueur1.get('Nom', '')} (score: {joueur1.get('Score', '')})",
                    f"{joueur2.get('Nom', '')} (score: {joueur2.get('Score', '')})"
                ]
                match_table.append(ligne)
            if match_table:
                print(tabulate(match_table, headers=["Joueur 1", "Joueur 2"], tablefmt="fancy_grid"))
            else:
                print("Aucun match enregistré pour ce tour.")

    def request_enter_description(self, name):
        Utils.clear()
        print("*"*10 + "Description" + "*"*10 + "\n")
        contents_description = input(f"Veuillez saisir une description pour le tournoi ({name}): ")
        return contents_description
