import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2
"""
figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("X axes")
axes_cube.set_ylabel("Y axes")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.19,0.6,0.25,0.253])
axes_square.plot(x,z,'r')
axes_square.set_xlabel("X axes")
axes_square.set_ylabel("Z axes")
axes_square.set_title("Square")

plt.show()
"""
"""
figure = plt.figure() 

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend()

plt.show()
"""

fig,axes = plt.subplots(nrows=2,ncols=1, figsize=(8,8))

axes[0].plot(x,y)
axes[0].set_title("Cube")

axes[1].plot(x,z)
axes[1].set_title("Square")

plt.savefig("figure.png")
plt.tight_layout()
plt.show()
