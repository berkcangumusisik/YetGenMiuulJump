# FONKSİYONLAR(FUNCTIONS)
"""
- Fonksiyonlar belli görevleri yerine getiren kod bloklarıdır.
- ?print ile ekrana yazdırma işlemi yapan fonksiyonun nasıl çalıştığını görebiliriz.
- argüman => Fonksiyonlar çağırıldığında parametre olarak girilen değerlerdir.
- parametre => fonksiyonun tanımlanması sırasındaki belirtilen değişkenlerdir.

"""
print("a")
print("a", "b", sep="__")

# Fonksiyon Tanımlamak
"""
def fonksiyon_adi(argüman1, argüman2, ...):
    kod bloğu

fonksiyon_adi(argüman1, argüman2, ...)
"""

def calculate(x):
    print(x * 2)

calculate(2)

# İki argümanlı / parametreli fonksiyon tanımlamak

def summer(arg1, arg2):
    print(arg1 + arg2)

summer(7, 8)

# argüman sırası önemlidir.

summer(8, 7)

summer(arg2=8, arg1=7)


# Docstring (Açıklama Satırı)
"""
Fonksiyonlara bilgi eklemek için kullanılır.
numpy docstring formatı kullanılır.
- 3 ana başlık vardır.
- Açıklama : Fonksiyonun ne yaptığı
- Parameters : Fonksiyona girilen argümanların ne olduğu
- Returns : Fonksiyonun döndürdüğü değerlerin ne olduğu
"""

def summer(arg1, arg2):
    """
    Sum of two numbers
    Parameters
    ----------
    arg1 : int, float
    arg2 : int, float

    Returns
    -------
    int, float
    """
    print(arg1 + arg2)

summer(1,3)


# Fonksiyonlarda Statement / Body bölümü
"""
def function_name(parameters / arguments):
    statement(function body)
"""

def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")

say_hi()


def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

say_hi("miuul")



def multipication(a, b):
    c = a * b
    print(c)

multipication(10,9)

# girilen değerleri bir liste içinde saklayacak fonksiyon

list_store = []

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1,8)
add_element(18,8)
add_element(180,10)


# Ön Tanımlı Argümanlar / Parametreler (Default Parameters / Arguments)
"""
- Fonksiyon tanımlanırken argümanlara varsayılan değerler verilebilir.

"""
def divide(a, b):
    print(a / b)

divide(1, 2)


def divide(a, b=1):
    print(a / b)

divide(1)

def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi("mrb")


# Ne Zaman Fonksiyon Kullanmalıyız?
"""
- DRY (Don't Repeat Yourself) => Tekrar etme
- Fonksiyonlar kod tekrarını önler.
- Fonksiyonlar kodun okunabilirliğini artırır. 
"""

def calculate(varm, moisture, charge):
    print((varm + moisture ) / charge)

calculate(98, 12, 78)

# Return
"""
- Fonksiyon çıktılarını girdi olarak kullanmak için kullanılır.
- Fonksiyon dışında işlem yapmak için kullanılır.
"""

def calculate(varm, moisture, charge):
    print((varm + moisture ) / charge)

calculate(98, 12, 78)

def calculate(varm, moisture, charge):
    return (varm + moisture ) / charge

calculate(98, 12, 78) * 10

a = calculate(98, 12, 78)

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture ) / charge
    return varm, moisture, charge, output

calculate(98, 12, 78)

varm, moisture, charge, output = calculate(98, 12, 78)


# Fonksiyonlar İçerisinde Fonksiyon Çağırma

def calculate(varm, moisture, charge):
    return int((varm + moisture ) / charge)

calculate(90, 12, 12) * 10

def standardizaton(a,p):
    return a * 10 / 100 * p * p

standardizaton(45, 1)

def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardizaton(a, p)
    print(b * 10)

all_calculation(1, 3, 5, 12)


def all_calculation(varm, moisture, charge, a, p):
    calculate(varm, moisture, charge)
    b = standardizaton(a, p)
    print(b * 10)

all_calculation(1, 3, 5,19, 12)


# Local ve Global Değişkenler
"""
- Global Değişkenler => Fonksiyon dışında tanımlanmış değişkenlerdir.
- Local Değişkenler => Fonksiyon içinde tanımlanmış değişkenlerdir.
"""
list_store = [1,2]

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(1,9)