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

    def run(self):
        
        while True:
            Players.instances_load()
            Utils.clear()
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
                    Players.clear_instances()
                    break

                case _:
                    self.view.display_string("Choix inconnue.")
                    Players.clear_instances()

    def add_player(self):
        """
        
        """        
        number_player_add = self.view.number_add_player()
        if number_player_add == 0:
            breakpoint
        for i in range(1, number_player_add + 1):
            info_player = self.view.request_add_player()
            player = Players.from_dict(info_player)
            Players.instances_save()
        Players.clear_instances()

    def mofify_player(self):
        self.display_player()
        Players.instances_load()
        if Players.list_of_player:
            chess_id = self.view.request_player_id("modifier")
            if chess_id:
                player = Players.get_player_by_id(chess_id)
                if player:
                    data = self.view.request_modify_player()
                    player.update(**data)
                    Players.instances_save()
                    self.display_player(f"\nLe joueur avec l'ID: {chess_id} a été correctement modifié.")
                else:
                    self.view.display_string(f"\nLe joueur avecl'ID: {chess_id} n'as pas été trouvé.")
                    Players.clear_instances()
            else:
                Players.clear_instances()
                breakpoint
        else:
            Players.clear_instances()
            breakpoint

    def suppress_player(self):
        self.display_player()
        Players.instances_load()
        if Players.list_of_player:
            chess_id = self.view.request_player_id("supprimer")
            if chess_id:
                player = Players.get_player_by_id(chess_id)
                if player == None:
                    self.view.display_string("\nJoueur inexistant")
                    self.display_player()

                else:
                    player.delete()
                    Players.instances_save()
                    self.display_player(f"\nLe joueur avec l'ID: {chess_id} a été correctement supprimé.")
                    Players.clear_instances()
            else:
                Players.clear_instances()
                breakpoint
        else:
            Players.clear_instances()
            breakpoint

    def display_player(self, prompt=""):
        data_players = [player.to_dict() for player in Players.list_of_player]
        if data_players:
            self.view.display_table(data_players, prompt)
            Players.clear_instances()
        else:
            self.view.display_string("Pas de joueur dans la base de donnée")