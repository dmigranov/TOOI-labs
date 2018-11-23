#1
class Things:
    def __init__(self,n,t):
        self.namething = n
        self.total = t
        self.color = 'black'
        
th1 = Things("table", 5)
th2 = Things("computer", 7)

print (th1.namething, th1.total) 
print (th2.namething, th2.total)

th1.color = "green"

print (th1.color) 
print (th2.color)


#2
class Table:
    def __init__(self,l,w,h):
        self.long = l
        self.width = w
        self.height = h
    def outing(self):
        print (self.long,self.width,self.height)
class Kitchen(Table):
    def howplaces(self,n):
        if n < 2:
            print ("It is not kitchen table")
        else:
            self.places = n
    def outplases(self):
        print (self.places)
class Chair(Table): #стул - подкласс стола
    def setMaterial(self, material):
        self.material = material
    def printMaterial(self):
        print (self.material)

t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
t_2 = Table(1,3,0.7)
t_2.outing()
t_3 = Chair(0.5,0.5,1)
t_3.setMaterial("Iron")
t_3.printMaterial()

print("----------------------------")
import math
#3
class Figure:
    color = "white"
    def setColor(self, color):
        self.color = color
    def showParams(self):
        pass


class Oval(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def showParams(self):
        print(self.color, "ellipse with axes of", self.a, "and", self.b, "and area of", math.pi * self.a * self.b)

class Square(Figure):
    def __init__(self, a):
        self.a = a
    def showParams(self):
        print(self.color, "square with side of", self.a, "and area of", self.a * self.a )




o = Oval(3,2)
o.showParams()
s = Square(3)
s.setColor('green')
s.showParams()

print("----------------------------")

#4

class Company:

    def __init__(self):
        self.workers = list()

    def addWorker(self, worker):
        self.workers.append(worker)
    def printAll(self):
        for worker in self.workers:
            worker.printInfo()

class Worker:
    def __init__(self, name, wage):
        self.wage = wage
        self.name = name
    def printInfo(self):
        print(self.name, 'earns', self.wage, 'rubles')
    def changeWage(self, wage):
        self.wage = wage


class Director(Worker):
    def __init__(self, name, wage):
        if wage < 100000:
            raise Exception('THE WAGE IS TOO SMALL!!!')
        self.wage = wage
        self.name = name
    def changeWage(self, wage):
        self.wage += wage #потому что директор!

company = Company()
w1 = Worker('Vasya Krutoi', 15000)
#w1.changeWage(10000)
d1 = Director('Ivan Ivanov', 150000)
d1.changeWage(100000)

company.addWorker(w1)
company.addWorker(d1)

company.printAll()









