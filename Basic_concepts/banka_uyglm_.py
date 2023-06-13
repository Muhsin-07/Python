sadikhesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '1324568',
    'bakiye': 3000,
    'ekHesap': 2000
}

alikhesap = {
    'ad': 'Ali Turan',
    'hesapNo': '1245568',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']} ")

    if (hesap['bakiye']) >= miktar:
        hesap['bakiye'] -= miktar
        print("Paranızı Abilirsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = input("ek hesap Kullanılsın mı (e\h): ")
            if ekHesapKullanimi == 'e':
                ekHesapKullanıalcakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanıalcakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda ek hesap ile birlikte toplam {toplam} TL bakiye bulunmaktadır.")
        else:
            print(f"Toplam bakiyeniz ek hesap ile birlikte {toplam} TL'dir. Lütfen limitler dahilinde işlem yapınız.")
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} Tl bulunmaktadır. ek hesap limitiniz ise {hesap['ekHesap']} TL'dir.")


paraCek(sadikhesap, 3000)
print("***********************")
paraCek(sadikhesap, 1600)
