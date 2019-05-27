#!/bin/python3
# -*-coding:Utf-8 -*

from menu import *
import pickle
import time

def game():

    word = randWord()
    lenWord = word.len()
    hidenWord = hide(lenWord)


    print("====================== zHANGED ============================")
