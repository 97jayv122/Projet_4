import random
import time
from models.matchs import Matchs


class Tours:

    def __init__(self, tour_number):
        self.tour_number = tour_number
        self.name = "round" + str(tour_number)
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
        tour.name = data["tour_name"]
        tour.time_start = data["time_start"]
        tour.time_end = data["time_end"]
        tour.matchs = [
            Matchs.from_dict(match) if isinstance(match, dict) 
            else match for match in data["matchs_list"]
        ]
        tour.stat = data["stat"]
        return tour
    
    def to_dict(self):
        return {
            "tour_number" : self.tour_number,
            "tour_name" : self.name,
            "duration": self.duration,
            "time_start": self.time_start,
            "time_end": self.time_end,
            "matchs_list": [
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
        return f"<Tours: {self.name}, durée: {self.duration}\nliste des matchs : {self.matchs}>"

