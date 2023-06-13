sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# for sayi in sayilar:
#     if sayi % 3 == 0 :
#         print(f"{sayi} sayısı 3'ün katıdır.")


# toplam = sum(sayilar)
# print(toplam)
'''
veya böyle de yapılabilir:

# toplam = 0
#for sayi in sayilar:
    toplam += sayi
    print("toplam: ", toplam)

'''

# for sayi2 in sayilar:
#     if sayi2 % 2 != 0:
#         print(sayi2**2)


# sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# for sehir in sehirler:
#     karakterSayisi = len(sehir)
#     if karakterSayisi <= 5:
#         print(sehir)


urunler = [ 
    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s7', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '6000'},
    {'name': 'samsung s10', 'price': '7000'}
]

# toplam = 0
# for urun in urunler:
#     fiyat = int(urun['price'])
#     toplam += fiyat

# print(f"Toplam ürün fiayat bilgisi: {toplam}")

for urun in urunler:
    if (int(urun['price'])) <= 5000:
        print(urun['name'])