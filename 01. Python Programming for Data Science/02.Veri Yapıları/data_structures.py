# VERİ YAPILARI
"""
- Veri yapıları programlama sürecinde farklı veri tiplerini bir arada tutmak için kullanılır.
"""

# Veri Yapılarına Giriş ve Hızlı Bir Bakış
x = 46 # integer
type(x)

x = 10.3 # float
type(x)

x = 2j + 1 # complex
type(x)

x = "Hello AI Era" # string
type(x)

True # boolean
False # boolean
type(True)

5 == 4 # False
3 == 2 # False
1 == 1 # True
type(3 == 2)

x = ["btc", "eth", "xrp"] # list
type(x)

x = {"name": "Peter", "age": 36} # dictionary
type(x)

x = ("python", "ml", "ds") # tuple
type(x)

x = {"python", "ml", "ds"} # set
type(x)

"""
Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collection (Array) olarak geçmektedir.
"""
# Sayılar(Numbers): int, float, complex
a = 5 # integer
b = 10.5 # float
a * 3
a / 7
a * b / 10
a ** 2 # üs alma

### Tip Dönüşümleri(Type Conversion)
int(b) # int() fonksiyonu ile float tipini integer tipine dönüştürebiliriz.
float(a) # float() fonksiyonu ile integer tipini float tipine dönüştürebiliriz.

int(a * b / 10)
c = a * b / 10
int(c)

# Karakter Dizileri(Strings): str
"""
- Karakter dizileri metinsel ifadelerdir ve tırnak içerisinde yazılır.
- Tek tırnak veya çift tırnak kullanılabilir.

"""
print("John")
print('John')
"John"


# Çok Satırlı Karakter Dizileri(Multiline Strings)
long_string = """Veri Yapıları : Hızlı Özet,
Sayılar(Numbers): int, float, complex
Karakter Dizileri(Strings): str
List, Dictionary, Tuple, Set
Boolean(True/False): bool
"""
long_string

# Karakter Dizilerinin Elemanlarına Erişmek
"""
- Karakter dizilerinin elemanlarına erişmek için indis numarası kullanılır.
- İlk karakterin indis numarası 0'dır.

"""
name = "John"
name
name[0] # ilk karakter
name[1] # ikinci karakter

# Karakter Dizilerinde Slice İşlemi
"""
- Karakter dizilerinde slice işlemi, karakter dizisinin belirli bir bölümünü almak için kullanılır.
- Slice işlemi için karakter dizisinin başlangıç ve bitiş indis numaraları kullanılır.
"""
name[0:2] # 0. karakterden 2. karaktere kadar olan karakterler

long_string[0:10] # 0. karakterden 10. karaktere kadar olan karakterler

# String İçerisinde Karakter Sorgulamak
"""
- in operatörü ile karakter dizilerinde bir karakterin olup olmadığını sorgulayabiliriz.
"""

"veri" in long_string # False

"Veri" in long_string # True

"bool" in long_string # True
# String(Karakter Dizileri) Metodları
"""
- dir(str) fonksiyonu ile karakter dizilerinin metodlarını görebiliriz. 
"""
dir(str)

# len() fonksiyonu ile karakter dizilerinin uzunluğunu öğrenebiliriz.
len(name)
len("berkcangümüşışık")
len("miuul")

# Bir fonksiyon class içerisinde tanımlı ise  methodtur. Class içerisinde tanımlı değilse fonksiyondur.

# upper() methodu ile karakter dizilerinin tüm karakterlerini büyük harfe çevirebiliriz.
# lower() methodu ile karakter dizilerinin tüm karakterlerini küçük harfe çevirebiliriz.
"miuul".upper()
"MIUUL".lower()

# replace() methodu ile karakter dizilerindeki bir karakteri başka bir karakter ile değiştirebiliriz.
hi = "Hello AI Era"
hi.replace("l", "p")

# split() methodu ile karakter dizilerini belirli bir karaktere göre bölebiliriz.

hi.split()

# strip() methodu ile karakter dizilerinin başındaki ve sonundaki boşlukları kaldırabiliriz.

"ofofo".strip()
"ofofo".strip("o")

# capitalize() methodu ile karakter dizilerinin ilk karakterini büyük harfe çevirebiliriz.
"foo".capitalize()

# startswith() methodu ile karakter dizilerinin belirli bir karakterle başlayıp başlamadığını sorgulayabiliriz.
"foo".startswith("f")

# Boolean(True/False): bool

