from models.players import Players


class ConstantTournamentReport:
    """
    Constants representing options in the tournament report menu.
    """
    PLAYERS_TOURNAMENT = "1"
    TOURNAMENT_INFO = "2"
    RETURN_REPORT_MAIN_MENU = "x"


class ControllerTournamentReport:
    """
    Controller for generating a report for a specific tournament.

    Provides functionalities to display a sorted list of players
    and detailed tournament information.
    """
    def __init__(self, view, tournament):
        """
        Initialize the tournament report controller.

        Parameters:
            view: The view instance for user interactions.
            tournament: The tournament object for which to generate the report.
        """
        self.view = view
        self.tournament = tournament

    def run(self):
        """
        Run the tournament report loop.

        Processes user actions to display players sorted alphabetically,
        show tournament information, or return to the main report menu.
        """
        while True:
            action = self.view.report_menu_tournament()
            match action:
                case ConstantTournamentReport.PLAYERS_TOURNAMENT:
                    self.get_player_tournament_sorted()

                case ConstantTournamentReport.TOURNAMENT_INFO:
                    self.get_tournament_info_dict()

                case ConstantTournamentReport.RETURN_REPORT_MAIN_MENU:
                    break

    def get_player_tournament_sorted(self):
        """
        Display a list of tournament players sorted alphabetically.
        """
        message = "Liste des joueurs du tournoi par ordre alphabétique."
        players = Players.load_by_ids(*self.tournament.list_player)
        players_sorted = sorted(players, key=lambda x: (x.last_name.capitalize(), x.first_name.capitalize()))
        players_dict_sorted = [player.to_dict() for player in players_sorted]
        self.view.display_table(players_dict_sorted, message)
        self.view.press_enter()

    def get_tournament_info_dict(self):
        """
        Display detailed information about the tournament.

        Constructs a dictionary with key details such as tournament name,
        location, number of players, dates, rounds, description, status,
        and details for each round and match.
        """
        tournament_info = {
            "Nom du tournoi": self.tournament.name,
            "Lieu du tournoi": self.tournament.place,
            "Nombre de joueurs": self.tournament.number_player,
            "Date de début": self.tournament.date_start,
            "Date de fin": self.tournament.date_end,
            "Nombre de tours": self.tournament.number_of_turns,
            "Description": self.tournament.description,
            "Statut": self.tournament.stat,
            "Tours": []  # This will contain information about each round.
        }

        # Loop through each round in the tournament
        for tour in self.tournament.list_of_tours:
            tour_info = {
                "Tour": tour.tour_number,
                "Date de début": tour.time_start,
                "Date de fin": tour.time_end,
                "Statut": tour.stat,
                "Matchs": []  # This will contain information about each match in the round.
            }
            # Loop through each match in the round
            for match in tour.matchs:
                match_info = {
                    "Joueur 1": {
                        "Nom": Players.load_by_ids(match[0][0])[0],
                        "Score": match[0][1]
                    },
                    "Joueur 2": {
                        "Nom": Players.load_by_ids(match[1][0])[0],
                        "Score": match[1][1]
                    }
                }
                tour_info["Matchs"].append(match_info)
            tournament_info["Tours"].append(tour_info)

        self.view.display_tournament_info_table(tournament_info)
        self.view.press_enter()
