#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

year =input("Pick a year : ")

try:
    year = int(year)
    assert year > 0

except ValueError:
    print("a year please, you fckin morron...")
except AssertionError:
    print("Diid you ever seen a negative year ? oh wait...")