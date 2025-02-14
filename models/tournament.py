import json
from models.players import Players
from models.tours import Tours
from models.matchs import Matchs                                                                                                      
FOLDER_TOURNAMENT = "data/tournaments/"
FILE_TOURNAMENT = FOLDER_TOURNAMENT + "tournament.json"


# class Tournaments:
#     def __init__(self):
#         # self.list_tournaments = []
#         pass

class Tournaments:
    def __init__(self, name, place, date_start, date_end,
                 number_of_turns=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.number_of_turns = number_of_turns
        self.list_player = []
        self.list_of_tours = []
        self.current_tour = 0
        self.current_matchs = []
        self.description = ""

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
            date_end=data.get("date_end")
        )
        tournament.list_player=list_player
        tournament.list_of_tours=list_of_tours
        tournament.current_tour=data.get("current_tour", 0)
        tournament.current_matchs=data.get("current_matchs", [])
        tournament.description=data.get("description", "")

        return tournament
        

    def to_dict(self):
        return {
            "name": self.name,
            "place": self.place,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "number_of_turns": self.number_of_turns,
            "list_player": [
                player.to_dict() if isinstance(player, Players)
                else player for player in self.list_player
                ],
            "list_of_tours": [
                tour.to_dict() if isinstance(tour, Tours)
                else tour for tour in self.list_of_tours
                ],
            "current_tour": self.current_tour,
            "current_matchs": self.current_matchs,
            "description": self.description
        }

    # @classmethod
    # def load(cls, data):
    #     return cls.from_dict(data)

    
    def start_new_tour(self):
        """
        Démarre un nouveau tour et initialise les matchs.
        """
        self.current_tour = Tours(self.list_player)
        self.current_matchs = []  # Réinitialise les matchs pour le nouveau tour
        self.list_of_tours.append(self.current_tour)

    def add_1_to_current_tour(self):
        self.current_tour += 1
        

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
        self.current_matchs = []
        self.description = ""

    def recovery_list_of_matchs(self, matchs):
        """
        Ajoute une liste de matchs au tour.

        Args:
            matchs (list): Liste d'instances de la classe Matchs.
        """
        self.matchs_list_by_round = [match.to_dict() for match in matchs]

    def add_tour(self, tour):
        """
        Ajoute un tour à la liste des tours du tournoi.

        Args:
            tour (Tours): Instance de la classe Tours. 
        """
        self.list_of_tours.append(tour.to_dict())

    def add_match_to_current_tour(self, match):
        """
        Ajoute un match au tour actuel.
        """
        if self.current_tour:
            self.current_matchs.append(match)
            self.current_tour.recovery_list_of_matchs(self.current_matchs)

    def __repr__(self):
        tr = f"Nom du tournoi : {self.name}, player: "  
        for player in self.list_player:
            tr = tr + f"\n{player}"
        return tr 
    
    def update(self, name, tournament_dict):
        if len(self.tournaments) > 0:
            for index, tournament in enumerate(self.tournaments):
                if tournament.name== name:
                    self.tournaments[index] = tournament_dict
                    break

    def save(self):
        tournaments = Tournaments.load()
        tournaments.append(self)

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