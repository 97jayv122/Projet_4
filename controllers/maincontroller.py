import re
import datetime
import os
from models.models import Players, FOLDER
from view.view import View
from controllers.controllerplayer import ControllerPlayer
from controllers.controllertournament import ControllerTournament

class Controller:

    def make_folder_data(self):
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)

    def valide_date(date, date_format="%d/%m/%y"):
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False
        
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

                case "3":
                    pass

                case "x":
                    break

                case _:
                    print("Choix inconnue.")


