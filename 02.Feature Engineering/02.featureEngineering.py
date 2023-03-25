# Outliers (Aykırı Değerler)
"""
- Verideki genel eğilimin oldukça dışına çıkan değerlerdir.
- Aykırı değerler veri setinin doğruluğunu etkileyebilir.
- Aykırı deperkerş ayıklamak için yöntemler vardır.
    * Sektör bilgisi
    * Standart Sapma Yaklaşımı
    * Z Skor Yaklaşımı
    * Boxplot (interquartile range - IQR)

Boxplot (interquartile range - IQR)
- Aykırı değerlerin bulunması için kullanılır.
- Lower Limit = Q1 - 1.5 * IQR
- Upper Limit = Q3 + 1.5 * IQR
- Minimum değeri Q1 - 1.5 * IQR değerinden küçükse aykırı değerdir.
- Maximum değeri Q3 + 1.5 * IQR değerinden büyükse aykırı değerdir.

"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# !pip install missingno
import missingno as msno
from datetime import date
# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
# from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

def load_application_train():
    data = pd.read_csv("02.Feature Engineering/datasets/application_train.csv")
    return data

df = load_application_train()
df.head()


def load():
    data = pd.read_csv("02.Feature Engineering/datasets/titanic.csv")
    return data

df = load()
df.head()

# 1. Outliers (Aykırı Değerler)

# Aykırı Değerleri Yakalama

sns.boxplot(x=df["Age"])
plt.show()

# Aykırı Değerleri Hesaplama
q1 = df["Age"].quantile(0.25) # quantile = yüzdelik
q3 = df["Age"].quantile(0.75)
iqr = q3 - q1

up = q3 + 1.5 * iqr
low = q1 - 1.5 * iqr
df[(df["Age"] > up) | (df["Age"] < low)].any(axis = None) # any = herhangi biri

df[~((df["Age"] > up) | (df["Age"] < low))].any(axis = None) # ~ = değil
df[(df["Age"] < low)].any(axis = None)

"""
1. Eşik değer belirledik.
2.Aykırılara eriştik
3. Aykırı değer var mı diye kontrol ettik.
"""


# İşlemleri Fonksiyonlaştırma
def outlier_thresholds(dataframe, col_name, q1 = 0.25, q3 = 0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

outlier_thresholds(df, "Age")

low, up = outlier_thresholds(df, "Age")

df[(df["Fare"] > up) | (df["Fare"] < low)].head()
df[(df["Fare"] > up) | (df["Fare"] < low)].index

def check_outlier(dataframe,col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit)].any(axis = None):
        return True
    else:
        return False

check_outlier(df, "Age")

# grab_col_names
dff = load_application_train()
dff.head()

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)

num_cols = [col for col in num_cols if col not in "PassengerId"]

for col in num_cols:
    print(col, check_outlier(df, col))

cat_cols, num_cols, cat_but_car = grab_col_names(dff)
num_cols = [col for col in num_cols if col not in "SK_ID_CURR"]

for col in num_cols:
    print(col, check_outlier(dff, col))

# Aykırı Değerler Var Mı Yok Mu

def grab_outliers(dataframe, col_name, index=False):
    low, up = outlier_thresholds(dataframe, col_name)

    if dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].shape[0] > 10:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].head())
    else:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))])

    if index:
        outlier_index = dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].index
        return outlier_index

grab_outliers(df, "Age")

age_index = grab_outliers(df,"Age", True)
check_outlier(df, "Age")
grab_outliers(df, "Fare", True)

# Aykırı Değer Problemini Çözmek
# Aykırı Değerleri Silme

low , up = outlier_thresholds(df, "Fare")
df[~((df["Fare"] < low) | (df["Fare"] > up))].shape

def remove_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    df_without_outliers = dataframe[~((dataframe[col_name] < low_limit) | (dataframe[col_name] > up_limit))]
    return df_without_outliers

cat_cols, num_cols, cat_but_car = grab_col_names(df)
num_cols = [col for col in num_cols if col not in "PassengerId"]

for col in num_cols:
    new_df = remove_outlier(df, col)

df.shape[0] - new_df.shape[0]

# Baskılama Yöntemi ile Aykırı Değer Problemini Çözmek (re-assigment with threshold values)
# veri setindeki aykırı değerleri sınır değerler ile değiştirmektir. Veri kaybı yaşanmaz.

low, up = outlier_thresholds(df, "Fare")
df[((df["Fare"] < low) | (df["Fare"] > up))]["Fare"]
df.loc[((df["Fare"] < low) | (df["Fare"] > up)), "Fare"]

df.loc[(df["Fare"] > up), "Fare"] = up
df.loc[(df["Fare"] < low), "Fare"] = low


def replace_with_thresholds(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    dataframe.loc[(dataframe[col_name] < low_limit), col_name] = low_limit
    dataframe.loc[(dataframe[col_name] > up_limit), col_name] = up_limit

df = load()
cat_cols, num_cols, cat_but_car = grab_col_names(df)
num_cols = [col for col in num_cols if col not in "PassengerId"]

df.shape

for col in num_cols:
    print(col, check_outlier(df, col))

for col in num_cols:
    replace_with_thresholds(df, col)

# Recap
df = load()
outlier_thresholds(df, "Age")
check_outlier(df, "Age")
grab_outliers(df, "Age",index=True)
remove_outlier(df, "Age").shape
replace_with_thresholds(df, "Age")


#Çok Değişkenli Aykırı Değer Analizi : Local Outlier Factor (LOF)
"""
Yaş tek başına 17 olursa aykırı değer değildir. Ama 17 yaşında olup 3 kez evlenmek bir aykırı değerdir.

