import numpy as np

numbers = np.array ([0,5,10,15,20,25,50,75])

result = numbers[3]
result = numbers[-1] # tek boyutlu dizileri normal listelerde olduğu gibi index numarası ile ulaşabiliriz.
result = numbers[3:6] # 3:6 diyerek 3 ile 6. indexe sahip elemanları arasında kalan değerleri alabiliriz. 6. index dahil edilmez.
result = numbers[:3] # sıfırdan başlar 3. indexe kadar devam eder. 3. index dahil edilmez.
result = numbers[3:] # 3. indexten başlar sona kadar yazdırılır.
result = numbers[::] # tüm liste elemanları yazdırılır. 
result = numbers[::-1] # sağdan sola doğru adım sayısı bir olarak yazdırılır. (yani liste tersten yazılmış olur.)
result = numbers[::2] # baştan başlayarak liste elemanları 2şer adımda bir yazfdırılır.

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]]) # 2D bir matris ile index üzerinden veri alalım.

result = numbers2[0] # dersek eğer; [ 0  5 10] ifadesini elde ederiz.
result = numbers2[0,2] # dersek eğer; [ 0  5 10] listesinin içinde 2 indexine sahip eleman ekrana yazdırılır. '10'
result = numbers2[:,2] # dediğimizde : tüm satırı seç demek olur yani satır komple seçilir. satırlar üzerinde ise 2 indexine sahip tüm elemanlar ekran yazdırılır. 
# çıktı: [10 25 85] olur
result = numbers2[:,0:2] #dediğimizde ise satırlar seçilir ve her satırdan 0-2 arası verileri yazdırır.
result = numbers2[-1,:] # dediğimizde ise son satır seçilir son satırdaki tüm elemanlar ekrana yazdırılır.

# print(result)

arr1 = np.arange(0,10)
arr2 = arr1 # referans
arr2[0] = 432

print(f"İlk liste: {arr1}\nİkinci liste: {arr2}") 
# bu işlemn sonucunda her iki listenin bağlı olduğu adres aynı olduğu için arr2 üzerinde yapılan değişiklik arr1'i de etkiler.

arr3 = np.arange(0,10)
arr4 = arr3.copy() # kopyalama işlmei iki ayrı liste aynı içerik.
arr4[0] = 432

print(f"Üçüncü liste: {arr3}\nDördüncü liste: {arr4}") 
# işelm sonrası arr4 üzerindeki değişiklik arr3 listesi üzerinde bir etki yaratmadı. 