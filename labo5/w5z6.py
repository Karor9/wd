class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

tak = Wspak("To będzie wspak")

print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())
print(tak.__next__())

nie = Wspak("To")

print(nie.__next__())
print(nie.__next__())