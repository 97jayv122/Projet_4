
import json
import uuid
from datetime import datetime
FOLDER = "data/tournaments"
FOLDER_PLAYER = FOLDER + "/players.json"

class Players:
    list_of_player = []

    def __init__(self, first_name, name, date_of_birth,
                 national_chess_identifier):
        self.first_name = first_name
        self.name = name
        self.date_of_birth = date_of_birth
        self.national_chess_identifier = national_chess_identifier
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now().isoformat()
        self.update_at = ""
        Players.list_of_player.append(self)

    def __repr__(self):
        return str(self.first_name) + "." + str(
            self.name
            ) + " chess ID : " + str(self.national_chess_identifier)

    def to_dict(self):
        return {"first_name": self.first_name,
                "name": self.name,
                "date_of_birth": self.date_of_birth,
                "national_chess_identifier": self.national_chess_identifier,
                "id": self.id,
                "create_at": self.create_at,
                "update_at": self.update_at
                }

    @classmethod
    def instances_save(self):
        with open(FOLDER_PLAYER, "w") as file:
            json.dump(
                [player.to_dict() for player in self.list_of_player], file
                )

    @staticmethod
    def load_file():
        try:
            with open(FOLDER_PLAYER, "r") as file:
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            print("pas de données a charger")
        except FileNotFoundError:
            print("pas de fichier a charger")
        return []

    @classmethod
    def instances_load(cls):
        data = Players.load_file()
        return [Players.from_dict(player) for player in data]

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data.get("first_name"),
            name=data.get("name"),
            date_of_birth=data.get("date_of_birth"),
            national_chess_identifier=data.get("national_chess_identifier")
        )

    def update(self, **new_values):
        allowed_keys = ["first_name", "name", "date_of_birth"]
        for key, value in new_values.items():
            if key in allowed_keys:
                setattr(self, key, value)
        self.update_at = datetime.now().isoformat()

    def delete(self):
        Players.list_of_player.remove(self)

    @classmethod
    def get_player_by_id(cls, chess_id):
        for player in cls.list_of_player:
            if player.national_chess_identifier == chess_id:
                return player
        return None

            
    @classmethod
    def clear_instances(cls):
        cls.list_of_player = []

