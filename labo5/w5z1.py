class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        
    def wyswietl_nazwe(self):
        print(self.rodzaj)

class Ubrania(Material):
    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
        Material.__init__(self, rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print(self.rozmiar + " " + self.kolor + " " + self.dla_kogo) 

class Sweter(Ubrania):
    def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo, rodzaj_swetra):

        Ubrania.__init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo)
        self.rodzaj_swetra = rodzaj_swetra
        
    def wyswietl_dane(self):
        print(self.rodzaj + " " + str(self.dlugosc) + " " + str(self.szerokosc) + " " + self.rozmiar + " " + self.kolor + " " + self.dla_kogo + " " + self.rodzaj_swetra)

koszulka = Ubrania("T-Shirt", 1.4, 0.8, "XL", "Czerwony", "Męska")
koszulka.wyswietl_dane()
akryl = Material("Akryl", 6, 2)
akryl.wyswietl_nazwe()
sweter = Sweter(akryl.rodzaj, akryl.dlugosc, akryl.szerokosc, "L", "Zółty", "Damski", "z golfem")
sweter.wyswietl_dane()