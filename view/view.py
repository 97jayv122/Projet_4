import time

class View:
    def home_menu(self):
        print("Bienvenue dans le gestionnaire de tournoi d'échecs")
        print("1 pour entrer dans le menu joueur.")
        print("2 pour entrer dans le menu tournois.")
        print("x pour quitter le programme.")
        return input("Entrer uvotre choix : ")
    
    def player_menu(self):
        print("Bienvenue dans le gestionnaire de joueur")
        print("1 pour entrer un joueur")
        print("2 pour lister les joueurs")
<<<<<<< HEAD
        print("3 pour charger les joueurs.")
        print("x pour quitter le programme.")
        return input("Entrer uvotre choix : ")
    
    def tournament_menu(self):
        print("Bienvenue dans le gestionnaire de tournoi")
        print("1 créer un tournoi")
        print("2 Commencer un tour")
        print("3 Terminer un tour")
        print("4 Sauvegarder le tournoi")
        print("5 Charger le tournoi")
=======
        print("3 pour entrer dans le menu tournois.")
>>>>>>> c2ce1e66595171b76cc82fe7ea370da7f47edc92
        print("x pour quitter le programme.")
        return input("Entrer uvotre choix : ")

    def request_create_tournament(self):
        file_tournament = {}
        file_tournament["name"] = input("Entrer le nom du tournoi : ")
        file_tournament["location"] = input("Entrer le lieu du tournoi : ")
        file_tournament["date_start"] = input("Entrer la date de début du tournoi : ")
        file_tournament["date_end"] = input("Entrer la date de fin du tournoi : ")
        return file_tournament 
    
    def number_add_player(self):
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
    
    def display_player(self, players):
        for player in players:
            print(player)
        time.sleep(3)
        exit