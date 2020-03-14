x = input("Podaj liczbę nie większą niż 10")
x = int(x)
x += 1
for liczba in range(x):
    for iloscA in range(liczba):
        print("A", end='')
    print()
