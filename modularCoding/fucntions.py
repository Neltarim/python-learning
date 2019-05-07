#!/bin/python3
# -*-coding:Utf-8 -*

def table(nb, max=10): #on met max 0 dix par defaut
    i = 0
    while i < max: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.

