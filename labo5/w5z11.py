def fibbonaci(n):
    pomoc = 0
    liczba = 1
    x = 1
    yield liczba
    while (x < n):
        liczba, pomoc, x = liczba+pomoc, liczba, x+1
        yield liczba

for liczba in fibbonaci(10):
    print(liczba) 