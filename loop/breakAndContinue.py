#!/bin/python3
# -*-coding:Utf-8 -*

i = 1
while i < 20: # Tant que i est inférieure à 20

    if i % 3 == 0:
        i += 4 # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue # On retourne au while sans exécuter les autres lignes

    print("La variable i =", i)
    i += 1 # Dans le cas classique on ajoute juste 1 à i


while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break