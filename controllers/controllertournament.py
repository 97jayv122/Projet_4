import datetime
import re 
import os
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
                    
                case "x":
                    break

                case _:
                    print("Choix inconnue.")


