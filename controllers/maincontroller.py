import os
from models.players import FOLDER
from view.utils import Utils
from controllers.controllerplayer import ControllerPlayer
from controllers.controllertournament import ControllerTournament

class Constant:

    PLAYER_MENU = "1"
    TOURNAMENT_MENU = "2"
    DISPLAY_REPORTS = "3"
    EXIT_PROGRAM = "x"

class Controller:
    """
    Main controller of the application that allows 
    to navigate between the different menus.
    """

    # Définition des numéros d'action comme variables de classe

    def make_folder_data(self):
        """
        Create the data folder if it does not exist.
        """        
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)

    def __init__(self, view):
        """
        Constructor of the main controller.

        Args:
            view (_type_): _description_
        """        
        self.view = view
        self.make_folder_data()

    def run(self):
        """
        Main method of the main controller that allows
        the user to navigate between the different menus.
        """        
        while True:
            Utils.clear()
            action = self.view.home_menu()
            match action:
                case Constant.PLAYER_MENU:
                    self.run_controller_player()

                case Constant.TOURNAMENT_MENU:
                    self.run_controller_tournament()

                case Constant.DISPLAY_REPORTS:
                    pass

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

    def run_controller_tournament(self):
        """
        Run the tournament controller.
        """        
        controllertournament = ControllerTournament(self.view)
        controllertournament.run()

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
        print("Choix inconnue.")
        input("Appuyer sur entrée pour continuer...")