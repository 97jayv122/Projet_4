
import json
import uuid
from datetime import datetime
FILE_PLAYER = "data/tournaments/players.json"


class Players:

    def __init__(self, first_name, name, date_of_birth, national_chess_identifier, player_id=None):
        """
        Initialise un joueur. Si `player_id` est fourni, il est utilisé, sinon un nouvel ID est généré.
        """
        self.first_name = first_name
        self.name = name
        self.date_of_birth = date_of_birth
        self.national_chess_identifier = national_chess_identifier
        self.id = player_id if player_id else str(uuid.uuid4())  # Préserve l'ID existant si fourni
        self.create_at = datetime.now().isoformat()
        self.update_at = ""

    def __repr__(self):
        return str(self.first_name) + "." + str(
            self.name
            )

    def to_dict(self):
        return self.__dict__


    def save(self):

        players = Players.load()
        players.append(self)

        with open(FILE_PLAYER, "w") as file:
            json.dump(
                [player.to_dict() for player in players],
                  file, indent=4
                )

    @staticmethod
    def save_all(players):

        with open(FILE_PLAYER, "w") as file:
            json.dump(
                [player.to_dict() for player in players],
                  file, indent=4
                )
        

    @staticmethod
    def load():
        try:
            with open(FILE_PLAYER, "r") as file:
                data = json.load(file)
                return [Players.restore_from_json(player) for player in data]
        except json.JSONDecodeError:
            print("pas de données a charger")
        except FileNotFoundError:
            print("pas de fichier a charger")
        return []
    
    @classmethod
    def restore_from_json(cls, data):
        """_summary_

        Args:
            data (_type_): _description_
        """
        player = cls(
            first_name=data.get("first_name"),
            name=data.get("name"),
            date_of_birth=data.get("date_of_birth"),
            national_chess_identifier=data.get("national_chess_identifier"),
            player_id=data.get("id")  # Restaurer l'ID existant
        )
        # Restauration des dates de création et modification
        player.create_at = data.get("create_at", player.create_at)
        player.update_at = data.get("update_at", player.update_at)
        return player
                

    def update(self, **new_values):
        allowed_keys = ["first_name", "name", "date_of_birth"]
        for key, value in new_values.items():
            if key in allowed_keys:
                setattr(self, key, value)
        self.update_at = datetime.now().isoformat()

    @staticmethod
    def load_info_players_by_id(*id):
        info_player = []
        players = Players.load()
        for player in players:
            if player.id in id:
                info_player.append(player)
        return info_player
    

# id = [
#     "28a1c764-66a5-4ba4-a122-3d85242fb088",
#     "dbf7d6fd-ab9c-4a2d-950a-96730b63bad7",
#     "2cb53db1-6ff2-4202-9feb-0ff677b03f4f",
#     "ebc62e3a-1d72-4f17-b282-e3e0111f25a2"
#     ]

# print(Players.load_info_players_by_id(*id))