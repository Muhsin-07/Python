message = "Hello There. My name is Muhsin Demir"

# message = message.upper()       # upper metodu str olan içeriğin tüm haerfleini büyük oalrak yazar.
# message = message.lower()       # lower metodu da tüm karakterleri küçük yapar.
# message = message.title()       # title ise tüm kelimelerin ilk harfini büyük yapar.
# message = message.capitalize()  # bu metod ise sadece cümlenin ilk harffini büyük yapar.
# message = message.strip()       # strip metodu ise cümlenin başında veya sonunda boşluk varsa siler.
# message = message.split()       # split metodu ise cümlenin her bir kelimesini (boşlukları kullanarak) kelimelere ayırır ve liste olarak önümüze sunar.
# message = message.split('.')    # parantez içine cümleyi ne kullanarak ayırmak istiyorssak ekleyip ona göre ayırabiliriz.
# message = ' '.join(message)       # split metodunun tersine birleştirme işlemi yapar = '---' boşluk yerine bunları da ekleyip her birleştirmeden sonra üç tane çizgi eklemesini sağlayabiliriz.
# print(message)



# index = message.find("Muhsin")
# print(index)
# find metodu ile cümle içinden bir karakteri veya kelimeyi arayabiliriz 
# print ile indexi yazdırınca önümüze 24 çıkıyor bu da Muhsin kelimesinin ilk harfinin 24. index numarasında olduğunu belirtiyor
# cümle içinde aradığımız kelimeyi bulamazsa sonuç -1 olarak önümüze çıkar.



# isFound = message.startswith("H")
# print(isFound)
# bu metod ile str ifademizin H ile başlayıp başlamadığına bakarız. ifade H ile başlıyorsa sonuç True olarak önümüze çıkar.



# isFound = message.endswith("r")
# print(isFound)
# bu metod ile str ifademizin r ile bitip bitmediğne bakarız. ifade r ile bitiyorsa sonuç True olarak önümüze çıkar.



# message = message.replace("Muhsin", "Elif")
# print(message)
# replace metodu ile str ifademizdeki kelimeleri veya karakterleri değiştirebiliriz. 
# örneğin:
            # message = message.replace("ç","c").replace("i","ı").replace(" ","*")



# message = message.center(100, "*")
# print(message)
# center metodu ifademizi alır ve belirttiğimiz uzunluktaki bir satıra ortalar 
# virgül diyip tırnak içinde bir şey yazarsak eğer de bıraktığı boşlukların yerini onla doldurur.

