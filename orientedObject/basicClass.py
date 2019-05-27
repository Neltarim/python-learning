#!/bin/python3
# -*-coding:Utf-8 -*

#creeer un classe de base:

class Personne:
    """Classe definissant une personne
    attributs :
    -son prenom
    -son nom
    -son age
    -son lieu de residence"""

    def __init__(self, lastName, name): #constructeur
        self.lastName = lastName
        self.name = name
        self.age = 20
        self.whereFrom = "Paris"

        #appel : perso = Personnage("lastName", "name")

    def who(self):
        print("Je suis {} {}, j'ai {} ans et je viens de {}.".format(self.name, self.lastName,self.age,self.whereFrom))



#les methodes CLS ....

class Count:
    """sert a rien masi tg on s'en fout"""

    objectsCreated = 0 #compteur d'objet

    def __init__(self):
        """a chaques instance, on compte"""
        Count.objectsCreated += 1 #ca me manque le ++ ...

    def howMany(cls):
        print("{} objets ont ete crees.".format(cls.objectsCreated))
    howMany = classMethod(howMany)

    #CLS definit la classe de l'objet et non son instance
    #elle peut donc compter le nombre de fois ou on instancie
    #un objet de la classe (entre autre)