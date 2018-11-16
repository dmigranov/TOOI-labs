import math


#1
print("#1")
class Box:
    figures = []

    def addFigure(self, fig):
        self.figures.append(fig)

    def printBox(self):
        for f in self.figures:
            if isinstance(f, Circle):
                print("Circle of radius", f.radius, "and area of", f.area)
            elif isinstance(f, Square):
                print("Square with side of", f.a, "and area of", f.area)
            elif isinstance(f, Rectangle):
                print("Rectangle with sides of", f.a, "and", f.b, "and area of", f.area)
            elif isinstance(f, Triangle):
                print("Triangle with sides of", f.a, "and", f.b, "and", f.c, "and area of", f.area)

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * radius * radius

class Square:

    def __init__(self, a):
        self.a = a
        self.area = a * a

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area = a * b

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        p = (a+b+c)/2
        self.area = math.sqrt(p * (p-a) * (p-b) * (p-c))


box = Box()
box.addFigure(Circle(3))
box.addFigure(Square(4))
box.addFigure(Rectangle(4, 3))
box.addFigure(Triangle(3, 4, 5))
box.printBox()

print("#2")

#2
class Zone:
    def __init__(self, price):
        self.price = price

class City:
    def __init__(self, zone):
        self.zone = zone

class Ticket:
    def __init__(self, whence, whither, isCoupe):
        self.whence = whence
        self.whither = whither
        self.isCoupe = isCoupe
        if whence.zone == whither.zone:
            self.price = whence.zone.price
        else:
            self.price = whence.zone.price + whither.zone.price
        if isCoupe:
            self.price *= 1.25



Siberia = Zone(300)
Novosibirsk = City(Siberia)
Omsk = City(Siberia)
ticket1 = Ticket(Novosibirsk, Omsk, True)
print(ticket1.price)
Ural = Zone(400)
Ekaterinburg = City(Ural)
ticket2 = Ticket(Novosibirsk, Ekaterinburg, False)
print(ticket2.price)



        
