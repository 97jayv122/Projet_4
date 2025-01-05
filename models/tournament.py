import json
from models.players import Players
from models.tours import Tours
class Tournament:
    def __init__(self, name, place, date_start, date_end,
                 number_of_turns=4, **kwargs):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.number_of_turns = number_of_turns
        self.list_player = kwargs.get("list_player", [])
        self.list_of_tours = kwargs.get("list_of_tours", [])
        self.current_tour = kwargs.get("current_tour", 0)
        self.description = kwargs.get("description", "")

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            place=data.get("place"),
            date_start=data.get("date_start"),
            date_end=data.get("date_end"),
            list_player=data.get("list_player"),
            list_of_tours=data.get("list_of_tours"),
            current_tour=data.get("current_tour"),
            description=data.get("description")
        )

    def to_dict(self):
        return {"name": self.name,
                "place": self.place,
                "date_start": self.date_start,
                "date_end": self.date_end,
                "number_of_turns": self.number_of_turns,
                "list_player": [player.to_dict() for player in self.list_player],
                "list_of_tours": [tour.to_dict() for tour in self.list_of_tours],
                "current_tour": self.current_tour,
                "description": self.description}
    
    def save_tournament(self):
        with open("data/tournaments/tournament.json", "w") as file:
            json.dump(self.to_dict(), file)
    @classmethod
    def load_tournament(cls):
        try:
            with open("data/tournaments/tournament.json", "r") as file:
                data = json.load(file)
                return Tournament.from_dict(data)
        except json.JSONDecodeError:
            print("pas de données a charger")
        except FileNotFoundError:
            print("pas de fichier a charger")
        return None
        