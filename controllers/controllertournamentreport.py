from models.players import Players


class ConstantTournamentReport:

    PLAYERS_TOURNAMENT = "1"
    TOURNAMENT_INFO = "2"
    RETURN_REPORT_MAIN_MENU = "x"


class ControllerTournamentReport:
    def __init__(self, view, tournament):
        self.view = view
        self.tournament = tournament

    def run(self):
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
        message = "Liste des joueurs du tournoi par ordre alphabétique(nom)."
        players = Players.load_by_ids(*self.tournament.list_player)
        players_sorted = sorted(players, key=lambda x: (x.last_name).capitalize())
        players_dict_sorted = [player.to_dict() for player in players_sorted]
        self.view.display_table(players_dict_sorted, message)
        self.view.press_enter()

    def get_tournament_info_dict(self):
        # Création d'un dictionnaire principal regroupant les infos du tournoi
        tournament_info = {
            "Nom du tournoi": self.tournament.name,
            "Lieu du tournoi": self.tournament.place,
            "Nombre de joueurs": self.tournament.number_player,
            "Date de début": self.tournament.date_start,
            "Date de fin": self.tournament.date_end,
            "Nombre de tours": self.tournament.number_of_turns,
            "Description": self.tournament.description,
            "Statut": self.tournament.stat,
            "Tours": []  # Liste qui contiendra les informations sur chaque tour
        }

        # Parcours des tours du tournoi
        for tour in self.tournament.list_of_tours:
            tour_info = {
                "Tour": tour.tour_number,
                "Date de début": tour.time_start,
                "Date de fin": tour.time_end,
                "Statut": tour.stat,
                "Matchs": []  # Liste qui contiendra les informations sur chaque match du tour
            }
            # Parcours des matchs du tour
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
