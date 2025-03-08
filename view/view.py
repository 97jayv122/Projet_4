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
PRESS_ENTER = "\nAppuyer sur entrée pour continuer..."


def display_message(func):
    """
    A decorator that clears the screen before displaying a message and
    waits for user input after the message is displayed.

    This decorator ensures that all decorated functions follow a consistent
    format where the screen is cleared before displaying a message, and the
    program pauses to wait for user confirmation.

    Args:
        func (function): The function to be wrapped, which should display a message.

    Returns:
        function: The wrapped function that includes screen clearing
                  and user input before proceeding.
    """
    def wrapper(self, *args, **kwargs):
        Utils.clear()
        func(self, *args, **kwargs)
        input(PRESS_ENTER)
    return wrapper


class View:
    def home_menu(self):
        """
        Display the main menu of the application and prompts the useer to make a choice.

        The main menu contains the following options:
            - Enter the player menu.
            - Enter the tournament manager.
            - Reports.
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
            - Remove player.
            - Start the tournament.
            - Delete the tournament.
            - Add a description to a tournament.
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
            "\n" + ConstantTournamentManagement.DELETE_PLAYER + ". Retirer un joueur"
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
            -Load previous pairings.
            -Return to the tournament management menu.

        Returns:
            str: The validated user choice.
        """
        Utils.clear()
        print("-" * 10 + " Menu Tournois " + "-" * 10)
        print("\n" + ConstantTournament.START_A_TOUR + ". Commencer un tour")
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
            - Tournament players report.
            - Tournament details report.
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
        """
        Prompt the user to select players for the tournament.

        Returns:
            list: A list of selected player indices.
        """
        print("\nSélectionnez les joueurs pour le tournoi\n")
        index_players = input(
            "\nEntrer les numéros des joueurs séparés par une virgule : "
        )
        index_players = index_players.split(",")
        return index_players

    def request_create_tournament(self):
        """
        Request tournament details from the user to create a new tournament.

        Returns:
            dict: A dictionary with tournament details.
        """
        Utils.clear()
        file_tournament = {}
        file_tournament["name"] = input("Entrer le nom du tournoi : ")
        file_tournament["place"] = input("\nEntrer le lieu du tournoi : ")
        # Récupération et stockage de la date de début
        date_start = Utils.get_valid_date(
            "\nEntrer la date de début du tournoi (ex: 01/02/2022) : "
        )
        file_tournament["date_start"] = date_start
        while True:
            date_end = Utils.get_valid_date(
                "\nEntrer la date de fin du tournoi (ex: 01/02/2022) : "
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
        Prompt the user to enter the number of players to add.

        Returns:
            int: The number of players entered by the user.
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
        """
        Request player details from the user to add a new player.

        Returns:
            dict: A dictionary with the player's details.
        """
        file_player = {}
        file_player["first_name"] = input("Entrer le prénom du joueur : ")
        file_player["last_name"] = input("Entrer le nom du joueur : ")
        file_player["date_of_birth"] = Utils.get_valid_date(
            "Entrer la date de naissance du joueur(01/12/2003) : "
        )
        file_player["national_chess_identifier"] = Utils.get_chess_identifier(
            "Enter l'identiant national d' échecs : "
        )
        return file_player

    def request_player_id(self, action):
        """
        Request a player's chess identifier for a specified action.

        Args:
            action (str): The action to perform (e.g., modify or delete).

        Returns:
            str or None: The player's chess identifier if valid, otherwise None.
        """
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
        """
        Request new details for modifying a player's information.

        Returns:
            dict: A dictionary containing updated player details.
        """
        player_data = {}
        player_data["first_name"] = input("Entrer le prénom du joueur : ")
        player_data["last_name"] = input("Entrer le nom du joueur : ")
        player_data["date_of_birth"] = Utils.get_valid_date(
            "Entrer la date de naissance du joueur(01/12/2003) : "
        )

        return player_data

    def display_table(self, datas):
        """
        Display a table of data.

        Parameters:
            datas (list of dict): A list of dictionaries representing table rows.
            prompt (str, optional): A prompt message to display after the table.
        """
        Utils.clear()
        index = [index for index in range(1, len(datas) + 1)]
        print(tabulate(datas, headers="keys", tablefmt="fancy_grid", showindex=index))

    def display_color_player(self, color_player):
        """
        Display the color assignments for players in a match.

        Parameters:
            color_player (dict): A dictionary mapping players to their assigned colors.
        """
        Utils.clear()
        table = []
        for player, color in color_player.items():
            table.append([player, color])
        print(tabulate(table, headers=["Joueur", "couleur"], tablefmt="fancy_grid"))
        input(PRESS_ENTER)

    def requests_score(self, player_1, player_2):
        """
        Request the scores for a match between two players with validation.

        Args:
            player_1 (str): The name of the first player.
            player_2 (str): The name of the second player.

        Returns:
            tuple: The scores of player_1 and player_2.
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
        """
        Prompt the user to select a tournament from a displayed list.

        Parameters:
            datas (list): A list of tournament data.

        Returns:
            int: The index of the selected tournament.
        """
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

    def press_enter(self):
        """
        Prompt the user to press enter to continue.
        """
        input(PRESS_ENTER)

    def display_tournament_info_table(self, tournament_info):
        """
        Display detailed tournament information in a tabulated format.

        Parameters:
            tournament_info (dict): A dictionary containing tournament details.
        """
        Utils.clear()
        # Display general tournament info
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

        # Display info for each round
        tours = tournament_info.get("Tours", [])
        for tour in tours:
            print("\nTour n°", tour.get("Tour"))
            # Convert timestamps to readable dates
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

            # Display matches for this round
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
        """
        Request a description for a tournament.

        Parameters:
            name (str): The name of the tournament.

        Returns:
            str: The entered description.
        """
        Utils.clear()
        print("*"*10 + "Description" + "*"*10 + "\n")
        contents_description = input(f"Veuillez saisir une description pour le tournoi ({name}): ")
        return contents_description

    def choose_player_to_remove(self, datas):
        """
        Prompt the user to select a player from a displayed list.

        Parameters:
            datas (list): A list of players from tournament.

        Returns:
            int: The index of the selected player.
        """
        while True:
            try:
                user_input = int(
                    input(
                        "\nSelectionner l'index du jouer à retirer: "
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

    @display_message
    def display_unknow_choice_message(self):
        """
        Display a message when the user enters an unknown choice
        """
        print("\nChoix inconnue.")

    @display_message
    def display_end_tournament_message(self):
        """
        Display a message when the tournament is over.
        """
        print("\nTournoi terminé.")

    @display_message
    def display_not_tournament_selected_message(self):
        """
        Display a message when no tournament is selected.
        """
        print("\nPas de tournoi sélectionner")

    @display_message
    def display_empty_player_database_message(self):
        """
        Display a message when the player database is empty.
        """
        print("\nPas de joueur dans la base de donnée")

    @display_message
    def display_empty_tournament_database_message(self):
        """
        Display a message when the tournament database is empty.
        """
        print("\nAucun tournoi disponible.")

    @display_message
    def display_request_start_tournament_message(self):
        """
        Display a message requesting the user to start the tournament.
        """
        print("\nVeuillez commencer un tournoi.")

    @display_message
    def display_id_chess_not_find_message(self, chess_id):
        """
        Displays a message when a chess player with a specific ID
        is not found.

        Args:
            chess_id (str): The chess player ID that was not found
        """
        print(f"\nLe joueur avecl'ID: {chess_id} n'as pas été trouvé.")

    @display_message
    def display_impossible_to_remove_player_message(self):
        """
        Display a message when it is impossible to remove a player
        registered in a tournament.
        """
        print(
            "Impossibilité de supprimer un joueur inscrit dans un tournoi"
            )

    @display_message
    def display_start_round_message(self, round_name):
        """
        Display a message when starting a new round.

        Args:
            round_name (str): The name of the round.
        """
        print(f"Début du {round_name}")

    @display_message
    def display_matchs_pairs_already_load_message(self):
        """
        Display a message when the previous match pairs
        have already been loaded.
        """
        print("Les précédentes paires de matchs on déjas été chargé.")

    @display_message
    def display_matchs_pairs_properly_loaded_message(self, round_name):
        """
        Displays a message indicating that the previous match pairs
        have been properly loaded.

        Args:
            round_name (str): The name of the round.
        """
        print(f"Les précédentes paire de match\n{round_name} terminé")

    @display_message
    def request_select_or_create_tournament(self):
        """Prompts the user to select or create a new tournament."""
        print("Veuillez sélectionner ou créer un nouveau tournoi")

    @display_message
    def display_tournament_deleted_message(self, tournament_name):
        """
        Display a message when a tournament is deleted.

        Args:
            tournament_name (str): The name of the deleted tournament.
        """
        print(f"Le tournoi: {tournament_name}, à été supprimé.")

    @display_message
    def prompt_add_player_tournament(self, number_player):
        """
        Prompts the user to add a specific number of players to a tournament.

        Args:
            number_player (int): The number of players to add.
        """
        print(f"Veuillez ajouter {number_player} joueurs")

    @display_message
    def prompt_retrieve_player_tournament(self, number_player):
        """
        Prompts the user to remove a specific number of players from a tournament.

        Args:
            number_player (int): The number of players to remove.
        """
        print(f"Veuillez retirer {number_player} joueurs")

    @display_message
    def display_number_of_player_full_message(self):
        """
        Display a message when the tournament has the required number of players.
        """
        print("tournoi ayant le nombre de joueur requis")

    @display_message
    def display_player_tournament_empty_message(self):
        """
        Display a message when there are no players in the tournament.
        """
        print("Pas de joueur dans la liste du tournoi.")

    @display_message
    def prompt_correct_format(self):
        """
        Display a message prompting the user to enter the correct format.
        """
        print("Veuillez entrer un bon format.")

    @staticmethod
    def display_wrond_date_format_message():
        """
        Display a message when the date format is incorrect.
        """
        print("\nVeuillez entrer un bon format de date valide.")

    def display_alphabetical_sorted_players_message(self):
        """
        Display a message when the players are sorted alphabetically.
        """
        print("Liste des joueurs par ordre alphabétique.")

    def display_tournaments_list_message(self):
        """
        Display a message when the list of tournaments is displayed.
        """
        print("Liste des tournois.")

    def display_player_list_message(self):
        """Display a message when the list of players is displayed."""
        print("Liste des joueurs de la base de donnée")

    def display_player_add_list_message(self):
        """Display a message when the list of players added is displayed."""
        print("liste des joueurs ajoutés.")

    def display_player_update_message(self, chess_id):
        """
        Display a message when a player is correctly updated.

        Args:
            chess_id (str): The chess player ID that was updated.
        """
        print(f"\nLe joueur avec l'ID: {chess_id} a été correctement modifié.")

    def display_player_deleted_message(self, chess_id):
        """
        Display a message when a player is correctly deleted

        Args:
            chess_id (str): The chess player ID that was deleted.
        """
        print(f"\nLe joueur avec l'ID: {chess_id} a été correctement supprimé.")

    def display_player_tournament_list_message(self):
        """
        Display a message when the list of players in the tournament is displayed.
        """
        print("Liste des joueurs du tournoi")

    def display_alphabetical_sorted_players_tournament_message(self):
        """
        Display a message when the players in the tournament are sorted alphabetically.
        """
        print("Liste des joueurs du tournoi par ordre alphabétique.")

    def display_farewell_message(self):
        """Display a farewell message when the user exits the program."""
        print("Merci et à bientôt.")

    @staticmethod
    def dispalay_id_already_exists_message():
        """Displays a message when the identifier already exists."""
        print("\nIdentifiant existe déjà.")
        input(PRESS_ENTER)

    @staticmethod
    def display_id_invalid_message():
        """Displays a message when the identifier is invalid."""
        print("\nIdentifiant est invalide.")
        input(PRESS_ENTER)
