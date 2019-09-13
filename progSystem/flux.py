#!/bin/python3
# -*-coding:Utf-8 -*

import sys
import os
import signal

sys.stdin #entree standard
sys.stdout #sortie standard
sys.stderr #erreur standard

#read and write pour lire les les flux standard

sys.stdout.write("test stdout\n")
#renvoie la string et le nombre de char a la ligne

fichier = open('sortie.txt', 'w')
sys.stdout = fichier
print("test...")
#ouvre un ficier et ecris la string
os.getcwd()

def shutdown_prog(signal, frame):
    print("Aller hop hop hop, ca degage")
    sys.exit(0)