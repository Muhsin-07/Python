import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)


result = numbers1 + numbers2 # üretilen sayılar index numaralarına göre toplanır. 0. index 0 ile 1. index 1. indexle...
result = numbers1 + 10 # numbers1'in içindeki her bir elemana 10 eklemiş oluruz.
result = numbers1 - numbers2 # üretilen sayılar index numaralarına göre çıkarılır. 0. index 0 ile 1. index 1. indexle...
result = numbers1 * numbers2
result = numbers1 / numbers2
result = np.sin(numbers1) # numbers1'in sinüsünü alır.
result = np.cos(numbers2)
result = np.tan(numbers2)
result = np.sqrt(numbers1) # ile numbers1 elemanlarının kare kökünü almış oluruz.
result = np.log(numbers1) # logaritması alınır.

print(numbers1)
print(numbers2)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3) # 2 satır 3 sütundan oluşan matrisler oluşturur.
print(mnumbers1)
print(mnumbers2)


result = np.vstack((mnumbers1,mnumbers2)) # dikey olarak matrisleri birleştirir. tek matris olur.
result = np.hstack((mnumbers1,mnumbers2)) # yatay olarak matrisleri birleştirir. tek matris olur.

result = numbers1 > 5 # liste elemanlarını tek tek alır ve karşılaştırır. bool veri tipinde yeni bir liste gönderir.
result = numbers1 % 2 == 0 # istediğimiz işlemi yapar ve bool veri tipinde yeni bir liste gönderir.

print(numbers1[result]) # bu işlemle numbers1 içinde numbers1 % 2 == 0 koşulunu sağlayan değerler liste olarak gelir.
print(result)

