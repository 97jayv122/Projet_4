from models.players import Players
from models.tournament import Tournaments


class ConstantPlayer:
    """
    A class to hold constant options for player management menu and
    player modification options.

    """
    ADD_PLAYER = "1"
    DISPLAY_PLAYER = "2"
    MODIFY_PLAYER = "3"
    SUPPRESS_PLAYER = "4"
    RETURN_MAIN_MENU = "x"
    MODIFY_PLAYER_ID = "modifier"
    DELETE_PLAYER_ID = "supprimer"


class ControllerPlayer:
    """
    Controller for the player menu.
    Provides functionalities to add, display, modify, and delete players.
    """

    def __init__(self, view):
        """
        Initialize the player controller with the given view.

        Parameters:
            view: The view instance for user interactions.
        """
        self.view = view
        self.players = Players.load()

    def run(self):
        """
        Run the player management loop.

        Displays the player menu and processes user actions.
        """
        while True:
            # Reload players to ensure the latest data is used.
            self.players = Players.load()
            action = self.view.player_menu()
            match action:
                case ConstantPlayer.ADD_PLAYER:
                    self.add_player()

                case ConstantPlayer.DISPLAY_PLAYER:
                    self.display_player()
                    self.view.press_enter()

                case ConstantPlayer.MODIFY_PLAYER:
                    self.modify_player()

                case ConstantPlayer.SUPPRESS_PLAYER:
                    self.suppress_player()

                case ConstantPlayer.RETURN_MAIN_MENU:
                    break

                case _:
                    self.view.display_unknow_choice_message()

    def add_player(self):
        """
        Add one or multiple players to the database.

        The method prompts the user for the number of players to add, then requests
        player details for each new player. After creation, it displays the list of
        newly added players.
        """
        number_player_add = self.view.number_add_player()
        if number_player_add == 0:
            # If no players are to be added, break or handle accordingly.
            return
        for i in range(1, number_player_add + 1):
            input_player = self.view.request_add_player()
            player = Players.from_dict(input_player)
            player.save()
        self.display_new_player(number_player_add)
        self.view.display_player_add_list_message()
        self.view.press_enter()

    def modify_player(self):
        """
        Modify an existing player's information.

        Displays the list of players, then prompts the user for the chess identifier
        of the player to modify. If found, requests new player details and updates the
        player's record.
        """
        self.display_player()
        if self.players:
            chess_id = self.view.request_player_id(ConstantPlayer.MODIFY_PLAYER_ID)
            if chess_id:
                player = self.load_by_id(chess_id)
                if player:

                    data = self.view.request_modify_player()
                    player.update(**data)
                    Players.save_all(self.players)
                    self.display_player()
                    self.view.display_player_update_message(chess_id)
                    self.view.press_enter()

                else:
                    self.view.display_id_chess_not_find_message(chess_id)
            else:
                self.view.display_id_chess_not_find_message(chess_id)
        else:
            self.view.display_empty_player_database_message()

    def suppress_player(self):
        """
        Delete a player from the database.

        Displays the list of players, then prompts the user for the chess identifier
        of the player to delete. If the player exists and is not registered in any tournament,
        removes the player from the database.
        """
        self.display_player()
        if self.players:
            chess_id = self.view.request_player_id(ConstantPlayer.DELETE_PLAYER_ID)
            if chess_id:
                player = self.load_by_id(chess_id)

                if player is not None:
                    if not self.check_player_in_tournament(player.id):

                        self.players.remove(player)
                        Players.save_all(self.players)
                        self.display_player()
                        self.view.display_player_deleted_message(chess_id)
                        self.view.press_enter()
                    else:
                        self.display_impossible_to_remove_player_message()
                else:
                    self.view.display_id_chess_not_find_message(chess_id)
                    self.display_player()
                    self.view.press_enter()
            else:
                self.view.display_id_chess_not_find_message(chess_id)
        else:
            self.view.display_empty_player_database_message()

    def display_player(self):
        """
        Display the list of players.

        If players exist, formats their data as a table and displays it. Otherwise,
        shows a message indicating no players are available.

        Parameters:
            prompt (str, optional): A prompt message to display with the table.
        """
        if self.players:
            players_dict = [player.to_dict() for player in self.players]
            self.view.display_table(players_dict)
        else:
            self.view.display_empty_player_database_message()

    def load_by_id(self, chess_id):
        """
        Retrieve a player from the loaded players based on their chess identifier.

        Parameters:
            chess_id (str): The chess identifier of the player to load.

        Returns:
            The player object if found; otherwise, None.
        """
        for player in self.players:
            if player.national_chess_identifier == chess_id:
                return player
        return None

    def display_new_player(self, number=1):
        """
        Display the newly added players.

        Parameters:
            number (int, optional): The number of players added. Defaults to 1.
            prompt (str, optional): A prompt message to display with the table.
        """
        self.players = Players.load()
        if self.players:
            new_players = self.players[-number:]
            new_players_sorted = sorted(
                new_players, key=lambda x: (x.last_name, x.first_name)
            )
            players_dict = [player.to_dict() for player in new_players_sorted]
            self.view.display_table(players_dict)
        else:
            self.view.display_empty_player_database_message()

    def check_player_in_tournament(self, player_id):
        """
        Check whether a player is registered in any tournament.

        Parameters:
            player_id: The unique ID of the player.

        Returns:
            bool: True if the player is registered in a tournament; otherwise, False.
        """
        tournaments = Tournaments.load()
        for tournament in tournaments:
            for player in tournament.list_player:

                if player == player_id:
                    return True
        return False
