#!/bin/python3
# -*-coding:Utf-8 -*

from menu import * #on importe les modules de menu et jeu
from game import *

infinit = 1 #sert simplement a creer une boucle innfinie pour le reload de menu/jeu etc

while infinit == 1:

    choice = menu() #on affiche le menu et demande quoi faire

    if choice == 1: #option1 : on affiche les regles
        menuSeeRules()

    if choice == 2: #option2 : on lance le jeu
        game()

    if choice == 3: #option3 : on  quitte le jeu
        MenuQuit()
