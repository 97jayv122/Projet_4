import random
import time
from models.matchs import Matchs


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

    def recovery_list_of_matchs(self, matchs):
        """
        Ajoute une liste de matchs au tour.

        Args:
            matchs (list): Liste d'instances de la classe Matchs.
        """
        self.matchs_list_by_round = [match.to_dict() for match in matchs]

    def __repr__(self):
        pass

    @classmethod
    def recovery_list_of_tour(self):
        # list_tour = list(tour.__dict__.items())
        # self.list_of_tours.append(list_tour)
        self.list_of_tours.append(tour.to_dict() if isinstance(tour, Tours) else tour)
    