# sayi1 = float(input("birinci sayıyı giriniz: "))
# sayi2 = float(input("İkinci sayyıyı giriniz: "))

# print(sayi1 > sayi2)

vize = float(input("vize notonu giriniz: "))
final = float(input("final notunu giriniz: "))

ortalama = (vize * 60 / 100) + (final * 40 / 100)

gecmeDurumu = ortalama > 50
print(ortalama)
print(gecmeDurumu)

