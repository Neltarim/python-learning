#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

import os

os.chdir("/home/netlarim/python-learning/streamFile") #definie un chemin d'acces
os.getcwd() #affiche le chemin d'acces actuel

path = "/home/neltarim/python-learning/streamFile/fichier.txt"

#mode d'ouverture de fichiers :
# 'r' read only
# 'w' supprime l'actuel fichier, en cree un et ecrit dedans
# 'a' ouvre le fichier en ecrivant a la fin (sans supprimer le contenu donc)
# 'b' ouvre le fichier en binaire


my_file = open(path, "r") #ouvre fichier.txt 
