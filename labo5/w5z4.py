
class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstuktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point()
print(p1.counter)
p2 = Point(1, 2)
print(p2.counter)
p3 = Point(3, 1)
print(p3.counter)

p1.update(4)

print(p1.counter)
print(p2.counter)
print(p3.counter)

p1.counter = [5]

print(p1.counter)
print(p2.counter)
print(p3.counter)