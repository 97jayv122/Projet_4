import datetime
import re 
import os
from models.players import Players
from models.tournament import Tournament
from models.tours import Tours
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
                    tournament.save_tournament()
                    tournament.list_player = self.view.select_player(tournament.list_player)
                    tournament.save_tournament()

                case "2":                   
                    tours = Tours(tournament.list_player)
                    tours.make_first_tour()
                    self.view.display_tours(tours.group_by_two) 
                    
                case "x":
                    break

                case _:
                    print("Choix inconnue.")