# Liste(List): list
"""
- Değiştirilebilir.
- Sıralıdır. Index numarası vardır.
- Kapsayıcıdır. Birden fazla veri tipini içerebilir.
- [] kullanılarak tanımlanır.

"""
notes = [1,2,3,4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1,2,3, "a", "b", True, [1,2,3]]
not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

type(not_nam[6])
type(not_nam[6][1])

notes[0] = 10
notes

# Liste Metodları (List Methods)
dir(list)

# len() fonksiyonu ile listenin uzunluğunu öğrenebiliriz.
len(notes)
len(not_nam)
# append() methodu ile listenin sonuna eleman ekleyebiliriz.
notes.append(100)
notes

# pop() methodu ile listenin sonundaki elemanı çıkarabiliriz.

notes.pop(0)
notes

# insert() methodu ile listenin istediğimiz bir konumuna eleman ekleyebiliriz.

notes.insert(2, 99)
notes
# Sözlük(Dictionary): dict
"""
- Key-Value çiftleri şeklinde tanımlanır.
- Değiştirilebilir.
- Sırasızdır. 3.7'den itibaren sıralıdır.
- Kapsayıcıdır. Birden fazla veri tipini içerebilir.
- {} kullanılarak tanımlanır.
- key'ler ile value'lar arasında : kullanılır.
- key-value çiftleri arasında , kullanılır.
- key'ler unique olmalıdır.
"""
dictionary = {"REG":"Regression",
              "LOG":"Logistic Regression",
              "CART":"Classification and Reg"}
dictionary["REG"]

dictionary = {"REG": ["RMSE",10],
              "LOG": ["MSE", 20],
                "CART": ["SSE", 30]
              }

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["REG"]
dictionary["CART"][1]

# Key Sorgulama
"REG" in dictionary

# Key'e Göre Value Erişme
dictionary["REG"]
dictionary.get("REG") # get() methodu ile key'e göre value'ya erişebiliriz.

# Value Değiştirme
dictionary["REG"] = ["YSA", 10]

# Tüm Key'lere Erişme
dictionary.keys() # keys() methodu ile tüm key'lere erişebiliriz.

# Tüm Value'lara Erişme
dictionary.values() # values() methodu ile tüm value'lara erişebiliriz.

# Tüm çiftlere Erişme
dictionary.items() # items() methodu ile tüm çiftlere erişebiliriz.

# Key Value Değerini Güncelleme
dictionary.update({"REG": 11}) # update() methodu ile key value değerini güncelleyebiliriz.

# Key Value Değeri Ekleme
dictionary.update({"RF": 10}) # update() methodu ile key value değeri ekleyebiliriz.
# Demet(Tuple): tuple
"""
- Değiştirilemez.
- Sıralıdır. Index numarası vardır.
- Kapsayıcıdır. Birden fazla veri tipini içerebilir.
- () kullanılarak tanımlanır.
- Listelerden farkı değiştirilemez olmasıdır.
"""
t = ("john","mark",1,2)
type(t)
t[0]
t[0 : 3]

t = list(t)
t[0] = 99
t = tuple(t)
t

# Küme(Set): set
"""
- Değiştirilebilir.
- Sırasızdır ve eşsizdir.
- Kapsayıcıdır. Birden fazla veri tipini içerebilir.
- {} kullanılarak tanımlanır.
- set() fonksiyonu ile de tanımlanabilir.
"""

# difference() methodu ile iki kümenin farkını alabiliriz.
set1 = set([1,3,5])
set2 = set([1,2,3])
# set1 de olup set2 de olmayan elemanlar
set1.difference(set2)

# set2'de olup set1'de olmayan elemanlar
set2.difference(set1)

# symmetric_difference() methodu ile iki kümenin simetrik farkını alabiliriz.
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

# intersection() methodu ile iki kümenin kesişimini alabiliriz.
set1 = set([1,3,5])
set2 = set([1,2,3])
set1.intersection(set2)
set2.intersection(set1)

# union() methodu ile iki kümenin birleşimini alabiliriz.
set1.union(set2)
set2.union(set1)

# isdisjoint() methodu ile iki kümenin kesişimini kontrol edebiliriz.
set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])
set1.isdisjoint(set2)
set2.isdisjoint(set1)

# issubset() methodu ile bir kümenin alt kümesi olup olmadığını kontrol edebiliriz.
set1.issubset(set2)
set2.issubset(set1)

# issuperset() methodu ile bir kümenin üst kümesi olup olmadığını kontrol edebiliriz.
set1.issuperset(set2)
set2.issuperset(set1)



