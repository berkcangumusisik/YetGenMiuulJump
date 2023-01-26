# Döngüler (Loops)
# for loop
"""
for döngüsü, bir veri grubu üzerinde tek tek gezinmek için kullanılır.
for değişken_ismi in veri_grubu:
    işlemler
"""
students = ["John", "Mark", "Venessa", "Marian"]
students[0]
students[1]
students[2]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary * 20 /100 + salary))

for salary in salaries:
    print(int(salary * 30 /100 + salary))

for salary in salaries:
    print(int(salary * 50 /100 + salary))

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)
new_salary(1500, 10)
new_salary(2000, 20)

for salary in salaries:
    print(new_salary(salary, 10))

salaries2 = [10700, 25000, 30400, 40300, 50200]
for salary in salaries2:
    print(new_salary(salary, 10))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))

# range() fonksiyonu
"""
range() fonksiyonu, bir veri grubu oluşturmak için kullanılır.
range(başlangıç, bitiş, artış miktarı)

"""
range(len("miuul"))
range(0, 5)

for i in range(0, 5):
    print(i)
# Uygulama - Mülakat Sorusu
"""
Amaç aşağıdaki gibi string değiştiren bir fonksiyon yazmak.

before : "hi my name is john and i am learning python"
after : "Hi mY NaMe is JoHn aNd i aM LeArNiNg PYtHoN"
"""

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()

    return new_string
alternating("hi my name is john and i am learning python")

# break ve continue
"""
break : döngüyü sonlandırır.
continue : döngüyü sonlandırmaz, bir sonraki adıma geçer.
"""

salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    if salary == 3000:
        break
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while loop
"""
- while döngüsü, bir koşul sağlandığı sürece döngüyü çalıştırmak için kullanılır.
"""

number = 0
while number < 5:
    print(number)
    number += 1

# Enumerate
"""
Otomatik counter oluşturmak için kullanılır.
enumerate veri grubu, başlangıç değeri ve artış miktarı alır.
"""

students = ["John", "Mark", "Venessa", "Marian"]
for index, student in enumerate(students, 1):
    print(index, student)

A = []
B = []
for index, student in enumerate(students, 1):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

# Mülakat Sorusu
"""
- divide_students fonksiyonu yazınız.
- Çift indexte yer alan öğrencileri bir listeye, tek indexte yer alan öğrencileri başka bir listeye alınız.
- Fakat bu iki liste tek bir liste içinde olmalıdır.
"""

students = ["John", "Mark", "Venessa", "Marian"]
def divide_students(students):
    groups = [[],[]]
    for index, student in enumerate(students, 1):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups
st = divide_students(students)
st[0]
st[1]


# alternating fonksiyonunun enumerate kullanarak yazılması

def alternating_with_enumerate(string):
    new_string = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")

# zip
"""
Listeleri birleştirmek için kullanılır.
"""

students = ["John", "Mark", "Venessa", "Marian"]
departments = ["mathematics","statistics","physics","astronomy"]
ages = [23, 30, 26, 22]

list(zip(students, departments, ages))


# Lambda
"""
Lambda fonksiyonu, tek satırda yazılan fonksiyonlardır.
lambda yazımı : 
lambda değişken_ismi : işlemler
"""


def summer(x, y):
    return x + y
summer(1, 3) * 9

new_sum = lambda a, b : a + b
new_sum(4, 5)


# map
"""
map fonksiyonu, bir veri grubunu başka bir veri grubuna dönüştürmek için kullanılır.
map(fonksiyon, veri_grubu)
"""

salaries = [1000, 2000, 3000, 4000, 5000]
def new_salary(x):
    return x * 20 / 100 + x
list(map(new_salary, salaries))
# del new_sum
list(map(lambda x: x *20 / 100 + x, salaries))
list(map(lambda x: x ** 2, salaries))

# filter
"""
filter fonksiyonu, bir veri grubundan istediğimiz elemanları seçmek için kullanılır.
"""

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# reduce
"""
reduce fonksiyonu, bir veri grubundaki elemanları birleştirmek için kullanılır.
"""

from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda x, y: x + y, list_store)