import time
from models.matchs import Matchs


class Tours:
    """
    Class representing a round (tour) in a tournament.

    Manages round details including round number, name, duration, start/end times, matches, and status.
    """
    def __init__(self, tour_number):
        """
        Initialize a new round.

        Parameters:
            tour_number (int): The round number.
        """
        self.tour_number = tour_number
        self.name = "round" + str(tour_number)
        self.duration = 0.0
        self.time_start = None
        self.time_end = None
        self.matchs = []
        self.stat = "not started"

    @classmethod
    def from_dict(cls, data):
        """
        Restore a Tours object from a dictionary.

        Parameters:
            data (dict): Dictionary containing round data.

        Returns:
            Tours: A new Tours instance populated with the provided data.
        """
        tour = cls(data["tour_number"])
        tour.name = data["tour_name"]
        tour.time_start = data["time_start"]
        tour.time_end = data["time_end"]
        tour.matchs = [
            Matchs.from_dict(match) if isinstance(match, dict) else match
            for match in data["matchs_list"]
        ]
        tour.stat = data["stat"]
        return tour

    def to_dict(self):
        """
        Convert the round instance to a dictionary.

        Returns:
            dict: Dictionary representation of the round.
        """
        return {
            "tour_number": self.tour_number,
            "tour_name": self.name,
            "duration": self.duration,
            "time_start": self.time_start,
            "time_end": self.time_end,
            "matchs_list": [
                match.to_dict() if isinstance(match, Matchs) else match
                for match in self.matchs
            ],
            "stat": self.stat,
        }

    def start(self):
        """
        Start the round.

        Records the current time as the start time and updates the status to "started".
        """
        self.time_start = time.time()
        self.stat = "started"

    def end(self):
        """
        End the round.

        Records the current time as the end time, calculates the duration,
        and updates the status to "finished".
        """
        self.time_end = time.time()
        self.duration = self.time_end - self.time_start
        self.stat = "finished"
        self.duration = self.time_end - self.time_start

    def __repr__(self):
        """
        Return a string representation of the round.

        Returns:
            str: Information about the round including its name, duration, and match list.
        """
        return f"<Tours: {self.name}, durée: {self.duration}\nliste des matchs : {self.matchs}>"
