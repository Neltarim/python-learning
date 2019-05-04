#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

my_str = "hello world"

for letter in my_str: #ecrit toute la chaine
    print(letter)

for letter in my_str: #n'ecrit que les voyelles 
    if letter in "AEYOUIaeyoui":
        print(letter)
    else:
        print('*')