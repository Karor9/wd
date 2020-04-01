class Ciag:
    def __init__(self, wartosci):
        self.wartosci = wartosci

    def wyswietl_dane(self):
        for x in range (0, len(self.wartosci)):
            print(self.wartosci[x], end= " ")

c1 = Ciag([1, 2, 3, 4, 5, 6])
c1.wyswietl_dane()