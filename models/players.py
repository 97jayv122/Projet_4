
import json
import uuid
from datetime import datetime
FOLDER_PLAYER = "data/players.json"


class Players:
    list_of_player = []

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
        Players.list_of_player.append(self)

    def __repr__(self):
        return str(self.first_name) + "." + str(
            self.name
            ) + " ID : " + str(self.id)

    def to_dict(self):
        return self.__dict__

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
        return [cls.restore_from_json(player) for player in data]

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data.get("first_name"),
            name=data.get("name"),
            date_of_birth=data.get("date_of_birth"),
            national_chess_identifier=data.get("national_chess_identifier")
        )
    
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

    def delete(self):
        Players.list_of_player.remove(self)

    @classmethod
    def get_player_by_id(cls, chess_id):
        for player in cls.list_of_player:
            if player.national_chess_identifier == chess_id:
                return player
        return None
    
    @staticmethod
    def load_info_players_by_id(*id):
        info_player = []
        players_datas = Players.load_file()
        for player_datas in players_datas:
            if player_datas['id'] in id:
                info_player.append([player_datas['first_name'], player_datas['name']])
            

    @classmethod
    def clear_instances(cls):
        cls.list_of_player = []

