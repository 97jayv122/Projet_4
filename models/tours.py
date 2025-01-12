import random
import time
from models.matchs import Matchs


class Tours:
    list_of_tours = []

    def __init__(self, list_player_of_tournament):
        self.list_player_of_tournament = list_player_of_tournament
        self.duration = 0
        self.time_start = None
        self.time_end = None
        self.group_by_two = []
        self.matchs_list_by_round = []
        self.stat = "not started"
        Tours.list_of_tours.append(self)

    def to_dict(self):
        return {
            "list_player_of_tournament": self.list_player_of_tournament,
            "duration": self.duration,
            "time_start": self.time_start,
            "time_end": self.time_end,
            "group_by_two": self.group_by_two,
            "match_list_by_round": [
                match.to_dict() if isinstance(match, Matchs)
                else match for match in self.matchs_list_by_round
                ],
            "stat": self.stat}

    def make_first_tour(self):
        random.shuffle(self.list_player_of_tournament)
        self.group_by_two = [[
            self.list_player_of_tournament[i],
            self.list_player_of_tournament[i + 1]
            ]
            for i in range(0, len(self.list_player_of_tournament) - 1, 2)
            ]
        if len(self.list_player_of_tournament) % 2 == 0:
            self.group_by_two.append([
                self.list_player_of_tournament[-1], "Sans adversaire"
                ])
        return self.group_by_two

    def start_tour(self):
        self.time_start = time.time()
        self.etat = "started"

    def end_tour(self):
        self.time_end = time.time()
        self.duration = self.time_end - self.time_start
        self.etat = "finished"
        self.duration = self.time_end - self.time_start

    def make_next_tour(self):
        pass

    def add_a_round(self):
        pass

    def recovery_list_of_matchs(self, matchs):
        list_matchs = list(matchs.__dict__.items())
        self.match_list_by_round.append(list_matchs)
