import datetime
import re 
import os
<<<<<<< HEAD
from models.models import Players, Tournament
from view.view import View

class ControllerTournament:
    def __init__(self, view):
        self.view = view
    
    def run(self):
        while True:
            action = self.view.tournament_menu()
            match action:
                case "1":
                    info_tournament = self.view.request_create_tournament()
                    tournament = Tournament.from_dict(info_tournament)
                    tournament.player_recovery()
                case "2":                   
                    pass
=======
from models.models import Players
from view.view import View

class ControllerPlayer:
    def __init__(self, view):
        self.view = view
        player = Players.load_data_player()

    def valide_date(date, date_format="%d/%m/%y"):
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False

    def valide_national_chess_identifier(identifier):
        pattern = r"^[A-Z]{2}[0-9]{5}$"
        return bool(re.match(pattern, identifier))
    
    def run(self):
        while True:
            action = self.view.player_menu()
            match action:
                case "1":
                    number_player_add = self.view.number_add_player()
                    for i in range (1, number_player_add + 1):
                        info_player = self.view.request_add_player()
                        player = Players.from_dict(info_player)
                        if self.valide_date(player.date_of_birth) and self.valide_national_chess_identifier(player.national_chess_identifier):
                            pass
                        else:
                            le f
                    player.save_player()
                        

                case "2":                   
                    self.view.display_player(Players.list_of_player)
>>>>>>> c2ce1e66595171b76cc82fe7ea370da7f47edc92
                    
                case "x":
                    break

                case _:
                    print("Choix inconnue.")


