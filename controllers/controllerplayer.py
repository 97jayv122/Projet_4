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
            action = self.view.player_menu()
            match action:
                case self.ADD_PLAYER:
                    Utils.clear()
                    self.add_player()

                case self.DISPLAY_PLAYER:
                    Utils.clear()
                    self.display_player
                case self.MODIFY_PLAYER:
                    pass

                case self.SUPPRESS_PLAYER:
                    pass

                case self.RETURN_MAIN_MENU:
                    Utils.clear()
                    break

                case _:
                    print("Choix inconnue.")

    def add_player(self):
        number_player_add = self.view.number_add_player()
        for i in range(1, number_player_add + 1):
            info_player = self.view.request_add_player()
            player = Players.from_dict(info_player)
        player.save_player()
        

    def display_player(self):
        data_players = Players.load_file()
        self.view.display(data_players)
