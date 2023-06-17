import pandas as pd
import numpy as np

data = {
    "col1":[1,2,3,4,5],
    "col2":[14,26,37,90,14],
    "col3":["ali","mehmet","muhsin","demir","elif"]
}

df = pd.DataFrame(data)
result = df

result = df["col2"].unique() # .unique() metodu tekrarlayan elemanları temizler ve col2'de bulunan değerleri liste halinde ekrana yazdırı
result = df["col2"].nunique() # listenin eleman sayısını verir.
result = df["col2"].value_counts() # her bir değeri ve kaç defa tekrar edildiğini yazdırır.
result = df["col1"] * 2 # her bir elemanı 2 ile çarpılır ve sonuçlar ekrana yazdırılır. ancak bunu bir metod kullanarak ta yapabiliriz. bunun için öncelikle bir fonksiyon (def) oluşturmalıyız.

def kareal(x):
    return x * x

result = df["col1"].apply(kareal) # burada oluşturduğumuz fonk. apply metodu ile çağırıp istediğimiz işlemi yaptırabiliriz.
# ancak çağırdığımız fonk.'a parametre göndermiyoruz. apply metodu ile listede bulunan her eleman fonk.'a gönderilir ve cevap return edilerek konsola yazdırılır.

kareal2 = lambda x: x * x
result = df["col1"].apply(kareal2) # bunu lamda fonk. ile de yapabiliriz.
result = df["col1"].apply(lambda x: x * x) # fonk. oluşturmadan da parametreleri .apply metoduna ekleyebiliriz. sonuç değişmez. 
result = df["col3"].apply(len) # normal python metodlarını da ekleyerek bir çok işlemi yapabiliriz. örneğin burada 'len' ile her bir değerin karakter sayısını almış olduk. 
df["karakterSayisi"] = df["col3"].apply(len) # karakterSayisi adında bir kolon oluşur ve içerisinde col3'e ait değerlerin karakter sayısını tutar.
result = df.columns # Kolon bilgileri listelenir.
result = len(df.columns) # kolon sayısı yazdırılır.
result = df.index # indexin başlama, bitiş ve artış miktarını gösterir.
result = len(df.index) # satır sayısına ulaşmış oluruz.
result = df.info # dataFrame hakkında detaylı bilgi verir.

result = df.sort_values("col2") # küçükten biyüğe doğru sıralama işelmi yapar. orjinal dataframe'i değiştirir ve col2'yi sıralanmış bir şekild görürürüz.
result = df.sort_values("col3") # col3 bilgileri str olduğu için d ealfabetik bir sıra ile listelenir.
result = df.sort_values("col2", ascending = False)  # normalde ascending değri True değer döndürür. ancak Folse yaparsak azdan çoğa değil de çoktan aza doğru bir işlem yapar.
# print(result)

data = {
    "Ay": ["Mayıs","haziran","Nisan","Mayıs","haziran","Nisan","Mayıs","haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,50,70,35,24,37]
}

df = pd.DataFrame(data)
df = df.pivot_table(index="Ay",columns="Kategori",values="Gelir") # tüm bilgileri aylara ve kategorilerine göre derledik.
print(df)