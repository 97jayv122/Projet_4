

class ConstantReport:

    TOURNAMENTS = "1"
    PLAYERS = "2"
    RETURN_TOURNAMENT_MANAGEMENT_MENU = "x"

class ControllerReport:


    def __init__(self, view):
        self.view = view

    def run(self):
        while True:
            action = self.view.report_menu()
            match action:
                case ConstantReport.TOURNAMENTS:
                    pass
                case ConstantReport.PLAYERS:
                    pass