import random

sayi = random.randint(1,6)
hak = int(input("hak sayınız: "))
puan = 100

while hak > 0:
    hak -= 1

    tahmin = int(input("tahmin : "))

    if tahmin == sayi:
        print(f"tebrikler {hak + (1)}. defada bildiniz. puanınız {100 - (puan/hak+1)}")
    elif tahmin < sayi:
        print("yukarı")
    else:
        print("aşağı")
        
    if hak == 0:
        print(f"hakkınız bitti tutulan sayı {sayi}")

    
