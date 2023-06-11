import numpy as np

# python listesi
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9]) # array metodu dizi oluşturmamızı sağlayan bir metoddur.

# print(type(py_list))
# print(type(numpy_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)   # reshape metodu ile oluşturulan diziyi parçalara ayırabiliriz. 
                                   # (3 satır ve 3 kolondan oluşan bir dizi elde etmek için "(3,3)" dedik.)

print(py_multi)
print(np_multi)

print(np_array.ndim)
print(np_multi.ndim)  # ndim mmetodu ise oluşturulan dizinin kaç boyutlu olduğunu bize söyler. 
                      # örneğin print(np_array.ndim) # 1 """  yani 1-D 1 boyutlu olduğunu belirtir.     """
                      # ya da print(np_multi.ndim) # 2   """  yani 2-D 2 boyutlu olduğunu belirtir.     """

print(np_array.shape)
print(np_multi.shape) # shope metodu ise dizinin kaça kaçlık olduğunu söyler yatayde ve dikeyde kaç eleman olduğunu belirtir.
