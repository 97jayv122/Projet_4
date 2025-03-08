from models.players import Players
from controllers.controllertournament import ControllerTournament
from models.tournament import Tournaments


class ConstantTournamentManagement:
    """
    Constants representing tournament management menu options.
    """
    CREATE_A_TOURNAMENT = "1"
    SELECT_PLAYER = "2"
    DELETE_PLAYER = "3"
    START_TOURNAMENT = "4"
    DELETE_TOURNAMENT = "5"
    ADD_DESCRIPTION = "6"
    RETURN_MAIN_MENU = "x"


class TournamentManagement:
    """
    Controller for managing tournaments.

    Handles creation of tournaments, player selection for a tournament,
    deleting players or tournaments, starting tournaments, and adding descriptions.
    """
    def __init__(self, view):
        """
        Initialize the tournament management controller.

        Parameters:
            view: The view instance for user interactions.
        """
        self.view = view
        tournaments = Tournaments.load()
        self.tournaments = tournaments
        self.tournament = None
        self.players = Players.load()

    def run(self):
        """
        Run the tournament management loop.

        Processes user actions for creating, selecting, modifying, and deleting tournaments.
        """
        while True:
            action = self.view.tournamament_management_menu()
            # Reload tournaments to get the latest data
            self.tournaments = Tournaments.load()
            match action:
                case ConstantTournamentManagement.CREATE_A_TOURNAMENT:
                    self.create_tournament()

                case ConstantTournamentManagement.SELECT_PLAYER:
                    self.select_tournament()
                    self.player_selection()

                case ConstantTournamentManagement.DELETE_PLAYER:
                    self.select_tournament()
                    self.remove_player_from_tournament()

                case ConstantTournamentManagement.START_TOURNAMENT:
                    self.select_tournament()
                    self.run_controller_tournament()

                case ConstantTournamentManagement.DELETE_TOURNAMENT:
                    self.select_tournament()
                    names_tournaments = self.get_tournament_name()
                    if names_tournaments is not None:
                        index = self.view.select_tournament(names_tournaments)
                        del self.tournaments[index - 1]
                        Tournaments.save_all(self.tournaments)
                    else:
                        return

                case ConstantTournamentManagement.ADD_DESCRIPTION:
                    self.select_tournament()
                    self.make_description()

                case ConstantTournamentManagement.RETURN_MAIN_MENU:
                    break

                case _:
                    self.view.display_unknow_choice_message()

    def get_tournament_name(self):
        """
        Retrieve tournament names and player counts for display.

        Returns:
            list: A list of dictionaries with tournament name and number of players,
                  or None if no tournaments exist.
        """
        if len(self.tournaments) > 1:
            return [
                {
                    "Nom du tournoi": tournament.name,
                    "Nombre de joueur": len(tournament.list_player),
                }
                for tournament in self.tournaments
            ]
        elif len(self.tournaments) == 1:
            return [
                {
                    "Nom du tournoi": self.tournaments[0].name,
                    "Nombre de joueur": len(self.tournaments[0].list_player),
                }
            ]
        else:
            self.view.display_empty_tournament_database_message()
            return None

    def create_tournament(self):
        """
        Create a new tournament.

        Requests tournament information from the view, creates a tournament instance,
        saves it, and then prompts for player selection.
        """
        info_tournament = self.view.request_create_tournament()
        tournament = Tournaments.from_dict(info_tournament)
        tournament.save()
        self.tournament = tournament
        self.player_selection()

    def select_tournament(self):
        """
        Allow the user to select a tournament from the list.
        """
        names_tournaments = self.get_tournament_name()
        if names_tournaments is not None:
            self.view.display_table(names_tournaments)
            index = self.view.select_tournament(names_tournaments)
            self.tournament = self.tournaments[index - 1]
            self.tournament.list_player = Players.load_by_ids(
                *self.tournament.list_player
            )
        else:
            self.view.display_empty_tournament_database_message()

    def player_selection(self):
        """
        Add players to the selected tournament.

        Displays the list of available players and prompts the user to select players
        to add to the tournament, until the required number is met.
        """
        if self.tournament is not None:
            if self.players:
                if len(self.tournament.list_player) < self.tournament.number_player:
                    data_players = [player.to_dict() for player in self.players]
                    self.view.display_table(data_players)
                    self.view.display_player_list_message()
                    try:
                        index_players = self.view.select_player()
                        for index in index_players:
                            self.tournament.add_player_score(self.players[int(index) - 1])
                    except ValueError:
                        self.view.prompt_correct_format()
                    self.tournament.update(self.tournament.id)
                else:
                    self.view.display_number_of_player_full_message()
            else:
                self.view.display_empty_player_database_message()
        else:
            self.view.display_not_tournament_selected_message()

    def check_player_number(self):
        """
        Check if the number of players in the tournament matches the required number.

        Returns:
            bool: True if the tournament has the required number of players, False otherwise.
        """
        tournament = self.tournament
        if len(tournament.list_player) == tournament.number_player:
            return True

        elif len(tournament.list_player) < tournament.number_player:
            missing = tournament.number_player - len(tournament.list_player)
            self.view.prompt_add_player_tournament(missing)
            return False

        elif len(tournament.list_player) > tournament.number_player:
            extra = len(tournament.list_player) - tournament.number_player
            self.view.prompt_retrieve_player_tournament(extra)
            return False
        else:
            return False

    def remove_player_from_tournament(self):
        """
        Remove a player from the selected tournament.
        """
        if self.tournament is not None:
            if self.tournament.list_player:
                players = [
                    [player.first_name, player.last_name]
                    for player in self.tournament.list_player
                ]
                self.view.display_table(players)
                self.view.display_player_tournament_list_message()
                user_input = self.view.choose_player_to_remove(players)
                self.tournament.list_player.pop(user_input - 1)
                self.tournament.update(self.tournament.id)
            else:
                self.view.display_player_tournament_empty_message()

        else:
            self.view.display_not_tournament_selected_message()

    def run_controller_tournament(self):
        """
        Start the tournament by running its controller if the player number is correct.
        """
        if self.tournament is not None:
            if self.check_player_number():
                controllertournament = ControllerTournament(self.view, self.tournament)
                controllertournament.run()
        else:
            self.view.request_select_or_create_tournament()

    def delete_tournament(self, index):
        """
        Delete a tournament instance.

        Parameters:
            index (int): The index of the tournament to delete.
        """
        self.view.display_tournament_deleted_message(self.tournament.name)
        self.tournament = None
        # display_tournament_deleted_message = self.tournaments.pop(index)

    def make_description(self):
        """
        Add a description to the selected tournament.

        Prompts the user for a description and updates the tournament.
        """
        data_entered = self.view.request_enter_description(self.tournament.name)
        self.tournament.add_description(data_entered)
        self.tournament.update(self.tournament.id)
