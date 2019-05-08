#!/bin/python3
# -*-coding:Utf-8 -*

import os
import pickle

#os.chdir("/home/neltarim/python-learning/streamFile")

filePath = "/home/neltarim/python-learning/streamFile/shmekelz"

#importer et sauvegarder des objets dans un fichier avec le module pickle

score = {   #on cree un dico avec les scores
    "joueur 1": 5,
    "joueur 2": 35,
    "joueur 3": 40,
}

money = {
    "joueur 1": 8000,
    "joueur 2": 5600,
    "joueur 3": 3450,
}

with open("shmekelz", "wb") as my_file: #ouvre le fichier en write binary
    my_pickler = pickle.Pickler(my_file) #OUBLIE PAS LA MAJ A PICKLER

    #enregistrement:

    my_pickler.dump(score) #on rajoute le tableau de score dans le fichier
    my_pickler.dump(money) #on peut en mettre plusieurs

#recuperer les objets:

with open("shmekelz", "rb") as my_file: #on ouvre en read binary
    my_unPickler = pickle.Unpickler(my_file)

    #lecture :

    score_grabbed = my_unPickler.load()
    money_grabbed = my_unPickler.load()
    #on grab deux fois dans l'ordre pour recuperer les dicos
