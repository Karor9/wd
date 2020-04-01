import random as r

plik = open("labo4/zadanie1.txt", "a+")

for x in range(1, 26):
    liczba = r.randint(1, 100)
    if liczba % 4 == 0: 
        plik.write(str(liczba))
        plik.write("\n")
        
plik.close        