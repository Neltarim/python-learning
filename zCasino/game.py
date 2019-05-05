#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

from menu import * 
import random
import time

def pairOrNot(nbr): #renvoie 1 si pair, sinon renvoie 0
    if (nbr % 2 == 0):
        return 1
    else:
        return 0

def cmpPairImpair(nb1, nb2): #renvoie 1 si les deux nbr sont pairs ou impairs
    if pairOrNot(nb1) == pairOrNot(nb2):
        return 1
    else:
        return 0 #si non, renvoie 0

def lost(): #si le joueur n'a plus d'argent
    
    clearScreen()
    yesno = str()
    print(" Dommage vous n'avez plus d'argent ....")
    print(" Vous voyez les videurs arriver au loin")
    print(" Cependant, votre voisin de table vous propose de vous redonner ")
    print(" un petit pecul pour rejouer.")
    print("     Accepter l'argent et rejouer ? (y/n) : ", end='')
    yesno = input()

    if  yesno == "y": #si le joueur veut rejouer, relance le jeu avec 500 $
        game(50)
    else: #sinon, retourne dans la boucle infinit
        print(" Retour au menu ...")
        time.sleep(2)
        return 0

def game(money =250): #boucle de jeu
    pary = 0    #le pari du joueur
    bet = 0     #sa mise
    wheel = 0   #le rand number
    yesno = str()

    if money <= 0: #juste au cas ou
        lost()


    clearScreen()
    print("==================== Roulette ========================")
    print( "    Il vous reste ", money, "$")
    print('\n')
    print("     Les paris sont ouverts !")
    print(" Votre mise : ", end='')
    bet = int(input()) #on demande la  mise du joueur
    print()

    if bet > money:
        print("Vous n'avez pas assez d'argent ...")
        time.sleep(1)
        return game(money)
    if bet <= 0:
        print("Le croupier vous regarde d'un air etrange ...")
        time.sleep(1)
        return game(money)

    print(" Sur quelle case pariez vous ? : ", end='')
    pary = int(input()) #la case sur laquelle il veut parier
    print()

    if pary > 50 or pary < 0:
        print("Il n'y a que 50 cases monsieur.")
        time.sleep(1)
        return game(money)

    print("     Les jeux sont faits, rien ne va plus !!!")
    print()
    print(" La bille tombe sur ............ ", end='')
    wheel = random.randrange(50) #on genere un nombre rand entre 1 et 50
    time.sleep(1)

    print(wheel, " !!!")

    if pary == wheel: #si le pari est bon alors on triple la mise
        print(" Wow perfect shot !! Vous recuperez donc ", (bet * 3), "$ !")
        money += bet * 3
    elif cmpPairImpair(pary, wheel) == 1: #si il y a une couleur on double la mise
        print(" Couleur ! Vous recuperez donc ", (bet * 1.5), "$ .")
        money += bet * 2
    else: #sinon on prend sa mise
        print(" Dommaaaaage ... vous perdez donc ", bet, "$ ...")
        money -= bet

    if money <= 0: #si le joueur  n'a plus un rond, on lance la fonction lost
        lost()

    print(" Quitter la table et repartir avec vos gains ? (y/n) : ", end='')
    yesno = input() #rejouer ou non
    print()

    if yesno == "y": #renvoie vers infinit
        print("     Merci d'avoir joue !")
        time.sleep(2)
        return 0
    else:
        return game(money) #sinon, relance la game en recursif avec l'argent gagne ou perdu