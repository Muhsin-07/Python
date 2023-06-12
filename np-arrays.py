import numpy as np

result = np.array([1,3,5,7,9]) # bu şekilde elemanlarını tek tek yazarak bir dizi oluşturabiliriz.

result = np.arange(1,10) # arange metodu ile belli bir aralığı dizi olarak alabiliriz. "10 dahil değil."

result = np.arange(10,100,3) # Bu dizinin artış miktarını ise bir virgül daha ekleyerek kendimiz belirleyebiliriz.

result = np.zeros(10) # bu metod ile içine yazılan sayı kadar 0 (sıfır) sayısı dizi olarak özümüze gelir. 

result = np.ones(10) # bu metod ile içine yazılan sayı kadar 1 (bir) sayısı dizi olarak özümüze gelir. 

result = np.linspace(1,100,5) # linspace metodu ise belirtilen aralığı istediğimiz bir adede bölmemizi sağlar.
                                # {örnekte 1-100 arasını 5 eşit parçaya bölmüştür ve önümüze 5 elemanlı bir dizi çıkmıştır.}

result = np.random.randint(0,10) # bu modül ise belirtilen aralıkta rastgele bir sayı türetir.

result = np.random.randint(0,10,3) # dersek eğer 0 ile 10 arası 3 sayı üretilir ve önümüze çıkarılır.

result = np.random.rand() # metodu ise 0-1 arasında rastgele sayı getirir. modüle herhangi bir parametre atarsak attığımız parametre adetince sayı üretilir.

result = np.random.randn() # random.rand metodunun sonuna 'n' getirsek eğer negatif sayıları kapsayacak şekilde değerlendirilir.

np_array = np.arange(50)
result = np_array.reshape(5,10) # dersek eğer 5 satır ve 10 sütundan oluşan bir matris oluşturmuş oluruz.

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
result = np_multi.sum(axis=1) # sum metodu ile satırları veya sütınları toplayabiliriz. axis=1 dersek eğer satırların toplamını verir.
result = np_multi.sum(axis=0) # axis=0 değerini girersek eğer sütunların toplamını verir.

result = np.random.randint(1,100,10)
# print(rnd_numbers)
resultMax = result.max() # max metodu ile oluşturulan 10 sayıdan en büyük olan sayıyı alabiliriz.
resultMin = result.min() # min metodu ile oluşturulan 10 sayıdan en küçük olan sayıyı alabiliriz.
resultMean = result.mean() # mean metodu ise oluşturulan sayıların ortaşamasını verir.
resultİndex_Max = result.argmax() # en büyük sayının index numarasını verir.
resultİndex_Min = result.argmin() # argmin metodu ise en küçük sayının index numarasını verir.

# print(result)
print(f"numbers: {result}\nMax value: {resultMax}\nMin value: {resultMin}\nAverage of numbers: {resultMean}\nİndex number of max value: {resultİndex_Max}\nSmallest index of numbers: {resultİndex_Min}")