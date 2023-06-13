#class
class Person:
    pass
    # class attributes 
    adress = 'no information.'

    # consructor (Yapıcı Method)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı.")
        # methods

#object (instance)
p1 = Person(name = 'muhsin', year = 2001)
p2 = Person(name = 'Elif', year=  2003)

# uppdating
p1.name = 'Demir'
p1.adress = 'Siirt/Merkez'
p2.adress = 'Adıyaman/Gölbaşı'

# accsesing object attributes
print(f"p1:name: {p1.name} year: {p1.year} adres: {p1.adress}")
print(f"p2:name: {p2.name} year: {p2.year} adres: {p2.adress}")

print(p1)
print(p2)