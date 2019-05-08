#!/bin/python3
# -*-coding:Utf-8 -*

import os

os.chdir("/home/neltarim/python-learning/streamFile") #definie un chemin d'acces
os.getcwd() #affiche le chemin d'acces actuel

path = "/home/neltarim/python-learning/streamFile/fichier.txt"

#mode d'ouverture de fichiers :
# 'r' read only
# 'w' supprime l'actuel fichier, en cree un et ecrit dedans
# 'a' ouvre le fichier en ecrivant a la fin (sans supprimer le contenu donc)
# 'b' ouvre le fichier en binaire


my_file = open(path, "r") #ouvre fichier.txt 

contenu = my_file.read() #stock le contenu du fichier dans une string
print(contenu)

#note : si il y a des return lines dans le fichier, la string contiendra des \n

my_file.close() #ferme le fichier


my_file = open(path, "w")
my_file.write("nouvelle chaine\n") #ecrit par dessus le fichier
my_file.close()

my_file = open(path,"a")
my_file.write("deuxieme chaine")
my_file.close()

#ouverture safe:

with open(path, "r") as new_file: #with permet de fermer le fichier if except
    text = new_file.read()  #lis  le fichier