Local Outlier Factor (LOF) yöntemi, 
- Gözlemleri bulundukları konumda yoğunluk tabanlı skorlayarak buna göre aykırı değer olabilecek tanımlayabilmemize imkan sağlıyor.
- Eğer bir nokta komşularının yoğunluğundan anlamlı bir şekilde düşük ise bu nokta komşularından daha seyrek bir bölgede bulunuyordur yorumu yapılıyor. Dolayısıyla burada bir komşuluk yapısı söz konusu. Bir değerin çevresi yoğun değilse demek ki bu değer aykırı değerdir şeklinde değerlendiriliyor.
"""

# Veri setini tanımlayalım.
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include=['float64', 'int64'])
df = df.dropna()
df.head()

for col in df.columns:
    print(col , check_outlier(df, col))
low, up = outlier_thresholds(df, "carat")
df[((df['carat'] < low) | (df['carat'] > up))].shape
low, up = outlier_thresholds(df, "depth")
df[((df['depth'] < low) | (df['depth'] > up))].shape

clf = LocalOutlierFactor(n_neighbors=20)
# n_neighbors aranan komşuluk sayısıdır. genellikle 20 olarak kullanılır.
# LOF u veri setine uygulamak için
print(clf.fit_predict(df))

# Lof değerlerini takip edebilmek için
df_scores = clf.negative_outlier_factor_ # -1 ile 1 arasında değerler alır.
print(df_scores)

# Eksi değerli gözükmesini istemiyorsak
# df_scores = -df_scores

print(np.sort(df_scores)[0:5])
scores = pd.DataFrame(np.sort(df_scores))
scores.plot(stacked=True,xlim=[0,20],style=".-")
plt.show()
# Daha detaylı bakalım.
scores.plot(stacked=True,xlim=[0,50],style=".-")
plt.show()
# Grafiğe bakarak kırılma noktasını belirleyelim.
th = np.sort(df_scores)[3]
df[df_scores < th]
# Bunlar neden aykırı?
df.describe([0.01,0.05,0.75,0.9,0.99]).T

