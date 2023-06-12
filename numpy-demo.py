import numpy as np

result = np.array([10,15,30,45,60])
result = np.arange(5,15)
result = np.arange(50,100,5)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0,100,5)
result = np.random.randint(10,30,5)
result = np.random.randn(5)
numbers = np.random.randint(10,50,15)
matris = numbers.reshape(3,5)
result = matris.sum(axis=1)
result = matris.sum(axis=0) 
result = matris.max()
result = matris.min()
result = matris.mean()
result = matris.argmax()
result = matris.argmin()

print(matris)
print(result)

numbers2 = np.arange(10,20)
result = numbers2[:3]
result = numbers2[::-1]
matris2 = numbers2.reshape(5,2) 
result = matris2[0]
result = matris2[1,1]
result = matris2[:,0]
result = matris2 ** 2

print(matris2)
print(numbers2)
print(result)


numbers3 = np.arange(-50,50)
çiftler = numbers3[numbers3 % 2 == 0]
result = çiftler[çiftler >= 0]

print(result)