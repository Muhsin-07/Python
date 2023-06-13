# def yazdır(kelime , adet):
#     print(kelime * adet)

# yazdır("merhaba \n", 3)


# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)
        
#     return liste

# result = listeyeCevir("merhaba", 6, 8, 10)

# print(result)

# def asalsayibul(sayi1,sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)


# sayi1 = int(input("ilk sayı: "))
# sayi2 = int(input("ikinci sayı: "))

# asalsayibul(sayi1, sayi2)


def tambolenleribul(sayi):
    liste = []
    for i in range(2,sayi):
        if sayi % i == 0:
            liste.append(i)
    return liste

result = tambolenleribul(int(input("Tam bölenlerini bulmak istediğiniz sayı: ")))

print(result)