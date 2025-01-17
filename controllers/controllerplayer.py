from models.players import Players
from view.utils import Utils


class ControllerPlayer:
    """
    Controller of the player menu that allows to add, display, and load players.
    """    
    ADD_PLAYER = "1"
    DISPLAY_PLAYER = "2"
    MODIFY_PLAYER = "3"
    SUPPRESS_PLAYER = "4"
    RETURN_MAIN_MENU = "x"
    def __init__(self, view):
        self.view = view

    def run(self):
        
        while True:
            Players.instances_load()
            Utils.clear()
            action = self.view.player_menu()
            match action:
                case self.ADD_PLAYER:
                    self.add_player()

                case self.DISPLAY_PLAYER:
                    self.display_player()
                case self.MODIFY_PLAYER:
                    self.mofify_player()

                case self.SUPPRESS_PLAYER:
                    self.suppress_player()

                case self.RETURN_MAIN_MENU:
                    break

                case _:
                    print("Choix inconnue.")
                    Players.clear_instances()

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
        print(chess_id)
        player = Players.get_player_by_id(chess_id)
        if player:
            data = self.view.request_modify_player()
            player.update(**data)
        else:
            print("Joueur inexistant")
            input("Appuyer sur entrée pour continuer")
        Players.instances_save()
        Players.clear_instances()

    def suppress_player(self):
        self.display_player()
        Players.instances_load()
        chess_id = self.view.request_player_id("supprimer")
        player = Players.get_player_by_id(chess_id)
        if player is None:
            print("Joueur inexistant")
        else:
            player.delete()
        Players.instances_save()
        Players.clear_instances()
   
    # def display_player(self):
    #     data_players = Players.load_file()
    #     self.view.display_json(data_players)

    def display_player(self):
        data_players = [player.to_dict() for player in Players.list_of_player]
        self.view.display_table(data_players)
        Players.clear_instances()