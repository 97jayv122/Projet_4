import json
import uuid
from datetime import datetime

FILE_PLAYER = "data/tournaments/players.json"


class Players:
    """
    Class representing a chess player.

    Stores player information including name, date of birth, national chess identifier, and unique ID.
    Provides methods for saving, loading, and updating player data.
    """
    def __init__(
        self,
        first_name,
        last_name,
        date_of_birth,
        national_chess_identifier,
        player_id=None,
    ):
        """
        Initialize a new instance of the Players class.

        Parameters:
            first_name (str): The first name of the player.
            last_name (str): The last name of the player.
            date_of_birth (str): The player's date of birth.
            national_chess_identifier (str): The national chess identifier.
            player_id (str, optional): Unique identifier for the player. Generated if not provided.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.national_chess_identifier = national_chess_identifier
        # Preserve existing ID if provided; otherwise, generate a new UUID.
        self.id = (
            player_id if player_id else str(uuid.uuid4())
        )
        self.create_at = datetime.now().isoformat()
        self.update_at = ""

    def __repr__(self):
        """
        Return a string representation of the player.

        Returns:
            str: A string in the format "FirstName.LastName".
        """
        return str(self.first_name) + "." + str(self.last_name)

    def to_dict(self):
        """
        Convert the player's attributes to a dictionary.

        Returns:
            dict: Dictionary containing player attributes.
        """
        return self.__dict__

    def save(self):
        """
        Save the current player to the JSON file.

        Loads all players, appends this player, and then writes the updated list back to the file.
        """
        players = Players.load()
        players.append(self)

        with open(FILE_PLAYER, "w") as file:
            json.dump([player.to_dict() for player in players], file, indent=4)

    @staticmethod
    def save_all(players):
        """
        Save all players to the JSON file.

        Parameters:
            players (list): List of Players instances to save.
        """
        with open(FILE_PLAYER, "w") as file:
            json.dump([player.to_dict() for player in players], file, indent=4)

    @staticmethod
    def load():
        """
        Load player data from the JSON file.

        Returns:
            list: A list of Players instances loaded from the file.
                  Returns an empty list if no file or valid data is found.
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
        Create a Players instance from a dictionary.

        Parameters:
            data (dict): Dictionary containing player data.

        Returns:
            Players: A new Players instance initialized with the provided data.
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
        Restore a Players object from a JSON dictionary.

        Parameters:
            data (dict): Dictionary containing player data including optional
            fields like 'id', 'create_at', and 'update_at'.

        Returns:
            Players: An instance of Players populated with the provided data.
        """
        player = cls(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            date_of_birth=data.get("date_of_birth"),
            national_chess_identifier=data.get("national_chess_identifier"),
            player_id=data.get("id"),  # Restore existing ID if available
        )
        # Restore creation and update timestamps if available
        player.create_at = data.get("create_at", player.create_at)
        player.update_at = data.get("update_at", player.update_at)
        return player

    def update(self, **new_values):
        """
        Update player attributes with new values.

        Only allows updates to 'first_name', 'last_name', and 'date_of_birth'.
        Updates the 'update_at' timestamp after changes.

        Parameters:
            **new_values: Arbitrary keyword arguments for player attributes.
        """
        allowed_keys = ["first_name", "last_name", "date_of_birth"]
        for key, value in new_values.items():
            if key in allowed_keys:
                if value != "":
                    setattr(self, key, value)
        self.update_at = datetime.now().isoformat()

    @staticmethod
    def load_by_ids(*id):
        """
        Retrieve players whose IDs match any of the provided IDs.

        Parameters:
            *ids: Variable number of player IDs to filter by.

        Returns:
            list: List of Players instances with matching IDs.
        """
        players_load = []
        players = Players.load()
        for player in players:
            if player.id in id:
                players_load.append(player)
        return players_load
