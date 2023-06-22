import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
x = [1,2,3,4]
y = [1,4,9,16]
# plt.plot(x,y) # x ve y'ye ait değerleri grafiğe döktük.
# plt.plot(x,y,color="yellow",linewidth="4") # color ile çizginin rengini sarı, linewidth ile kalınılığını 4 px yaptık.
plt.plot(x,y, "o--r") # marker,line,color bilgilerini bu şekilde de verebiliriz. ""matplotlib plot style"" diye aratırsak bilgi alabiliriz.
plt.axis([0,6,0,20]) # x ve y'nin değer aralığını belirttik.
plt.title("Grafik Başlığı") # grafik tablosunun başlığını verdik.
plt.xlabel("x label")
plt.ylabel("y label") # x ve y eksenine isim verdik.
"""
"""
x = np.linspace  (0,2,100)

plt.plot(x, x, label = "linear")
plt.plot(x, x**2, label = "quadratic")
plt.plot(x, x**3, label = "cubic")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Simple Plot")
plt.legend() 
plt.show()
"""
"""
x = np.linspace  (0,2,100)

fig,axs = plt.subplots(3)

axs[0].plot(x,x,color="blue")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="blue")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="blue")
axs[2].set_title("cubic")

plt.tight_layout()
plt.show()
"""
"""
x = np.linspace(0,2,100)

fig,axs = plt.subplots(2,2)
fig.suptitle("Grafik Başlığı")

axs[0,0].plot(x,x,color="blue")
axs[0,1].plot(x,x**2,color="red")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="yellow")

plt.show()
"""

df = pd.read_csv("datasets/nba.csv")
df.drop(["draft_number","gp","pts","reb","ast","oreb_pct","dreb_pct","usg_pct","ts_pct","ast_pct"], axis = 1, inplace=True)
df.groupby("team_abbreviation")[["age","player_height","player_weight"]].mean()
df.head().plot(subplots=True)

plt.legend()
plt.show()
