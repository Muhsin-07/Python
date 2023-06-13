'''
#class
from typing import Self


class Person:
    # class attributes 
    adress = 'no information.'

    # consructor (Yapıcı Method)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
    # instance methods

    def intro(self):
        print('Hello There ' + self.name)
    
    def calculateAge(self):
        return 2023 - self.year 

#object (instance)
p1 = Person(name = 'Muhsin', year = 2001)
p2 = Person(name = 'Elif', year=  2003)

p1.intro()
p2.intro()

print(f"merhaba ben {p1.name} ve yaşım {p1.calculateAge()} yaşındayım.")
print(f"merhaba ben {p2.name} ve yaşım {p2.calculateAge()} yaşındayım.")
'''
from typing import Self

class Circle:
    # class attributes
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    # Methods
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return 2 * self.pi * (self.yaricap ** 2)

c = Circle()
c1 = Circle(6)

print(f"c1: Alan = {c.alanHesapla()} Çevre= {c.cevreHesapla()}")
print(f"c1: Alan = {c1.alanHesapla()} Çevre= {c1.cevreHesapla()}")