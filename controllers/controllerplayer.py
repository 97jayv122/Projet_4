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
            Utils.clear()
            action = self.view.player_menu()
            match action:
                case self.ADD_PLAYER:
                    self.add_player()

                case self.DISPLAY_PLAYER:
                    self.display_player()
                case self.MODIFY_PLAYER:
                    pass

                case self.SUPPRESS_PLAYER:
                    pass

                case self.RETURN_MAIN_MENU:
                    break

                case _:
                    print("Choix inconnue.")

    def add_player(self):
        """
        
        """        
        number_player_add = self.view.number_add_player()
        for i in range(1, number_player_add + 1):
            info_player = self.view.request_add_player()
            player = Players.from_dict(info_player)
        player.save()
        

    def display_player(self):
        data_players = Players.load_file()
        self.view.display_json(data_players)
