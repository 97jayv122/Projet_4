import json
import uuid
from models.players import Players
from models.tours import Tours
from models.matchs import Matchs                                                                                                      
FOLDER_TOURNAMENT = "data/tournaments/"
FILE_TOURNAMENT = FOLDER_TOURNAMENT + "tournament.json"


class Tournaments:
    def __init__(self, name, place, date_start, date_end,
                 number_of_turns=4, tournament_id=None):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.number_of_turns = number_of_turns
        self.id = tournament_id if tournament_id else str(uuid.uuid4())
        self.list_player = []
        self.list_of_tours = []
        self.current_tour = 0
        self.description = ""
        self.player_scores = {}

    @classmethod
    def from_dict(cls, data):
        list_player = [
            Players.from_dict(player) if isinstance(player, dict)
            else player for player in data.get("list_player", [])
            ]
        list_of_tours = [
            Tours.from_dict(tour) if isinstance(tour, dict)
            else tour for tour in data.get("list_of_tours", [])
            ]
        tournament = cls(
            name=data.get("name"),
            place=data.get("place"),
            date_start=data.get("date_start"),
            date_end=data.get("date_end"),
            tournament_id=data.get("tournament_id")
        )
        tournament.list_player=list_player
        tournament.list_of_tours=list_of_tours
        tournament.current_tour=data.get("current_tour", 0)
        tournament.description=data.get("description", "")
        tournament.player_scores=data.get("player_scores", {})

        return tournament
        

    def to_dict(self):
        return {
            "name": self.name,
            "place": self.place,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "number_of_turns": self.number_of_turns,
            "list_player": [
                player if isinstance(player, str) else player.id
                for player in self.list_player
                ],
            "list_of_tours": [
                tour.to_dict() if isinstance(tour, Tours)
                else tour for tour in self.list_of_tours
                ],
            "current_tour": self.current_tour,
            "tournament_id": self.id,
            "description": self.description,
            "player_scores": self.player_scores
        }

    def instance_clear(self):
        """
        Réinitialise tous les attributs de l'instance aux valeurs par défaut.
        """
        self.name = ""
        self.place = ""
        self.date_start = ""
        self.date_end = ""
        self.number_of_turns = 4
        self.list_player = []
        self.list_of_tours = []
        self.current_tour = 0
        self.description = ""

    def add_1_to_current_tour(self):
        self.current_tour += 1

    def __repr__(self):
        tr = f"Nom du tournoi : {self.name}, player: "  
        for player in self.list_player:
            tr = tr + f"\n{player}"
        return tr 
    
    def update(self, id):
        tournaments = Tournaments.load()
        if len(tournaments) > 0:
            for index, tournament in enumerate(tournaments):
                if tournament.id == id:
                    tournaments[index] = self
                    Tournaments.save_all(tournaments)
                    break

    def save(self):
        tournaments = Tournaments.load()
        tournaments.append(self)

        with open(FILE_TOURNAMENT, "w") as file:
            json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)

    @staticmethod
    def save_all(tournaments):

        with open(FILE_TOURNAMENT, "w") as file:
            json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)
        
    @staticmethod
    def load():
        try:
            with open(FILE_TOURNAMENT, "r") as file:
                datas = json.load(file)
                return [Tournaments.from_dict(data) for data in datas]
        except json.JSONDecodeError as e:
            print(f"pas de données a charger: {e}")
        except FileNotFoundError:
            print(f"Fichier introuvable : data/tournaments/tournaments")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
        return []
    
    @staticmethod
    def clear_json_tournament():
        with open(FILE_TOURNAMENT, "w") as file:
            json.dump([], file, indent=4)

    def add_player_score(self, player):
        """
        Add a player to the tournament and initializes their score.

        Args:
            player (_type_): _description_
        """
        self.list_player.append(player)
        self.player_scores[player.id] = 0.0

    def update_player_score(self,player, score_delta):
        """_summary_

        Args:
            player_id (_type_): _description_
            score_delta (_type_): _description_
        """
        if player.id in self.player_scores:
            self.player_scores[player.id] += score_delta
