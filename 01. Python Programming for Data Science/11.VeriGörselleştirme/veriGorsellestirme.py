# Veri Görselleştirme : Matplotlib ve Seaborn

# Matplotlib
"""
Matplotlib, Python programlama dili için bir 2B grafik kütüphanesidir.
Matplotlib, MATLAB benzeri bir grafik çizim arayüzü sunar.
Veri görselleştirme için kullanılan en popüler kütüphanelerden biridir.
- Kategorik değişken : sütun grafiği, countplot bar
- Sayısal Değişken : histogram, boxplot


"""

# Kategorik Değişken Görselleştirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind = "bar") # .plot() fonksiyonu ile grafik çizdiriyoruz. kind parametresi ile çizim türünü belirliyoruz.
plt.show() # plt.show() ile grafik çizdiriyoruz.

# Sayısal Değişken Görselleştirme
plt.hist(df["age"], bins = 10) # bins parametresi ile histogramın bar sayısını belirliyoruz. .hist() fonksiyonu ile histogram çizdiriyoruz.
plt.show()

plt.boxplot(df["fare"]) # .boxplot() fonksiyonu ile kutu grafiği çizdiriyoruz.
plt.show()

# Matplotlib Özellikleri
"""
- .plot() fonksiyonu ile çizim yapılır. 
"""

x = np.array([1, 8])
y = np.array([0, 150])
plt.plot(x, y)
plt.show()

plt.plot(x,y,"o") # "o" parametresi ile nokta çizdiriyoruz.

x = np.array([2,4,6,8,10])
y = np.array([1,3,5,7,9])
plt.plot(x,y)
plt.show()


plt.plot(x,y, "o")
plt.show()

"""
marker ile çizim türünü belirleyebiliriz.
"""
y = np.array([13,28,11,100])
plt.plot(y, marker = "o")
plt.show()

plt.plot(y, marker = "*")
plt.show()

marker = ["o", "v", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D", "d", "|", "_"]

"""
line
- linestyle ile çizgi türünü belirleyebiliriz.
"""

y = np.array([13,28,11,100])
plt.plot(y, linestyle = "dashed") # linestyle ile çizgi türünü belirleyebiliriz. dashed, dotted, solid, dashdot vb.
plt.show()


# Multiple Lines
import numpy as np
x = np.array([23,18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

# Başlık ve Etiketler
"""
- plt.title() ile başlık ekleyebiliriz.
- plt.xlabel() ile x eksenine etiket ekleyebiliriz.
- plt.ylabel() ile y eksenine etiket ekleyebiliriz.
- plt.grid() ile grid ekleyebiliriz.
"""

plt.title("Matplotlib Örnek")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.grid()
plt.plot(x)


# Subplot .subplot() fonksiyonu ile çoklu grafik çizdirebiliriz.

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)


# 2. grafik
x = np.array([8,8,9,9,10,15,11,15,12,15])
y = np.array([24,20,26,27,280,29,30,30,30,30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)



x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)


# Seaborn
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x = df["sex"], data = df) # .countplot() fonksiyonu ile kategorik değişkenin frekansını görselleştirebiliriz.
plt.show()

df["sex"].value_counts().plot(kind = "bar")
plt.show()

# Sayısal Değişken Görselleştirme
sns.boxplot(x = df["total_bill"]) # .boxplot() fonksiyonu ile kutu grafiği çizdirebiliriz.
plt.show()

df["total_bill"].hist() # .hist() fonksiyonu ile histogram çizdirebiliriz.
plt.show()