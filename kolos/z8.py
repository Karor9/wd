slowo = "zgadujemy"
zgadniete = []
for litera in slowo:
    zgadniete.append("_")
gra = True
while(gra):
    zgaduj = ""
    for x in range(0, len(slowo)):
        zgaduj = zgaduj + zgadniete[x]
    print(zgaduj)
    literka= str(input('podaj literę, którą chcesz odgadnąć: '))
    if literka == "@":
        slowko= str(input('Podaj haslo: '))
        if slowo == slowko:
            print("Wygrałeś!")
            gra = False
            break
        else:
            print("Hasło nieprawidłowe")
    for x in range(0, len(slowo)):
        if slowo[x] == literka:
            zgadniete[x] = literka

