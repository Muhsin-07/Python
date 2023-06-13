import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)

df = pd.DataFrame(data, columns=["col1","col2","col3","col4","col5"])
result = df
result = df.columns # df.columns metodu ile tüm kolonları liste halinde görebiliriz.

result = df.head()
result = df.head(9) # df.head() metodu ilk 5 satırı almış oluruz. bunu arttırabilir veya azaltabiliriz, bunun için head()metoduna bir value değer göndermemiz lazım.

result = df.tail()  
result = df.tail(7) # df.tail() metodu son 5 satırı almış oluruz. bunu arttırabilir veya azaltabiliriz, bunun için tail()metoduna bir value değer göndermemiz lazım. 

result = df["col1"].head() # bu metod ile 'col1' kolonunun ilk 5 satırını almış oluyoruz.
result = df["col1"].tail() # bu metod ile 'col1' kolonunun son 5 satırını almış oluyoruz.
result = df[["col1", "col3"]].head() # bu şekilde col1 ve col3'e ait ilk beş satırdaki bilgiler yazdırılır.
result = df[5:15][["col1", "col3"]].head() # Bu durumda 5. satırddan başlar ve 9. satıra kadar yazdırır. Satır aralığını belirterek istediğimiz yerden bilgileri alabiliriz.

result = df > 50 # bu şekilde koşullar belirterek veriler üzerinde işlem yapabiliriz. dataFrame üzerinde 50'den büyük olan sayılar için True olamayanlar içinse Folse değerleri döner.
result = df[df > 50] 
result = df[df % 2 == 0] # bu şekilde belirtirsek eğer True-Folse yerine koşulu sağlayan veriler gösterilir, sağlamayanlar ise Nan olarak önümüze çıkar. 
result = df["col1"] > 50 # için sadece col1'e bakılır ve True-Folse değerleri gelir.
result = df[df["col1"] > 50] # dediğimizde col1'e bakar ve 50'den büyük olan her satırı kolon farketmeden col1 için uygun koşulu sağlayan tüm satırları getirir.
# bu durumu önlemek için:
result = df[df["col1"] > 50]["col1"] # diyebiliriz. bu durumda sadece col1'de koşulu sağlayan satırlar ekrana yazdırılır.
# başka kolonları da almak istersek eğer:
result = df[df["col1"] > 50][["col1","col3","col5"]] # diyerek gösterilecek kolon sayısını arttırabiliriz.

result = df[(df["col1"] > 50) & (df["col1"] <= 68)]["col1"] # burada col1 içerisnde 50'den büyük 70ten küçük veya eşit olan sonuçlar ekrana yazdırılır. ve operatörü yüzünden her iki koşulun da True değerini getirmesi gerekir.
result = df[(df["col1"] > 50) | (df["col1"] <= 68)]["col1"] # ya da operatörü ile ikisinden biri sağlanıyorsa ekrana yazdırılır.

result = df.query("col1 > 50 & col1 % 2 == 0") # query() metodu koşul belirtirken kullandığımız metoddur.
result = df.query("col1 > 50 & col4 % 2 == 0")[["col1","col4"]] # her iki koşul da True değerini return ettirdiği satırlar ekrana yazılır.
result = df.query("col1 > 50 | col2 % 2 == 0")[["col1","col2"]] # her iki koşuldan biri True değerini return ettirdiği satırlar ekrana yazılır. 


print(result)
