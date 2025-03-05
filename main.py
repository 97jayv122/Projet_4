#!/usr/bin/python
# -*-coding: utf-8-*-
"""
Main entry for the application.
"""

from controllers.maincontroller import Controller
from view.view import View


def main():
    """
    Main function of the application.

    It initializes the View and Controller, and then starts the application.
    The application can be interrupted by the user (e.g. via Ctrl+C).
    """
    view = View()
    administrator = Controller(view)
    try:
        administrator.run()
    except KeyboardInterrupt:
        print("\nProgramme arrêté par l'utilisateur. Au revoir !")


if __name__ == "__main__":
    main()
