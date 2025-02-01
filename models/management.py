import json
FOLDER_TOURNAMENT = "data/tournaments/tournament.json"


class Management:
    def __init__(self):
        self.list_tournaments = []

    def create_or_update(self, name, date, tournament_dict):
        for index, tournament in enumerate(self.list_tournaments):
            if tournament["name"] == name and tournament:
                self.list_tournaments[index] = tournament_dict
                break
            else:
                self.list_tournaments.append(tournament_dict)

    def save(self):
        with open(FOLDER_TOURNAMENT, "w") as file:
            json.dump(self.list_tournaments, file)

    def load(self):
        try:
            with open(FOLDER_TOURNAMENT, "r") as file:
                data = json.load(file)
                self.list_tournaments = data
        except json.JSONDecodeError as e:
            print(f"pas de données a charger: {e}")
        except FileNotFoundError:
            print(f"Fichier introuvable : data/tournaments/tournaments")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            raise
        return None
    
    def instance_clear(self):
        self.list_tournaments = []

management = Management()
management.instance_clear()
management.load()
management.save()
management.instance_clear()
management.load()
management.save()
