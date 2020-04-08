class Kwadrat:
    def __init__ (self, x):
        self.x = x

    def __add__(nr1, nr2):
        y = nr1 + nr2
        return Kwadrat(y)


kw1 = Kwadrat(6)
kw2 = Kwadrat(4)
kw3 = Kwadrat.__add__(kw1.x, kw2.x)
print(kw3.x)