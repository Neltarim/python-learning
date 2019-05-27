#!/bin/python3
#-*-coding:Utf-8 -*


import signal
import sys

def quitProgram(signal, frame):
    
    print("A plus !")
    sys.exit(0)

#connexion du signal a la fonction:
signal.signal(signal.SIGINT, quitProgram)


print("Le programme va boucler....")

while True:
    continue

#arret du programme en tappant ctrl+c comme m'importe quel programme