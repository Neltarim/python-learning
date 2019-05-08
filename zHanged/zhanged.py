#!/bin/python3
# -*-coding:Utf-8 -*

from menu import *

infinit = 0

while infinit != 1:

    choice = menu()

    if choice == 1:
        menuSeeRules()

    if choice == 2:
        game()

    if choice == 3:
        scores()

    if choice == 4:
        menuQuit()