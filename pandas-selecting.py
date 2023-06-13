from numpy.random import randn
import pandas as pd

df = pd.DataFrame(randn(3,3), index = ['A','B','C'], columns = ['col1','col2','col3'])

result = df
result = df["col1"] # sadece Colon1 ekrana yazdırılır.
result = type(df["col1"])
result = df[["col1","col2"]]

# loc["row","column"] => loc["row"] => loc[:,"column"]
result = df.loc["A"] # index'e göre seçerken satırı seri gibi yazıdrır. ve loc metodu ile çağırma işlemi yapılır.
result = type(df.loc["A"]),
result = df.iloc[2] # index numaralarını değiştirdiğimiz için '.loc' metodu ile çağıramayız. bu şekilde çağırmak için '.iloc' metodunu kullanabiliriz.
result = df.loc[:,"col2"] # kolona ait sütunu seri olarak yazdırır. ve loc metodu ile çağırma işlemi yapılır.
result = df.loc["A",:] # A indexinde bulunan 3 kolonu da seri şeklinde yazdırılır.
# result = df.loc[:,"col1","col2"] # bir ve ikinci kolon yazdırılır.
resualt = df.loc[:,"col1":"col3"] # df.loc[:,”col1”:”col3”] gibi DataFrame den bir dilim seçme işlemlerinde Numpy’dan farklı olarak col3 sütunu da dahil edilir. Yani col1, col2, col3 sütunlarından oluşan DataFrame nesnesi döndürür.
result = df.loc[:,:"col2"] #"" :"col2" "" baştan başla col2'ye kadar git demiş oluyoruz.
result = df.loc["A":"B",:"col2"] # indexlerde de aynı şekilde aralık belirtebiliriz.
result = df.loc[:"B",:"col2"] # :"B" baştan başla B'ye kadar git.
result = df.loc["A","col2"] # 'A' satırındaki 'col2''ye ait bilgiyi alabiliriz.
result = df.loc[["A","B"],["col1","col3"]] # A ve B satırındaki col1 ve col3 bilgilerini yazdırır.
# print(result)

# ekleme işlemi
df["col4"] = pd.Series(randn(3), ["A","B","C"]) # burada yeni bir seri oluşturduk ve col4 adını verdik. dataFrame'e ekledik.
df["col5"] = df["col1"] + df["col3"] # burada bir ekleme işlemi yaptın ancak yeni bir seri oluşturmadık. var olan serilerin toplamını gösteren bir seri oluşturmuş olduk.
# print(df)

# silme işlemi

result = df.drop("col5", axis=1)
result = df.drop("A", axis=0) # '.drop()' ile istediğimiz bir kolonu veya sütunu silebiliriz.
# önemli olan nokta axis değeri axis=1 ise kolon 0(sıfır) ise satır demiş .luyoruz.
print(df) # yaptığımız değişiklikler sadece result için yapılır orjinali  değişmez. orjinalinin değişmesini istiyorsak 'inplace=True' değerini de eklememiz gerekiyor.
result = df.drop("col5", axis=1, inplace=True)
print(result)
print(df) # orjinali değiştirdiğimiz için 'df''i yazdırınca da yaptığımız değişiklik uygulanmış olur.
