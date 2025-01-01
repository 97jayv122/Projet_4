class View:
    def home_menu(self):
        print("Bienvenue dans le gestionnaire de tournoi d'échecs")
        print("1 pour ajouter un joueur")
        print("2 pour lister les joueurs")
        print("x pour quitter le programme")
        return input("Entrer uvotre choix : ")

    def number_add_player(self):
        return int(input("Entrer le nombre de participant en chiffre : "))
    
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
        exit