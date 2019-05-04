#!/home/neltarim/Download/python3
# -*-coding:Utf-8 -*

try: 
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateu =r ou denomiateur n'a pas ete definie")
except TypeError:
    print("un des variables pssede un type incompatible")
except ZeroDivisionError:
    print("you're trying to divide by zer.... OH SHIIIIII-")

#on peut aussi capturer l'exception et la display:
except TypeError as exceptions:
    print("Erreur : ", exceptions)

else:
    print("Le resultat est : ", resultat)

finally:
    input("Press ENTER to quit ... ")