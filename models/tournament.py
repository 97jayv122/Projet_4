from models.players import Players
class Tournament:
    def __init__(self, name, place, date_start, date_end,
                 number_of_turns=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.number_of_turns = number_of_turns
        self.list_player = []
        self.list_of_tours = []
        self.current_tour = 0
        self.description = ""

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            place=data.get("place"),
            date_start=data.get("date_start"),
            date_end=data.get("date_end")
        )
    
    def player_retrieve(self):
        self.list_player = Players.load_data_player()