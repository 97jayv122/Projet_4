
import os
import re
from datetime import datetime
from models.players import Players


class Utils:
    @staticmethod
    def valide_national_chess_identifier(identifier):
        """
        Validates whether the given national chess identifier follows the correct format.

        Args:
            identifier (str): The national chess identifer to validate.

        Returns:
            bool: True if the identifier is valid, False otherwise.
        """
        pattern = r"^[A-Z]{2}[0-9]{5}$"
        return bool(re.match(pattern, identifier))
    
    @staticmethod
    def valide_date(date, date_format="%d/%m/%Y"):
        """
        Validates whether a given date string follows the specified format.

        Args:
            date (str): The date string to validate.
            date_format (str, optional): The expected format of the date string.
                                         Defaults to "%d/%m/%Y" (DD/MM/YYYY).

        Returns:
            bool: True if the date is valid and matches the format, False otherwise.
        """
        while True:
            try:
                datetime.strptime(date, date_format)
                return True
            except ValueError:
                return False
            
    @staticmethod
    def get_valid_date(prompt, error_message):
        """
        Prompt the user to enter a valid date and ensures it follows the expected format.

        Args:
            prompt (str): The message displayed to request input from the user. 
            error_message (str): The message displayed when the input does not match the expected format.

        Returns:
            str: A valid date string that conforms to the required format.
        """
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
        """
        Checks wether the national identifier chess exists in the saved records.

        Args:
            identifier (str): The national chess identifier of the player.

        Returns:
            bool: True if the player Id exists in the saveds records, False otherwise.
        """
        players = Players.load()
        for p in players:
            if p.national_chess_identifier == identifier:
                return True
        return False
    
    @staticmethod
    def get_chess_identifier(prompt, invert=True):
        """
        Check the validity of a chess identifier and whether it exists in the saveds records

        Args:
            prompt (_type_): request the player's chess identifer
            invert (bool, optional): If true, the function returns an identifier that does not exist
            in the saved records. if false returns an existing identifer.
            Defaults to True.

        Returns:
            _str_: A valid chess identifier that either exists or does not exist, depending on the `invert` paremeter.
        """
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

    @staticmethod
    def check_score(score_1):
        """
        Determines the second player's score based on the first player's score.

        Args:
            score_1 (float): The score of the first player.

        Returns:
            float: The score of the second player, determined based on the first player's score. 
        """
        if score_1 == 1:
            score_2 = 0
            return score_2
        elif score_1 == 0.5:
            score_2 = 0.5
            return score_2
        
        elif score_1 == 0:
            score_2 = 1
            return score_2

        else:
            return None
        