#!/usr/bin/python
#-*-coding: utf-8-*-
from controllers.maincontroller import Controller
from view.view import View
"""
"""


def main():
    """
    Main function of the application that allows to start the application.
    """    
    view = View()
    administrator = Controller(view)
    try:
        administrator.run()
    except KeyboardInterrupt:
        print("\nProgramme arrêté par l'utilisateur. Au revoir !")

if __name__ == "__main__":
    main()
