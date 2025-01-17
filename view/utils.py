
import os
import re
from datetime import datetime
from models.players import Players


class Utils:
    @staticmethod
    def valide_national_chess_identifier(identifier):
        pattern = r"^[A-Z]{2}[0-9]{5}$"
        return bool(re.match(pattern, identifier))
    
    @staticmethod
    def valide_date(date, date_format="%d/%m/%Y"):
        while True:
            try:
                datetime.strptime(date, date_format)
                return True
            except ValueError:
                return False
            
    @staticmethod
    def get_valid_date(prompt, error_message):
        while True:
            date_input = input(prompt)
            if Utils.valide_date(date_input):
                return date_input
            print(error_message)
    
    @staticmethod
    def clear():
        """
        Clear the console screen
        """        
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def chess_identifier_existing(identifier):
        datas = Players.load_file()
        for data in datas:
            if data["national_chess_identifier"] == identifier:
                return True
        return False
    
    @staticmethod
    def get_chess_identifier(prompt, invert=True):
        while True:
            national_chess_identifier = input(prompt)
            if Utils.valide_national_chess_identifier(national_chess_identifier):
                if (not Utils.chess_identifier_existing(
                    national_chess_identifier
                    ) if invert else Utils.chess_identifier_existing(
                        national_chess_identifier)):                        
                    return national_chess_identifier
                else:
                    print("Identifiant existe déjà")
            else:
                print("Identifiant est invalide")
