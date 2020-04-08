class Kwadrat:
    def __init__ (self, x):
        self.x = x

    def __lt__(self, other):
        if self.x<other.x:
            return "Pierwszy kwadrat jest mniejszy niż drugi"
        else:
            return "Pierwszy kwadrat nie jest mniejszy niż drugi"

    def __gt__(self, other):
        if self.x>other.x:
            return "Pierwszy kwadrat jest większy niż drugi"
        else:
            return "Pierwszy kwadrat nie jest większy niż drugi"

    def __le__(self, other):        
        if self.x<=other.x:
            return "Pierwszy kwadrat jest mniejszy lub równy drugiemu"
        else:
            return "Pierwszy kwadrat jest większy niż drugi"

    def __ge__(self, other):
        if self.x>=other.x:
            return "Pierwszy kwadrat jest większy lub równy drugiemu"
        else:
            return "Pierwszy kwadrat jest mniejszy niż drugi"

kw1 = Kwadrat(6)
kw2 = Kwadrat(5)
kw3 = Kwadrat(5)
kw4 = Kwadrat(4)

print(Kwadrat.__lt__(kw1, kw2))
print(Kwadrat.__gt__(kw2, kw3))
print(Kwadrat.__le__(kw3, kw2))
print(Kwadrat.__ge__(kw4, kw1))
