#1
class A:
    a = 100
    _a = 200 #указание другим программистам + не импортируется в import
    __a = 300

a = A()
print(a.a)
print(a._a)
#print(a.__a)

#2
class BankAccount:
    def __init__(self, name, accountNum, password):
        self.name = name
        self.accountNum = accountNum
        self.__password = password
        self.__balance = 0
    def setBalance(self, balance):
        self.__balance = balance
    def printBalance(self, password):
        if password == self.__password:
            print(self.__balance)
        else:
            print('Invalid password')

acc = BankAccount('Vasya', 243434, 1234)

acc.printBalance(3243)
acc.printBalance(1234)
acc.setBalance(3000)
acc.printBalance(1234)

#3
class PubPriv:
    def __privateMethod(self):
        print('PRIVATE')
    def publicMethod(self):
        print('PUBLIC')
        self.__privateMethod()

pp = PubPriv()
#pp.__privateMethods #закономерно ошибка
pp.publicMethod()

#4
class Car:

    def __init__(self, name, gasoline):
        self.__name = name
        self.__gasoline = gasoline

    def set_gasoline(self, gasoline):
        if gasoline > 0:
            self.__gasoline = gasoline
        else:
            print("Недопустимое количество бензина")

    def get_gasoline(self):
        return self.__gasoline

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Имя:", self.__name, "\tБензин:", self.__gasoline)


c = Car("Ford", 100)
c.set_gasoline(-1)
c.display_info()

c.set_gasoline(50)
c.display_info()












        
