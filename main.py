#!/usr/bin/python
#-*-coding: utf-8-*-
from controllers.maincontroller import Controller
from view.view import View
"""
"""


def main():
    view = View()
    administrator = Controller(view)
    administrator.run()


if __name__ == "__main__":
    main()
