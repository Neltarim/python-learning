#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

from menu import * 
import random
import time

def pairOrNot(nbr):
    if (nbr % 2 == 0):
        return 1
    else:
        return 0

def cmpPairImpair(nb1, nb2):
    if pairOrNot(nb1) == pairOrNot(nb2):
        return 1
    else:
        return 0

def lost():
    clearScreen()
    yesno = str()
    print(" Dommage vous n'avez plus d'argent ....")
    print(" Vous voyez les videurs arriver au loin")
    print(" Cependant, votre voisin de table vous propose de vous redonner ")
    print(" un petit pecul pour rejouer.")
    print("     Accepter l'argent et rejouer ? (y/n) : ", end='')
    yesno = input()

    if  yesno == "y":
        game(500)
    else:
        print(" Retour au menu ...")
        time.sleep(2)
        return 0

def game(money = 1000):
    pary = 0
    bet = 0
    wheel = 0
    yesno = str()

    if money <= 0:
        lost()


    clearScreen()
    print("==================== Roulette ========================")
    print( "    Il vous reste ", money, "$")
    print('\n')
    print("     Les paris sont ouverts !")
    print(" Votre mise : ", end='')
    bet = int(input())

    print()
    print(" Sur quelle case pariez vous ? : ", end='')
    pary = int(input())
    print()

    print("     Les jeux sont faits, rien ne va plus !!!")
    print()
    print(" La bille tombe sur ............ ", end='')
    wheel = random.randrange(50)
    time.sleep(1)

    print(wheel, " !!!")

    if pary == wheel:
        print(" Wow perfect shot !! Vous recuperez donc ", (bet * 3), "$ !")
        money += bet * 3
    elif cmpPairImpair(pary, wheel) == 1:
        print(" Couleur ! Vous recuperez donc ", (bet * 2), "$ .")
        money += bet * 2
    else:
        print(" Dommaaaaage ... vous perdez donc ", bet, "$ ...")
        money -= bet

    if money <= 0:
        lost()

    print(" Quitter la table et repartir avec vos gains ? (y/n) : ", end='')
    yesno = input()
    print()

    if yesno == "y":
        print("     Merci d'avoir joue !")
        time.sleep(2)
        return 0
    else:
        return game(money)