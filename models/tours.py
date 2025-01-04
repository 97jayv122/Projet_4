import random
import time
from models.tournament import Tournament
class Tours:
    def __init__(self, list_player_of_tournament):
        self.list_player_of_tournament = list_player_of_tournament
        self.time_start = time()
        self.time_end = time()
        self.group_by_two = []
        self.match_list_by_round = []

    

    def make_first_tour(self):
        random.shuffle(self.list_player_of_tournament)
        self.group_by_two = [[self.list_player_of_tournament[i], 
                              self.list_player_of_tournament[i + 1]]
                              for i in range(0, len(self.list_player_of_tournament) - 1, 2)]
        if len(self.list_player_of_tournament) % 2 == 0 :
            self.group_by_two.append([self.list_player_of_tournament[-1], "Sans adversaire"])
        return self.group_by_two
        
    def add_a_round(self):
        pass