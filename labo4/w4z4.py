class NaZakupy:
    def __init__(self, nazwa, ile, miara, cena):
        self.nazwa_produktu = nazwa
        self.ilosc = ile
        self.jednostka_miary = miara
        self.cena_jed = cena

    def wyswietl_produkt(self):
        print(self.nazwa_produktu + " " + self.jednostka_miary + " " + str(self.cena_jed) + "zł")

    def ile_produktu(self):
        print(str(self.ilosc) + " " + self.jednostka_miary)
         
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed


Ziemniak = NaZakupy("Ziemniaki", 3, "kg", 2.34)
Ziemniak.wyswietl_produkt()
Ziemniak.ile_produktu()
print(Ziemniak.ile_kosztuje())