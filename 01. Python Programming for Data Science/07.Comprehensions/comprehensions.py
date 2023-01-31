# Comprehensions

# List Comprehension
"""
- Comprehension, birden fazla kod satırını tek bir satırda yazmamızı sağlar.
"""

# Klasik Yöntem
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x
null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))


# List Comprehension
"""
- [içerik if koşul else içerik if koşul else içerik for değişken in veri_grubu]
"""
[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries ]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]


students = ["John", "Mark", "Venessa", "Marian"]

students_no = ["John","Venessa"]

[student.lower() if student in students_no else student.upper()  for student in students]

[student.lower() if student not in students_no else student.upper()  for student in students]

# Dictionary Comprehension
dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}
{k.upper(): v for (k, v) in dictionary.items()}
{k.upper(): v * 2 for (k, v) in dictionary.items()}


#Uygulama - Mülakat Sorusu
"""
Amaç : çift sayıların karesi alınarak bir sözlüğe eklenmek isteniyor.
- Keyler orijinal değerler value ise değişmiş değerler olacak.
"""

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n : n ** 2 for n in numbers if n % 2 == 0}

# Uygulamalar

"""
Bir veri setindeki değişken isimlerini değiştirmek istiyoruz.
before:
['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

after:
['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']
"""

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())


A =[]
for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]


"""
İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']
"""

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]


"""
Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.  Sadece sayısal değişkenler için yapmak istiyoruz.
# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}
"""

df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]

soz = {}
agg_list = ["mean", "min", "max", "var"]

for col in num_cols:
    soz[col] = agg_list

# kısa yol
new_dict = {col: agg_list for col in num_cols}
df[num_cols].head()

df[num_cols].agg(new_dict)


