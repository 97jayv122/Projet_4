import re
<<<<<<< HEAD
import datetime
=======
>>>>>>> c2ce1e66595171b76cc82fe7ea370da7f47edc92
import os
from models.models import Players, FOLDER
from view.view import View
from controllers.controllerplayer import ControllerPlayer
from controllers.controllertournament import ControllerTournament
<<<<<<< HEAD

=======
>>>>>>> c2ce1e66595171b76cc82fe7ea370da7f47edc92
class Controller:

    def make_folder_data(self):
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)
<<<<<<< HEAD

    def valide_date(date, date_format="%d/%m/%y"):
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False
=======
>>>>>>> c2ce1e66595171b76cc82fe7ea370da7f47edc92
        
    def __init__(self, view):
        self.view = view
        self.make_folder_data()

    def run(self):
        while True:
            action = self.view.home_menu()
            match action:
                case "1":
                    controllerplayer = ControllerPlayer(self.view)
                    controllerplayer.run()
                    
                case "2":                   
                    controllertournament = ControllerTournament(self.view)
                    controllertournament.run()

<<<<<<< HEAD
                case "3":
                    pass

=======
>>>>>>> c2ce1e66595171b76cc82fe7ea370da7f47edc92
                case "x":
                    break

                case _:
                    print("Choix inconnue.")


