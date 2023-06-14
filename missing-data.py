import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3) 
# rastgele sayılar ürettik bu sayılara 5 satır ve 3 sütuna ayırdık.

df = pd.DataFrame(data, index=['a','c','d','f','h'], columns=["col1","col2","col3"])
# oluşturulan sayıları dataFrame'e çevirdik ve index numaraları ve kolon bilgileri ekledik.

df = df.reindex(['a','b','c','d','e','f','g','h'])
# verilen indexleri çoğalttık. çoğalan inde numaraları karşısına Nan bilgisi gelecek hata almayacağız.

newColumn = [np.nan,30,np.nan,75,np.nan,62,np.nan,34]
df["col4"] = newColumn
# burada yen ibir kolon oluşturduk ve içerisine değerler atadık. mp.nan ise Nan değerlerine karşılık geliyor. 

result = df
# df'i result içine aldık

result = df.drop("col1", axis=1)
# col1'i sildik

result = df.drop(["col1","col3"], axis=1)
# birden fazla kolonu sildik. istemediğimiz uğraşmadığımız kolonları veya satırları bu şekilde rahatlıkla silebiliriz.

result = df.drop(["a","d"], axis=0)
# burada ise satır silme işlemi yaptık. 

result = df.isnull()
# .isnull() metodu Nan olan değerleri bulmak için kullandığımız bir metoddur. Nan olanlar True değerini döndürür.

result = df.notnull()
# yukardaki işlemin tersini yapar Nan olanlar Folse döndürür.

result = df.isnull().sum()
# bu şekşlde hangi kolonda kaç tane Nan değer var tespit edebiliriz.

result = df["col1"].isnull().sum()
# sadece col1 üzerinde kaç tane Nan var diye sormuş oluruz. 

result = df[df["col1"].isnull()]["col1"]
# col1 için Nan olan değerleri bize getirir.

result = df[df["col1"].notnull()]["col1"]
# col1 için Nan olmayan değerler bize getirilir.

result = df.dropna() # axis=0 => varsayılan değer.
# .dropna() metodu ise satrıda Nan olan bir değer varsa o satırı olduğu gibi getirmez.
result = df.dropna(axis=1)
# (axis=0)(varsayılanı) bunu istersek 1 yapıp kolonu getirme de diyebiliriz.

result = df.dropna(how="any") 
# how="any" dediğimizde satırda tek bir Nan varsa o satırı siler. ekrana getirmez.

result = df.dropna(how="all")
# how="all" dediğimizde ise satır tamamen Nan değer içeriyorsa siler diğer durumda satırı yazdırır.

result = df.dropna(subset=["col1","col3"])
# col1 ve col3 için bir arama yapar ve sadece o kolonlara bakarak işlem yapar.

result = df.dropna(subset=["col1","col3"], how="all")
# bu şekilde yazarsak eğer col1 ve col2'de aynı satırda ve Nan değerleri mevcutsa o satırı siler. 

result = df.dropna(thresh=2) # en az 2 normal veri.
# thresh=2 dediğimizde içerisinde Nan olmayan iki veri varsa satrı tutar(silmez).

result = df.fillna(value="no input")
result= df.fillna(value=1)
# .fillna() içerise yazılan value değerlerini Nan ile değiştiriyor.
###########Ortalama############
result = df.sum().sum()
# iki defa sum() metodunı kullandık çünkü sadece satırları değil sütunları da topplayıp tüm verilerin toplamını bulmak istiyorduk.
result = df.size
# .size metodu ile toplam veri adedini bulabiliyoruz. 
result = df.isnull().sum().sum() # ==> Nan olan değerlerin toplamıdır.


def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value = ortalama(df))

# buradaki fonksiyon sayesinde Nan olan değerler aldığımız ortalama bilgisini ekledik.

print(result)