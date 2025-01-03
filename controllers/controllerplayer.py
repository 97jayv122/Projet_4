import re
import os
from models.models import Players
from view.view import View

class ControllerPlayer:

    def valide_national_chess_identifier(identifier):
        pattern = r"^[A-Z]{2}[0-9]{5}$"
        return bool(re.match(pattern, identifier))
    
    def __init__(self, view):
        self.view = view

    def run(self):
        while True:
            action = self.view.player_menu()
            match action:
                case "1":
                    number_player_add = self.view.number_add_player()
                    for i in range (1, number_player_add + 1):
                        info_player = self.view.request_add_player()
                        player = Players.from_dict(info_player)                 
                    player.save_player()
                        
                case "2":                   
                    self.view.display_player(Players.list_of_player)
                    
                case "3":
                    player = Players.load_data_player()
                    
                case "x":
                    break

                case _:
                    print("Choix inconnue.")


