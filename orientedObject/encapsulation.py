#!/bin/python3
#-*-coding:Utf-8 -*

class person:

    def __init__(self,name, lastName):
        
        self.name = name
        self.lastName = lastName
        self._whereFrom = "Paris" # '_' equivalent au private (mais ne bloque pas)

    def _get_from(self): #classique get

        print("acces a l'attribut from")
        return self._whereFrom

    def _set_from(self, newFrom): #classique set

        print("changement de from : {}".format(newFrom))
        self._whereFrom = newFrom #on modifie indirectement whereFrom


    whereFrom = property(_get_from, _set_from) #on definie whereFrom en property