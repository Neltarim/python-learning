#!/bin/python3
#-*-coding:Utf-8 -*

import argparse

parser = argparse.ArgumentParser() #on cree le parser d'args

#ajouter un argv
parser.add_argument("x", help="description")

parser.parse_args()
