class Slowa:
    def __init__(self, slowo1, slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2

    def sprawdz_czy_palindrom(self, slowo):
        slowo.lower()
        for x in range(0, len(slowo)):
            if slowo[x] != slowo[-1 + x * -1]:
                return "Nie"
        return "Tak"

    def wyswietl_wyrazy(self):
        print(self.slowo1 + " " + self.slowo2)

    def sprawdz_czy_metagramy(self):
        ileRoznych = 0
        for x in range(0, len(self.slowo1)):
            if(self.slowo1[x] != self.slowo2[x]):
                ileRoznych += 1
            if(ileRoznych>1):
                return "Nie"
        return "Tak"

    def sprawdz_czy_anagramy(self):
        kopia1 = list(self.slowo1)
        kopia2 = list(self.slowo2)
        for x in self.slowo1:
            for y in kopia2:
                if x == y:
                    kopia1.remove(x)                    
                    kopia2.remove(y)
                    break
        if kopia1 == kopia2:
            return "Anagram"
        return "Nie anagram"

k = Slowa("kajak", "jakka")
print(k.sprawdz_czy_palindrom(k.slowo1))
print(k.sprawdz_czy_palindrom(k.slowo2))
k.wyswietl_wyrazy()
print(k.sprawdz_czy_metagramy())
print(k.sprawdz_czy_anagramy())
