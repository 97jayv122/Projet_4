from models.players import Players
from view.utils import Utils


class ConstantPlayer:

    ADD_PLAYER = "1"
    DISPLAY_PLAYER = "2"
    MODIFY_PLAYER = "3"
    SUPPRESS_PLAYER = "4"
    RETURN_MAIN_MENU = "x"

class ControllerPlayer:
    """
    Controller of the player menu that allows to add, display, and load players.
    """    
    def __init__(self, view):
        self.view = view
        self.players = Players.load()

    def run(self):
        
        while True:
            self.players = Players.load()
            action = self.view.player_menu()
            match action:
                case ConstantPlayer.ADD_PLAYER:
                    self.add_player()

                case ConstantPlayer.DISPLAY_PLAYER:
                    self.display_player()

                case ConstantPlayer.MODIFY_PLAYER:
                    self.mofify_player()

                case ConstantPlayer.SUPPRESS_PLAYER:
                    self.suppress_player()

                case ConstantPlayer.RETURN_MAIN_MENU:
                    break

                case _:
                    self.view.display_string("Choix inconnue.")

    def add_player(self):
        """
        
        """        
        number_player_add = self.view.number_add_player()
        if number_player_add == 0:
            breakpoint
        for i in range(1, number_player_add + 1):
            input_player = self.view.request_add_player()
            player = Players.from_dict(input_player)
            player.add()

    def mofify_player(self):
        self.display_player()
        if self.players:
            chess_id = self.view.request_player_id("modifier")
            if chess_id:
                player = self.load_by_id(chess_id)
                if player:
                    data = self.view.request_modify_player()
                    player.update(**data)
                    player.save()
                    self.display_player(f"\nLe joueur avec l'ID: {chess_id} a été correctement modifié.")
                else:
                    self.view.display_string(f"\nLe joueur avecl'ID: {chess_id} n'as pas été trouvé.")

            else:
                self.display_string("Nous n'avons pas trouvez de jouer avec cette id ")
        else:
            self.display_string("La base de donnée joueur est vide")

    def suppress_player(self):
        self.display_player()
        if self.players:
            chess_id = self.view.request_player_id("supprimer")
            if chess_id:
                player = self.load_by_id(chess_id)
                if player == None:
                    self.view.display_string("\nJoueur inexistant")
                    self.display_player()

                else:
                    player.delete(player)
                    self.display_player(f"\nLe joueur avec l'ID: {chess_id} a été correctement supprimé.")
            else:
                self.display_string("Nous n'avons pas trouvez de jouer avec cette id ")   
        else:
            self.display_string("La base de donnée joueur est vide")

    def display_player(self, prompt=""):
        if self.players:
            players_dict = [player.to_dict() for player in self.players]
            self.view.display_table(players_dict, prompt)
        else:
            self.view.display_string("Pas de joueur dans la base de donnée")

    def load_by_id(self, chess_id):
        for player in self.players:
            if player.national_chess_identifier == chess_id:
                return player
        return None
    