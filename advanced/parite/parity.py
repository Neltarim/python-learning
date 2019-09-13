#!/bin/python3
# coding:Utf-8

import analysis.csv as c_an     #lance le module csv.py dans le dir analysis
import analysis.xml as x_an     #pareil pour xml.py

import pdb                      #debugger python (comme GDB pour le C)
import argparse                 #permet le passage d'arguments


def parse_arguments():                          #defini les arguments possible
    parser = argparse.ArgumentParser()          #initie le parser d'arguments
    parser.add_argument("-e", "--extension",    #ajoute les arguments
    help="""Type of file to analyse. Is it CSV or XML?""")
    return parser.parse_args()                  #renvoie le parsing

def main():
    args = parse_arguments()
    pdb.set_trace()             #place un breakpoint avec pdb
    if args.extension == 'csv': #verifie l''argument passe en parametre
        c_an.launch_analysis('current_mps.csv')
    
    elif args.extension == 'xml':
        x_an.launch_analysis('SyceronBrut.xml')

if __name__ == "__main__":      #verifie que le script est lance seul ou en tant que module
    main()
else:
    print("importation success.")
