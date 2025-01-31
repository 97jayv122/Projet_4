import random
import time
from matchs import Matchs


class Tours:


    def __init__(self, list_player_of_tournament):
        self.list_player_of_tournament = list_player_of_tournament
        self.duration = 0
        self.time_start = None
        self.time_end = None
        self.matchs_list_by_round = []
        self.stat = "not started"

    @classmethod
    def from_dict(cls, data):
        """
        Restaure un objet Tours depuis un dictionnaire.
        """
        tour = cls(data["list_player_of_tournament"])
        tour.time_start = data["time_start"]
        tour.time_end = data["time_end"]
        tour.matchs_list_by_round = [
            Matchs.from_dict(match) for match in data["matchs_list_by_round"]
        ]
        tour.stat = data["stat"]
        return tour
    
    def to_dict(self):
        return {
            "list_player_of_tournament": self.list_player_of_tournament,
            "duration": self.duration,
            "time_start": self.time_start,
            "time_end": self.time_end,
            "matchs_list_by_round": [
                match.to_dict() if isinstance(match, Matchs)
                else match for match in self.matchs_list_by_round
                ],
            "stat": self.stat}

    def start(self):
        self.time_start = time.time()
        self.stat = "started"

    def end(self):
        self.time_end = time.time()
        self.duration = self.time_end - self.time_start
        self.stat = "finished"
        self.duration = self.time_end - self.time_start

    def __repr__(self):
        pass

    

# round1 = Tours(["jay", "kérinah", "némi", "léti"])
# round1.start()
# round1.end()
# print(round1.duration)
# data = round1.to_dict()
# print(data)
# round2 = Tours.from_dict(data)
# print(round2.to_dict())
# round1.recovery_list_of_matchs()
# print(round1.matchs_list_by_round)

