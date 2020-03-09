from os import system as sc
from sys import argv

turn = int(argv[1])

while turn:
    sc("curl https://api.github.com/zen")
    print()
    turn -= 1