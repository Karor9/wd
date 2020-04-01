class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def __del__(self):
        print("Papa robaczku")
        
    def idz_w_gore(self, ile):
        self.y += ile * self.krok

    def idz_w_dol(self, ile):
        self.y -= ile * self.krok

    def idz_w_lewo(self, ile):
        self.x -= ile * self.krok

    def idz_w_prawo(self, ile):
        self.x += ile * self.krok

    def pokaz_gdzie_jestes(self):
        print(str(self.x) + " " + str(self.y)) 

bobak = Robaczek(0, 0, 1)
bobak.idz_w_gore(4)
bobak.pokaz_gdzie_jestes()
bobak.idz_w_dol(3)
bobak.pokaz_gdzie_jestes()
bobak.idz_w_lewo(2)
bobak.pokaz_gdzie_jestes()
bobak.idz_w_prawo(1)
bobak.pokaz_gdzie_jestes()