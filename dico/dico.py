#!/bin/python3
# -*-coding:Utf-8 -*

dico = {} #initie un dico vide

#ajouter un nouvelle clef et sa valeur dans le dico:
dico["pseudo"] = "Prolixe"
dico["password"] = "*"



echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# ... Seconde ligne des blancs


#on peuut aussi mettre une string en clef
placard = {"chemise":3, "pantalon":6, "tee-shirt":7}

#supprimer une valeur:
del placard["chemise"]

#supprimer la valeur ET la clef:
placard.pop("chemise")

#parcourir les clefs:
fruits = {"pommes":21, "melons":3, "poires":31}
for cle in fruits.keys():
    print(cle)


#parcourir les valeurs:

for valeur in fruits.values():
    print(valeur)

#trouver une valeur en particulier:
if 21 in fruits.values():
    print("un des fruits est dans la quantite 21.")

#parcourir les deux en meme temps:
for  cle, valeur in fruits.items():
    print("la cle {} contient la valeur {}".format(cle, valeur))