#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

import time


def clearScreen(): #nettoie jsute le terminal
    i = 0

    while i <= 30:
        print('\n')
        i += 1


def menu(): #affiche le menu et demande un choix a renvoyer dans infinit

    clearScreen()
    print("================== BIENVENUE AU zCASINO !!! ======================")
    print("******************************************************************")
    print("*                                                                *")
    print("*            1 : Afficher les regles du jeu                      *")
    print("*            2 : Nouvelle partie                                 *")
    print("*            3 : Quitter le jeu                                  *")
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
    yesno = str()

    clearScreen()
    print("======================== REGLES DU JEU =============================")
    print("********************************************************************")
    print("*                                                                  *")
    print("* tout d'abord, le joueur choisit un nombre, la roulette choisit,  *")
    print("* ensuite un nombre. Si ce nombre est le meme, le joueur triple    *")
    print("* sa mise de depart. Si il est de la meme couleur (pair ou impair) *")
    print("* alors il double sa mise. Sinon , il perd sa mise .               *")
    print("*                                                                  *")
    print("*  Messieurs, faites vos jeux !                                    *")
    print("*                                                                  *")
    print("********************************************************************")
    print('\n')
    
    time.sleep(3)
    yesno = input("Revenir au menu ? (y/n) : ") #ferme les regles

    if yesno == "y": #termine la fonction et renvoie vers infinit
        return 0
    elif yesno == "n": #relance en recursif les regles si non
        return menuSeeRules()
    else:  #gestion d'erreurs de frappes
        print("Choix invalide .")
        time.sleep(1)
        return menuSeeRules()

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