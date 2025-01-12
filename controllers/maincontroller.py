import os
from models.players import FOLDER
from view.utils import Utils
from controllers.controllerplayer import ControllerPlayer
from controllers.controllertournament import ControllerTournament


class Controller:
    """
    Main controller of the application that allows 
    to navigate between the different menus.
    """

    # Définition des numéros d'action comme variables de classe
    PLAYER_MENU = "1"
    TOURNAMENT_MENU = "2"
    EXIT_MENU = "x"

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
            action = self.view.home_menu()
            match action:
                case self.PLAYER_MENU:
                    Utils.clear()
                    self.run_controller_player()

                case self.TOURNAMENT_MENU:
                    Utils.clear()
                    self.run_controller_tournament()

                case "3":
                    pass

                case self.EXIT_MENU:
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