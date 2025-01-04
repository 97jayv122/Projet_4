
import json
import uuid
FOLDER = "data/tournaments"
class Players:

    list_of_player = []

    def __init__(self, first_name, name, date_of_birth,
                 national_chess_identifier):
        self.first_name = first_name
        self.name = name
        self.date_of_birth = date_of_birth
        self.national_chess_identifier = national_chess_identifier
        self.id = str(uuid.uuid4())
        Players.list_of_player.append(self)

    def __repr__(self):
        return str(self.first_name) + "." + str(self.name)
    
    def to_dict(self):
        return {"first_name":self.first_name,
                "name": self.name,
                "date_of_birth": self.date_of_birth,
                "national_chess_identifier": self.national_chess_identifier,
                "id": self.id}
    
    def save_player(self):
        with open(FOLDER + "/players.json", "w") as file:
            json.dump([player.to_dict() for player in self.list_of_player], file)

    @classmethod
    def load_data_player(cls):
        try:
            with open(FOLDER + "/players.json", "r") as file:
                data = json.load(file)
                return [Players.from_dict(player) for player in data]
        except json.JSONDecodeError:
            print("pas de données a charger")
        except FileNotFoundError:
            print("pas de fichier a charger")
        return []
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data.get("first_name"),
            name=data.get("name"),
            date_of_birth=data.get("date_of_birth"),
            national_chess_identifier=data.get("national_chess_identifier")
        )
    
