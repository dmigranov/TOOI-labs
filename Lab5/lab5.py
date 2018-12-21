import unittest
import random



#1
def subtract(a, b):
    c = a - b
    return c
def triple(a):
    return [a-1, a, a+1]

#3
def isDate(s):
    list = s.split()
    
    for l in list:
        if l.isdigit():
            number = l
    nindex = list.index(number)

    if list[nindex + 1] == "году" or list[nindex + 1] == "год" or list[nindex + 1] == "г" or list[nindex + 1] == "года" :
        return True
    elif list[nindex + 1] == "век" or list[nindex + 1] == "веке" or list[nindex + 1] == "века" or list[nindex + 1] == "лет" :
        return True
    elif "январ" in list[nindex + 1] or "феврал" in list[nindex + 1] or "март" in list[nindex + 1] or "апрел" in list[nindex + 1]:
        return True
    elif "эры" in list [nindex + 1:]:
        return True
    return False

print(isDate("В 2015 году всё хорошо"))




class MyTest(unittest.TestCase):
    #2
    def test_rand(self):
        for i in range(0,10):
            with self.subTest(i=i):
                self.assertGreaterEqual(random.random(), 0.5)
    #раскомментить
    def test_equal(self):
        self.assertTrue(subtract(3,6) == -3)
    def test_notequal(self):
        self.assertFalse(subtract(7,7) != 0)
    def test_in(self):
        self.assertIn(2, triple(2));
    def test_notin(self):
        self.assertNotIn(4, triple(2));
    def test_greater(self):
        self.assertGreater(4, subtract(4,1));
    def test_less(self):
        self.assertLess(4, subtract(5,0.5));
    def test_count(self):
        self.assertCountEqual(triple(4), [4,3,5])
    def test_date(self):
        self.assertTrue(isDate("с тех пор прошло 3 года"))
        self.assertTrue(isDate("бюджет в 2018 году"))
        self.assertTrue(isDate("в 6 веке"))
        self.assertTrue(isDate("5 марта"))
        self.assertTrue(isDate("почти половина мужчин не доживают до 65 лет"))
        self.assertTrue(isDate("в 1897 г"))
        self.assertTrue(isDate("1978 до нашей эры"))
        self.assertTrue(isDate("в мае 2018 года"))


if __name__ == '__main__':
    unittest.main()
