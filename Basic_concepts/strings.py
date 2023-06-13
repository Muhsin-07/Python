name = "Muhsin"
surname = "DEMİR"
age = 21

greeting = "Hello may name is "+ name +" "+  surname + " and \nI am "+ str(age) + " years old."
# print(greeting)

lenght = len(greeting) 

# print(greeting[0])
# print(greeting[4])
# print(len(greeting)) # len metodu ile cümlemizin kaç karakter olduğunu buluruz bulduğum sayıdan bir çıkartak ise son karakterine erişebiliriz.
# # print(greeting[lenght - 1])

# print(greeting[0:6]) # iki nokta ile indeks numaralarını kullanarak belli aralıklarda bulunan yerleri yazdırabiliriz.

print(greeting[3:])  # iki noktadan sonra bir şey yazmazsak eğer indek nosu 3 olandan sonuna kadar yazdırır.
print(greeting[:-9])

print(greeting[:15])

print(greeting[5:40:2]) # 5ten başla 40 kadar 2 karakterde bir yazdır demiş oluruz

