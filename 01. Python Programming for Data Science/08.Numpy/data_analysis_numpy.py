# NUMPY

# Neden Numpy?
"""
- Numpy, Python'da bilimsel hesaplamalar için kullanılan bir kütüphanedir.
- Arrayler, çok boyutlu diziler, matrisler üzerinde çalışmamızı sağlar.
- Temelleri 1995 yılında atılmıştır.
- Matematiksel, bilimsel, finansal hesaplamalar için kullanılır.
Listelerden farkı:
- Verimli veri saklama
- Yüksek seviyeden işlemler (vektörel işlemler)
- Hızlıdır.
- Döngü yazmaya gerek olmadan array üzerinde işlem yapılabilir.
"""
import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
ab

# Numpy Array ile
"""
np.array() fonksiyonu ile listelerden numpy array oluşturabiliriz.
"""
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a * b

# Numpy Array Oluşturma
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype = int)
# np.zeros() ile 0'lardan oluşan bir array oluşturabiliriz.

np.random.randint(0, 10, size = 10)
# np.random.randint() ile belirli bir aralıkta rastgele sayılar üretebiliriz.

np.random.normal(10, 4, size = (3, 5))
# np.random.normal() ile normal dağılım gösteren sayılar üretebiliriz.

np.ones((3, 5), dtype = int)
# np.ones() ile 1'lerden oluşan bir array oluşturabiliriz.


# Numpy Array Özellikleri
"""
- ndim: boyut sayısı
- shape: boyut bilgisi
- size: toplam eleman sayısı
- dtype: array veri tipi
"""

a = np.random.randint(10, size = 5)
a.ndim
a.shape
a.size
a.dtype

# Reshaping (Yeniden Şekillendirme)
"""
.reshape() fonksiyonu ile arrayin boyutlarını değiştirebiliriz.
"""

np.random.randint(1,10, size = 9)
np.random.randint(1,10, size = 9).reshape(3,3)

ar = np.random.randint(1,10, size = 9)
ar.reshape(3,3)


# Index Seçimi
a = np.random.randint(10, size = 10)
a[0]
a[0:5] # 0'dan 5'e kadar
a[0] = 999

m = np.random.randint(10, size = (3, 5))
# [satır, sütun]
m[0, 0]
m[1, 1]
m[2, 3] = 999
m[2, 3] = 2.9 # 2.9 değeri 2'ye yuvarlanır.

m[ : , 0] # Tüm satırların 0. sütunu
m[1, : ] # 1. satırın tüm sütunları
m[0:2, 0:3] # 0 ve 1. satırların 0, 1 ve 2. sütunları

# Fancy Index
v = np.arange(0, 30, 3)
v[1]
v[4]

"""
Fancy Index ile birden fazla index seçimi yapabiliriz.

"""

catch = [1, 2, 3]
v[catch]


# Koşullu Eleman İşlemleri
v = np.array([1, 2, 3, 4, 5])


## Klasik Yöntem
ab = []
for i in v:
    if i < 3:
        ab.append(i)
ab

## Numpy Yöntemi
v < 3 # Bütün elemanlara koşul uygulanır.
v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v <= 3]
v[v >= 3]


# Matematiksel İşlemler
v = np.array([1, 2, 3, 4, 5])
v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1) # v'den 1 çıkarır.
np.add(v, 1) # v'ye 1 ekler.
np.mean(v) # v'in ortalaması
np.sum(v) # v'in toplamı
np.max(v) # v'in en büyük elemanı
np.min(v) # v'in en küçük elemanı
np.var(v) # v'in varyansı

# İki Bilinmeyenli Denklem Çözümü
"""
5*x0 + x1 = 12
x0 + 3*x1 = 10
"""

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])
np.linalg.solve(a, b)

# np.linalg.solve() ile iki bilinmeyenli denklem çözümü yapabiliriz.
