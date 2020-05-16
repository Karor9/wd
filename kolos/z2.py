def odwroc(s):
    lista = s.split()
    lista2 = s.split()
    wynik = ""
    for x in range(0, len(lista)):
        slowo = ''.join(reversed(lista[x]))
        wynik += slowo + " "
    print(wynik)

st = "Ala ma kota"
odwroc(st)