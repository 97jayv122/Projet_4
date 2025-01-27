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
                    break

                case _:
                    print("Choix inconnue.")
                    input("Appuyer sur entrée pour continuer...")

    def add_player(self):
        """
        
        """        
        number_player_add = self.view.number_add_player()
        for i in range(1, number_player_add + 1):
            info_player = self.view.request_add_player()
            player = Players.from_dict(info_player)
            Players.instances_save()
        Players.clear_instances()

    def mofify_player(self):
        self.display_player()
        Players.instances_load()
        chess_id = self.view.request_player_id("modifier")
        player = Players.get_player_by_id(chess_id)
        if player != None:
            data = self.view.request_modify_player()
            player.update(**data)
            Players.instances_save()
            self.display_player()
        else:
            print(f"Le joueur avecl'ID: {chess_id} n'as pas été trouvé.")
            input("Appuyer sur entrée pour continuer")
            self.display_player()
            
            


    def suppress_player(self):
        self.display_player()
        Players.instances_load()
        chess_id = self.view.request_player_id("supprimer")
        player = Players.get_player_by_id(chess_id)
        if player is None:
            print("Joueur inexistant")
            self.display_player()

        else:
            player.delete()
            Players.instances_save()
            self.display_player()
            Players.clear_instances()

    # def display_player(self):
    #     data_players = Players.load_file()
    #     self.view.display_json(data_players)

    def display_player(self):
        data_players = [player.to_dict() for player in Players.list_of_player]
        self.view.display_table(data_players)
        Players.clear_instances()