import json
FOLDER_TOURNAMENT = "data/tournaments/"
FILE_TOURNAMENT = FOLDER_TOURNAMENT + "tournament.json"

class Management:
    def __init__(self):
        # self.list_tournaments = []
        pass

    def update(self, name, tournament_dict):
        if len(self.tournaments) > 0:
            for index, tournament in enumerate(self.tournaments):
                if tournament.name== name:
                    self.tournaments[index] = tournament_dict
                    break

    def save(self):
        with open(FILE_TOURNAMENT, "w") as file:
            json.dump(self.tournaments, file, indent=4)


    def load(self):
        try:
            with open(FILE_TOURNAMENT, "r") as file:
                data = json.load(file)
                 
                return self.tournaments
        except json.JSONDecodeError as e:
            print(f"pas de données a charger: {e}")
        except FileNotFoundError:
            print(f"Fichier introuvable : data/tournaments/tournaments")
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            raise
    
    # def instance_clear(self):
    #     self.list_tournaments = []
        
# management = Management()
# management.instance_clear()
# management.load()
# management.create_or_update("Home", {"name": "Home"})
# management.save()
# management.instance_clear()
# management.load()
# management.save()
