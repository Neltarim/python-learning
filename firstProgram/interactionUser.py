#!/bin/python3
# -*-coding:Utf-8 -*

year = input("Saisissez une annee : ") #on demande l'annee 
year = int(year) #on interdit autre chose qu'un int

bissextile = False #on cree un bool

if year % 400 == 0: #pas un poit virgule mais deux point !!
    bissextile = True

elif year % 100 == 0: #elif et pas else if
    bissextile = False

elif year % 4 == 0:
    bissextile = True

else:
    bissextile = False


if bissextile:
    print("L'anne est bissextile")
else:
    print("L'anne n'est pas bissextile")