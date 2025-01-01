import os
from models import Players, FOLDER
from view import View

class Controller:

    def make_folder_data(self):
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)

    def __init__(self, view):
        self.view = view
        self.make_folder_data()

    def run(self):
        while True:
            action = self.view.home_menu()
            match action:
                case "1":
                    number_player_add = self.view.number_add_player()
                    for i in range (1, number_player_add + 1):
                        info_player = self.view.request_add_player()
                        player = Players.from_dict(info_player) 

                case "2":                   
                    self.view.display_player(Players.list_of_player)
                    player.save_player()
                    
                case "x":
                    break

                case _:
                    print("Choix inconnue.")


