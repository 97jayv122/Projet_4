import os
from models.tournament import FOLDER_TOURNAMENT
from controllers.controllerplayer import ControllerPlayer
from controllers.tournamentmanagement import TournamentManagement
from controllers.controllerreport import ControllerReport


class Constant:
    """
    Constants representing the main menu options.
    """
    PLAYER_MENU = "1"
    TOURNAMENT_MENU = "2"
    DISPLAY_REPORTS = "3"
    EXIT_PROGRAM = "x"


class Controller:
    """
    Main controller of the application.

    Facilitates navigation between different menus such as the player,
    tournament, and reports menus.
    """

    def make_folder_data(self):
        """
        Create the data folder if it does not exist.
        """
        if not os.path.exists(FOLDER_TOURNAMENT):
            os.makedirs(FOLDER_TOURNAMENT)

    def __init__(self, view):
        """
        Initialize the main controller with the given view.

        Parameters:
            view: The view instance used for user interactions.
        """
        self.view = view
        self.make_folder_data()

    def run(self):
        """
        Main method of the controller that displays the home menu and
        navigates to the selected sub-menu.
        """
        while True:
            action = self.view.home_menu()
            match action:
                case Constant.PLAYER_MENU:
                    self.run_controller_player()

                case Constant.TOURNAMENT_MENU:
                    self.run_tournament_management()

                case Constant.DISPLAY_REPORTS:
                    self.run_controller_report()

                case Constant.EXIT_PROGRAM:
                    self.exit_program()

                case _:
                    self.unknown_choice

    def run_controller_player(self):
        """
        Run the player controller.
        """
        controllerplayer = ControllerPlayer(self.view)
        controllerplayer.run()

    def run_tournament_management(self):
        """
        Run the tournamment management controller.
        """
        tounamentmanagement = TournamentManagement(self.view)
        tounamentmanagement.run()

    def run_controller_report(self):
        """
        Run the reports controller.
        """
        controllerreport = ControllerReport(self.view)
        controllerreport.run()

    def exit_program(self):
        """
        Exit the program.
        """
        print("Merci et à bientôt.")
        exit()

    def unknown_choice(self):
        """
        Display a message when the choice is unknown.
        """
        self.view.display_string("Choix inconnue.")
