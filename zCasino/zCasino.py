#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

from menu import *
from game import *
import random
import time

infinit = 0

while infinit == 0:

    choice = menu()

    if choice == 1:
        menuSeeRules()

    if choice == 2:
        game()

    if choice == 3:
        MenuQuit()
