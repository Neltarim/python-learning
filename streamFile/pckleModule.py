#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

import os
import pickle

os.chdir("/home/neltarim/python-learning/streamFile")

filePath = "/home/neltarim/python-learning/streamFile/shmekelz"

#importer et sauvegarder des objets dans un fichier avec le module pickle

score = {   #on cree un dico avec les scores
    "joueur 1": 5,
    "joueur 2": 35,
    "joueur 3": 40,
}

with open('shmekelz', 'wb') as my_file:
    my_pickler = pickle.pickler(my_file)

    #enregistrement ...

    my_pickler.dump(score) #on rajoute le tableau de score dans le fichier
