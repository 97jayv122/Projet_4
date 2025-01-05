import random
import time

class Tours:
    def __init__(self, list_player_of_tournament):
        self.list_player_of_tournament = list_player_of_tournament
        self.duration = 0
        self.time_start = None
        self.time_end = None
        self.group_by_two = []
        self.match_list_by_round = []
        self.etat = "not started"
    

    def make_first_tour(self):
        random.shuffle(self.list_player_of_tournament)
        self.group_by_two = [[self.list_player_of_tournament[i], 
                              self.list_player_of_tournament[i + 1]]
                              for i in range(0, len(self.list_player_of_tournament) - 1, 2)]
        if len(self.list_player_of_tournament) % 2 == 0 :
            self.group_by_two.append([self.list_player_of_tournament[-1], "Sans adversaire"])
        return self.group_by_two
        
    def start_tour(self):
        self.time_start = time.time()
        self.etat = "started"
    
    def end_tour(self):
        self.time_end = time.time()
        self.duration = self.time_end - self.time_start
        self.etat = "finished"

    def make_next_tour(self):
        pass
    def add_a_round(self):
        pass