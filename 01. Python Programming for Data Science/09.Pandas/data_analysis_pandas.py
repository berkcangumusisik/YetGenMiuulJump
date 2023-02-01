# Pandas Series
"""
pd.Series ile pandas kütüphanesindeki Series sınıfını kullanabiliriz.
"""
import pandas as pd
s = pd.Series([10,77, 12, 4, 5])
type(s)
s.index # .index ile indeksleri görebiliriz.
s.dtype # .dtype ile veri tipini görebiliriz.
s.size # .size ile eleman sayısını görebiliriz.
s.shape # .shape ile boyut bilgisini görebiliriz.
s.ndim # .ndim ile boyut sayısını görebiliriz.
s.values # .values ile array değerlerini görebiliriz.
type(s.values)
s.head() # .head() ile ilk 5 değeri görebiliriz.
s.head(3) # .head() ile ilk 3 değeri görebiliriz.
s.tail() # .tail() ile son 5 değeri görebiliriz.
s.tail(3) # .tail() ile son 3 değeri görebiliriz.

# Veri Okuma
df = pd.read_csv("01. Python Programming for Data Science/09.Pandas/datasets/advertising.csv") # .read_csv() ile csv dosyasını okuyabiliriz.
df.head()

# Veriye Hızlı Bakış
import seaborn as sns
df = sns.load_dataset("titanic")

df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T #.describe() ile veri setinin istatistiksel özelliklerine ulaşabiliriz. T ile transpozunu alabiliriz. (Satır ve sütunları yer değiştirir.)
df.isnull().values.any() # .isnull() ile eksik değer var mı diye kontrol edebiliriz. .values.any() ile de True/False olarak görebiliriz.
df.isnull().sum() # .isnull().sum() ile eksik değerlerin toplamını görebiliriz.
df["sex"].head()

# Pandas Seçim İşlemleri
df = sns.load_dataset("titanic")
df.head()

df.index
df[0 : 13]
df.drop(0, axis = 0).head() # .drop() ile istediğimiz satırı silebiliriz. axis = 0 ile satır, axis = 1 ile sütun seçimi yapabiliriz.

delete_indexes = [1,3,5,7]
df.drop(delete_indexes, axis = 0).head()

# Kalıcı Silme
"""
df = df.drop(delete_indexes, axis = 0)
df.drop(delete_indexes, axis = 0, inplace = True) # inplace = True ile kalıcı olarak silebiliriz.
"""

# Değişkenleri Indexe Çevirme
df["age"].head()
df.age.head()
df.index = df["age"]

df.drop("age", axis = 1, inplace = True)
df.head()


# Indexi Değişken Yapma
df.index
df["age"] = df.index
df.head()
df.drop("age", axis = 1, inplace = True)

df.reset_index().head() # .reset_index() ile indexi değişken yapabiliriz.
df = df.reset_index()
df.head()


# Değişenkenler Üzerinde İşlemler

pd.set_option("display.max_columns", None) # .set_option() ile gösterilecek maksimum sütun sayısını belirleyebiliriz.
df = sns.load_dataset("titanic")
df.head()

"age" in df # "age" değişkeni df içinde var mı diye kontrol edebiliriz.

df["age"].head()
df.age.head()

type(df["age"].head())

df[["age"]].head() # Tek değişken seçimi yapmak istediğimizde tek köşeli parantez kullanmalıyız.

type(df[["age"]].head())

df[["age","alive"]]

col_names = ["age","adult_male","alive"]
df[col_names]

df["age2"] = df["age"] ** 2 # Yeni değişken oluşturmak için değişkenler üzerinde işlem yapabiliriz.
df["age3"] = df["age"] / df["age2"]
df.head()

df.drop("age2", axis = 1).head()

df.drop(col_names, axis = 1)

df.loc[:, ~df.columns.str.contains("age")].head() # .loc[] ile satır ve sütun seçimi yapabiliriz. ~ ile değişken isimlerinde ... geçenleri seçmeyebiliriz.


# LOC ve ILOC
"""
iloc integer based selection
loc label based selection
loc[] ile verilen indexlere göre seçim yapabiliriz. Verilen indexi de seçer. string indexlerde kullanılabilir.
iloc[] ile indexlere göre seçim yapabiliriz. Verilen indexi seçmez. Sadece indexler arasındaki değerleri seçer.
"""
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df.iloc[0:3]
df.iloc[0, 0]

df.loc[0:3]

df.iloc[0:3,0:3]
df.loc[0:3,"age"]


col_names = ["age","embarked","alive"]
df.loc[0:3,col_names]


# Koşullu Eleman İşlemleri

df = sns.load_dataset("titanic")
df.head()

# Yaşı 50'den büyük olanları seçelim.

df[df["age"] > 50].head()

# Yaşı 50'den büyük kaç kişi var?
df[df["age"] > 50]["age"].count()

# Yaşı 50'den büyük class değerlerini seçelim.
df.loc[df["age"] > 50, "class"].head()
df.loc[df["age"] > 50, ["age","class"]].head()

# Yaşı 50'den büyük ve erkek olanları seçelim.

df.loc[(df["age"] > 50) & (df["sex"] == "male"),["age","class"]].head()

# Yaşı 50'den büyük ve erkek olanları ve Cherbourg'dan binenleri seçelim.
df.loc[(df["age"] > 50) &
       (df["sex"] == "male") &
       (df["embark_town"] == "Cherbourg") ,
       ["age","class","embark_town"]].head()

# Yaşı 50'den büyük ve erkek olanları ve Cherbourg'dan ya da  Southampton'tan binenleri seçelim.
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()

# Toplulaştırma ve Gruplama
"""
- count() : Değişkenin kaç gözlemi olduğunu gösterir.
- first(), last() : Değişkenin ilk ve son gözlemini gösterir.
- mean(), median() : Değişkenin ortalamasını ve medyanını gösterir.
- min(), max() : Değişkenin minimum ve maksimum değerini gösterir.
- std(), var() : Değişkenin standart sapmasını ve varyansını gösterir.
- sum() : Değişkenin toplamını gösterir.
- pivot_table() : Değişkenlerin birbirleriyle ilişkisini gösterir.
"""

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()


df["age"].mean()

df.groupby("sex")["age"].mean() # .groupby() ile değişkenleri gruplayabiliriz.

df.groupby("sex").agg({"age":"mean"}) # .agg() ile gruplara ait istediğimiz istatistikleri görebiliriz.

df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],"embark_town": "count"})
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                       "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})


# Pivot Table
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()
"""
.pivot_table() ile değişkenlerin birbirleriyle ilişkisini görebiliriz.
"""
df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", ["embarked", "class"])

df.head()

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90]) # .cut() ile değişkenleri belirli aralıklara bölebiliriz.

df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option('display.width', 500) # .set_option() ile gösterim ayarları yapabiliriz.

# Apply ve Lambda Fonksiyonu

df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()

# Birleştirme (Join) İşlemleri
import numpy as np
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"]) # .DataFrame() ile veri çerçevesi oluşturabiliriz.
df2 = df1 + 99
pd.concat([df1, df2]) # .concat() ile iki veri çerçevesini birleştirebiliriz.

pd.concat([df1, df2], ignore_index=True) # ignore_index=True ile indeksleri sıfırlayabiliriz.

# Merge İşlemleri
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})
pd.merge(df1, df2) # .merge() ile iki veri çerçevesini birleştirebiliriz.
pd.merge(df1, df2,on="employees")  # on parametresi ile hangi değişken üzerinden birleştirileceğini belirleyebiliriz.

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)