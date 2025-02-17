import random
import time
from models.matchs import Matchs


class Tours:

    def __init__(self, tour_number):
        self.tour_number = tour_number
        self.duration = 0
        self.time_start = None
        self.time_end = None
        self.matchs = []
        self.stat = "not started"

    @classmethod
    def from_dict(cls, data):
        """
        Restaure un objet Tours depuis un dictionnaire.
        """
        tour = cls(data["tour_number"])
        tour.time_start = data["time_start"]
        tour.time_end = data["time_end"]
        Tours.matchs = [
            Matchs.from_dict(match) for match in data["matchs"]
        ]
        tour.stat = data["stat"]
        return tour
    
    def to_dict(self):
        return {
            "tour_name" : self.tour_number,
            "duration": self.duration,
            "time_start": self.time_start,
            "time_end": self.time_end,
            "matchs_list_by_round": [
                match.to_dict() if isinstance(match, Matchs)
                else match for match in self.matchs
                ],
            "stat": self.stat}

    def start(self):
        """
        Starts the tour by recording the current time as the start time and updating
        the status to "started".
        """
        self.time_start = time.time()
        self.stat = "started"

    def end(self):
        """
        Ends the tour by recording the current time as the end time, calculating the duration
        and updating the status to "finished".
        """
        self.time_end = time.time()
        self.duration = self.time_end - self.time_start
        self.stat = "finished"
        self.duration = self.time_end - self.time_start

    def rename_as_round(self):
        """
        Renames this tour instance by updating its tour_number attribute to a string in the format "Round X".

        Example:
            If tour_number is 1, after calling this method it will become "Round 1".
        """
        self.tour_number = f"Round {self.tour_number}"

    def __repr__(self):
        """
        Returns an official string representation of the Tours object.
        """
        return f"<Tours: {self.tour_number}, status: {self.stat}>"

    

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

