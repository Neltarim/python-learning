#!/bin/python3
# -*-coding:Utf-8 -*

def clearScreen():
    index = 0

    while index != 30:
        print()
        index += 1

def menu(): #affiche le menu et demande un choix a renvoyer dans infinit

    clearScreen()
    print("================== BIENVENUE AU zHANGED !!! ======================")
    print("******************************************************************")
    print("*                                                                *")
    print("*            1 : Afficher les regles du jeu                      *")
    print("*            2 : Nouvelle partie                                 *")
    print("*            3 : afficher les scores                             *")
    print("*            4 : Quitter le jeu                                  *")
    print("*                                                                *")
    print("******************************************************************")
    print('\n')

    choice = input("Votre choix : ")
    choice = int(choice) #on verifie  que l'input est un int

    if choice != 1 and choice != 2 and choice != 3:
        print("Choix invalide.") #on relance le menu en recursif si le joueur c'est trompe
        time.sleep(1)
        return menu() #retour recursif 
    else: #sinon on renvoie le choix dans infinit
        return choice

def menuSeeRules(): #affiche les regles du jeu
    key = str()

    clearScreen()
    print("======================== REGLES DU JEU =============================")
    print("********************************************************************")
    print("*                                                                  *")
    print("*    Les regles sont simples, la machine choisit un mot,           *")
    print("*    vous devez deviner le mot.                                    *")
    print("*    Mais attention : vous n'avez que 10 essaies possibles,        *")
    print("*    Au dela, vous passerez votre tete dans le noeud !             *")
    print("*                                                                  *")
    print("*  Bonne chance !                                                  *")
    print("*                                                                  *")
    print("********************************************************************")
    print('\n')
    
    time.sleep(3)
    key = input("Appuyer sur ENTER pour revenir au menu ... : ") #ferme les regles

    if key == "y": 
        return 0
    else: #maj pour any key a la place d'un yesno
        return 0

def menuQuit(): #quitte le programme
    yesno = str()

    print("Voulez vous vraiment quitter ? (y/n) : ", end='')
    yesno = input()

    print()

    if yesno == "y":
        print("A plus tard !")
        quit()
    else:
        print("Retour au menu .")
        return menu()