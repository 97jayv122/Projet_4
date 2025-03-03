import json
import uuid
from datetime import datetime

FILE_PLAYER = "data/tournaments/players.json"


class Players:

    def __init__(
        self,
        first_name,
        last_name,
        date_of_birth,
        national_chess_identifier,
        player_id=None,
    ):
        """
        Initializes a new instance of the Players class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.national_chess_identifier = national_chess_identifier
        self.id = (
            player_id if player_id else str(uuid.uuid4())
        )  # Préserve l'ID existant si fourni
        self.create_at = datetime.now().isoformat()
        self.update_at = ""

    def __repr__(self):
        """
        Return a string representation of the Players instance.

        Returns:
            str: A string in the format "FirstName.LastName"
        """
        return str(self.first_name) + "." + str(self.last_name)

    def to_dict(self):
        return self.__dict__

    def save(self):
        players = Players.load()
        players.append(self)

        with open(FILE_PLAYER, "w") as file:
            json.dump([player.to_dict() for player in players], file, indent=4)

    @staticmethod
    def save_all(players):

        with open(FILE_PLAYER, "w") as file:
            json.dump([player.to_dict() for player in players], file, indent=4)

    @staticmethod
    def load():
        """
        Load player data from a JSON file.

        This method attempts to open a JSON file defined by the FILE_PLAYER constant, parse its content,
        and create a list of Players instances using the restore_from_json class method.
        If the JSON data is invalid or the file is not found, an error message is printed and an empty list is returned.

        Returns:
            List: A list of Players instances if the file is loaded successfully; otherwise, an empty list.
        """
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
    def from_dict(cls, data):
        """
        Creates a Players instance from a dictionary.

        This method creates a new Players instance using the provided dictionary data.
        It expects the following keys to be present in the dictionary:
            - "first_name" (str): The first name of the player.
            - "last_name" (str): The last name of the player.
            - "date_of_birth" (str): The date of birth of the player.
            - "national_chess_identifier" (str): The national chess identifier of the player.

        Args:
            data (dict): A dictionnary containing player data.

        Returns:
            Players: A new instance of the Players class initialized with the provided data.
        """
        return Players(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            date_of_birth=data.get("date_of_birth"),
            national_chess_identifier=data.get("national_chess_identifier"),
        )

    @classmethod
    def restore_from_json(cls, data):
        """
        Restores a Player object from a JSON dictionary.

        Args:
            data (dict): A dictionary containing player data with the following keys:
                - "first_name" (str): The first name of the player.
                - "last_name" (str): The last name of the player.
                - "date_of_birth" (str): The date of birth of the player.
                - "national_chess_identifier" (str): The national chess identifier of the player.
                - "id" (int): The unique ID of the player.
                - "create_at" (str, optional): The creation date of the player record.
                - "update_at" (str, optional): The last update date of the player record.

        Returns:
            Player: An instance of the Player class populated with the provided data.
        """
        player = cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            date_of_birth=data.get("date_of_birth"),
            national_chess_identifier=data.get("national_chess_identifier"),
            player_id=data.get("id"),  # Restaurer l'ID existant
        )
        # Restauration des dates de création et modification
        player.create_at = data.get("create_at", player.create_at)
        player.update_at = data.get("update_at", player.update_at)
        return player

    def update(self, **new_values):
        allowed_keys = ["first_name", "last_name", "date_of_birth"]
        for key, value in new_values.items():
            if key in allowed_keys:
                if value != "":
                    setattr(self, key, value)
        self.update_at = datetime.now().isoformat()

    @staticmethod
    def load_by_ids(*id):
        """
        Retrieve players whose IDs match any of the provided values.

        This method loads all player instances using Players.load() and filter them,
        returning only those whose 'id' attribute is included in the provided arguments.

        Args:
            *id: A variable number player IDs nto filter by.

        Returns:
            List: A list of player instances with matching IDs.
        """
        players_load = []
        players = Players.load()
        for player in players:
            if player.id in id:
                players_load.append(player)
        return players_load

    def __lt__(self, other):
        return self.last_name.capitalize() < other.last_name.capitalize()
