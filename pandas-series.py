import pandas as pd
import numpy as np
# data

numbers = [10,15,37,14,68,34]
letters = ['a','dc','kds','juj']

pandas_series = pd.Series(numbers) # dediğimizde numbers listesi bir seri olarak yazdırılır ve index numaraları da bu seride gösterilir. tipi int olarak yazdırılır.
pandas_series = pd.Series(letters) # dediğimizde letters listesi bir seri olarak yazdırılır ve index numaraları da bu seride gösterilir. tiği object olarak yazdırılır.


mixed = ['mercan','elif','muhsin', 20, 38]
pandas_series = pd.Series(mixed)
# oluşturduğumuz listeler aynı yapıda olmak zorunda değil. hetorejen yapılı listeler de oluşturulabilir bu durum seriler için bir sorun oluşturmaz. 

scalar = 3
pandas_series = pd.Series(scalar) # 3 değerini index ve tipi ile birlikte ekrana yazdırır.
scalar = 3
pandas_series = pd.Series(scalar,[0,3,4,7]) # istersek eğer index numaralarını atayıp index numarası adedince bilgiyi çoğaltabiliriz.


pandas_series = pd.Series(numbers,['a','b','c','d','e','f']) # oluşturulan seri index numarası ile değil verdiğimiz a,b,c... değerleri ile sıralanır.
                                                             # yani index numarası ile değil de key(anahtar kelime) bilgisi olarak atanmış olur 
                                                             # key bilgi sayısı liste eleman sayısı kadar olmalıdır.

dic = {'a':10,'b':20,'c':30,'d':40}
pandas_series = pd.Series(dic) # bu dic yapısını kolaylıkla bir pandas serisi olarak oluşturabiliyoruz. key bilgileri zaten verildiği için index olarak değil de listeden verilen key bilgileri önümüze çıkıyor.

random_numbers = np.random.randint(0,100,10)
pandas_series = pd.Series(random_numbers) # oluşturduğumuz numpy dizilerini de pandas serilerine çevirebiliyoruz.


numbers = [10,15,37,14,68,34]
pandas_series = pd.Series(numbers,['a','b','c','d','e','f'])
result = pandas_series[0]
result = pandas_series['c'] # index numarası yerine atatığımzı key üzerinden de ulaşılabilen value değerlerine, key bilgisi vermiş olsak bile index ile de ulaşabiliriz.
result = pandas_series[['a','d']] # 'a' ve 'd' to your keys karşılık gelen bilgiler yazdırılır.

result = pandas_series.ndim # ndim ile serinin kaç boyutlu olduğuna bakabiliriz.(tıpkı numpy'da olduğu gibi.) 
result = pandas_series.dtype # tipini öğrenebiliriz.
result = pandas_series.shape # 6'ya 1'lik bir liste olduğunu belirtir. 
result = pandas_series.sum() # tüm value değerlerinin toplamını yazdırır.
result = pandas_series.max() # max değeri gösterir.
result = pandas_series.min() # min değeri gösterir.
result = pandas_series + pandas_series # seriler toplayabiliriz.
result = pandas_series + 50 # serinin her value değerine 50 ekler.
result = np.sqrt(pandas_series) # her değerin karekökü alınır.
result =pandas_series > 50 # ile True ve Folse değerlerinden bir seri oluşur.
result = pandas_series % 2 == 0 # ile çift sayıları öğrenebiliriz.
result = pandas_series[result] # true dönen değerleri bize getirir.

# print(result)
# pandas_series = pd.Series() # tipi nesne (type = object) olan bir seri oluşturmuş oluruz.(liste)
# print(pandas_series)

"""
opel marka arabanın satış serisi.
"""
opel2018 = pd.Series([20,30,40,10],['astra','corsa','mokka','insignia'])
opel2019  = pd.Series([40,30,20,10],['astra','corsa','grandland','insignia'])

total = opel2018 + opel2019

print(total['astra'])