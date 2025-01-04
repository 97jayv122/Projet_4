import re
import time
import datetime

class View:
    def home_menu(self):
        print("")
        print("Bienvenue dans le gestionnaire de tournoi d'échecs")
        print("1 pour entrer dans le menu joueur.")
        print("2 pour entrer dans le menu tournois.")
        print("3. pour voir les rapports.")
        print("x pour quitter le programme.")
        return input("Entrer uvotre choix : ")
        

    def player_menu(self):
        print("")
        print("Bienvenue dans le gestionnaire de joueur")
        print("1 pour entrer un joueur")
        print("2 pour lister les joueurs")
        print("3 pour charger les joueurs.")
        print("x pour quitter le programme.")
        return input("Entrer uvotre choix : ")
        
    def tournament_menu(self):
        print("")
        print("Bienvenue dans le gestionnaire de tournoi")
        print("1 créer un tournoi")
        print("2 Commencer un tour")
        print("3 Rentrer les scores des joueurs")
        print("4 Sauvegarder le tournoi")
        print("5 Charger le tournoi")
        print("x pour quitter le programme.")
        return input("Entrer uvotre choix : ")
    
    def select_player(self, players):
        player_tournament = []
        print("")
        print("Sélectionnez les joueurs pour le tournoi")
        for i, player in enumerate(players):
            print(f"{i + 1}. {player}")
            print("=====================================")
        players_enter = input("Entrer les numéros des joueurs séparés par une virgule : ")
        split_players = players_enter.split(",")
        for player in split_players:
            player_tournament.append(players[int(player) - 1])
        return player_tournament

    def request_create_tournament(self):
        file_tournament = {}
        print("")
        file_tournament["name"] = input("Entrer le nom du tournoi : ")
        file_tournament["location"] = input("Entrer le lieu du tournoi : ")
        file_tournament["date_start"] = input("Entrer la date de début du tournoi : ")
        file_tournament["date_end"] = input("Entrer la date de fin du tournoi : ")
        return file_tournament 
    
    def number_add_player(self):
        print("")
        while True:  # Boucle pour continuer à demander une entrée valide
            try:
                number = int(input("Entrez le nombre de participants en chiffre : "))
                if number <= 0:  # Vérification si le nombre est positif
                    print("Veuillez entrer un nombre supérieur à 0.")
                    continue
                return number  # Retourne le nombre valide
            except ValueError:
                print("Entrée invalide. Veuillez entrer un chiffre valide.")
    
    def request_add_player(self):
        file_player = {}
        file_player["first_name"] = input("Entrer le prénom du joueur : ")
        file_player["name"] = input("Entrer le nom du joueur : ")
        file_player["date_of_birth"] = input("Entrer la date de naissance du joueur(01/12/2003) : ")
        file_player["national_chess_identifier"] = input("Enter l'identiant national d' échecs : ")
        return file_player
    
    def valide_national_chess_identifier(identifier):
        pattern = r"^[A-Z]{2}[0-9]{5}$"
        return bool(re.match(pattern, identifier))
    
    def valide_date(date, date_format="%d/%m/%y"):
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False
        
    def display_player(self, players):
        for player in players:
            print(player)
        time.sleep(3)
        exit