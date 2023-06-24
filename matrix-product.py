import numpy as np
# matris çarpımı nasıl yapılır ?
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([[5, 6, 3, 8], [3, 5, 9, 2]])

c = a.dot(b.T)

print(c)