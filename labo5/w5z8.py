class Samo:
    index = 0
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.ln = 0
        if isinstance(self.data, str):
            self.ln = len(data)
        else:
            pass

    def __iter__(self):
        return self

    def __next__(self):
        if Samo.index > self.ln or self.ln == 0:
            raise StopIteration
        if self.data[Samo.index] == "a" or self.data[Samo.index] == "e" or self.data[Samo.index] == "u" or self.data[Samo.index] == "i" or self.data[Samo.index] == "ą" or self.data[Samo.index] == "ę" or self.data[Samo.index] == "y" or self.data[Samo.index] == "ó" or self.data[Samo.index] == "o": 
            Samo.index += 1
            return self.data[Samo.index-1]
        else:
            Samo.index += 1
            pass

tak = Samo("abcdef")
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())

nie = Samo(13214)
print(nie.__next__())



