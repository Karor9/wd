class Ciag:

    wartosci = []

    def __init__(self):
        self = self

    def wyswietl_dane(self):
        for x in range (0, len(self.wartosci)):
            print(self.wartosci[x], end= " ")
        print("\n")

    def pobierz_elementy(self, wartosci):
        self.wartosci = wartosci

    def pobierz_parametry(self, start, skok, ile):
        tab = []
        for x in range(0, ile):
            tab.append(start + x * skok)
        self.wartosci = tab    

    def policz_sume(self):
        suma = 0
        for x in range(0, len(self.wartosci)):
            suma += self.wartosci[x]
        return suma

    def policz_elementy(self, pierwszy, roznica):
        for x in range(0, 5):
            self.wartosci.append(pierwszy + x * roznica)



c1 = Ciag()
c1.pobierz_elementy([1, 2, 3, 4, 5])
c1.wyswietl_dane()
c2 = Ciag()
c2.pobierz_parametry(1, 3, 3)
c2.wyswietl_dane()
print(c2.policz_sume())
c3 = Ciag()
c3.policz_elementy(1, 3)
c3.wyswietl_dane()

