"""
Feature Extraction(Özellik Çıkarımı)
Ham veriden değişken türetmektir.
Yapısal veriden değişken türetmek
Mevcut değişken üzerinden veri türetmek
Yapısal olmayan veriden değişken türetmek
Yazı, ses, görüntü gibi veri üzerinden veri türetmek
"""

# Binary Features : Flag, Bool, True - False

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# !pip install missingno
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)
pd.options.display.max_columns = None

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

df["NEW_CABIN_BOOL"] = df["Cabin"].notnull().astype('int')

df.groupby("NEW_CABIN_BOOL").agg({"Survived": "mean"})


from statsmodels.stats.proportion import proportions_ztest
test_stat, pvalue = proportions_ztest(count=[df.loc[df["NEW_CABIN_BOOL"] == 1, "Survived"].sum(),
                                             df.loc[df["NEW_CABIN_BOOL"] == 0, "Survived"].sum()],

                                      nobs=[df.loc[df["NEW_CABIN_BOOL"] == 1, "Survived"].shape[0],
                                            df.loc[df["NEW_CABIN_BOOL"] == 0, "Survived"].shape[0]])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


df.loc[((df['SibSp'] + df['Parch']) > 0), "NEW_IS_ALONE"] = "NO"
df.loc[((df['SibSp'] + df['Parch']) == 0), "NEW_IS_ALONE"] = "YES"

df.groupby("NEW_IS_ALONE").agg({"Survived": "mean"})


test_stat, pvalue = proportions_ztest(count=[df.loc[df["NEW_IS_ALONE"] == "YES", "Survived"].sum(),
                                             df.loc[df["NEW_IS_ALONE"] == "NO", "Survived"].sum()],

                                      nobs=[df.loc[df["NEW_IS_ALONE"] == "YES", "Survived"].shape[0],
                                            df.loc[df["NEW_IS_ALONE"] == "NO", "Survived"].shape[0]])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Text Features - Text'ler üzerinden özellik türetmek

df = load()
df.head()

# Letter Count
df["NEW_NAME_COUNT"] = df["Name"].str.len() #str.len() ile name alanının kaç karakter olduğunu buluyoruz.
df.head()

# Word Count
df["NEW_NAME_WORD_COUNT"] = df["Name"].apply(lambda x: len(str(x).split(" "))) #name alanının kaç kelime olduğunu buluyoruz.
df.head()

# Özel Yapıları Yakalamak
df["NEW_NAME_DR"] = df["Name"].apply(lambda x: len([x for x in x.split() if x.startswith("Dr")]))
df.head()
df.groupby("NEW_NAME_DR").agg({"Survived": ["mean","count"]})

# Regex ile Değişken Türetmek
df['NEW_TITLE'] = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
df[["NEW_TITLE", "Survived", "Age"]].groupby(["NEW_TITLE"]).agg({"Survived": "mean", "Age": ["count", "mean"]})

# Data Features - Tarihler üzerinden özellik türetmek

dff = pd.read_csv("02.Feature Engineering/datasets/course_reviews.csv")
dff.head()
dff.info()
dff['Timestamp'] = pd.to_datetime(dff["Timestamp"], format="%Y-%m-%d") #Timestamp alanının formatını değiştiriyoruz.
dff.head()

#year
dff["year"] = dff["Timestamp"].dt.year
dff.head()

#month
dff["month"] = dff["Timestamp"].dt.month
dff.head()

# year diff
dff['yearDiff'] = date.today().year - dff['Timestamp'].dt.year #date.today().year ile bugunun yılını alıyoruz.
dff.head()

# month diff (iki tarih arasındaki ay farkı): yıl farkı + ay farkı
dff['monthDiff'] = (date.today().year - dff['Timestamp'].dt.year) * 12 + date.today().month - dff['Timestamp'].dt.month
dff.head()

# day name
dff['dayName'] = dff['Timestamp'].dt.day_name() #Timestamp alanının day name alanına göre day name alanına atıyoruz.
dff.head()

#Feature Interactions (Özellik Etkileşimleri)
df = load()
df.head()

df["NEW_AGE_PCLASS"] = df["Age"] * df["Pclass"]
df["NEW_FAMILY_SIZE"] = df["SibSp"] + df["Parch"] + 1
df.loc[(df["Sex"] == "male") & (df["Age"] <= 21), "NEW_SEX_CAT"] = "youngmale"
df.loc[(df["Sex"] == "male") & (df["Age"] > 21) & (df["Age"] <= 50), "NEW_SEX_CAT"] = "maturemale"
df.loc[(df["Sex"] == "male") & (df["Age"] > 50), "NEW_SEX_CAT"] = "seniormale"
df.loc[(df["Sex"] == "female") & (df["Age"] <= 21), "NEW_SEX_CAT"] = "youngfemale"
df.loc[(df["Sex"] == "female") & (df["Age"] > 21) & (df["Age"] <= 50), "NEW_SEX_CAT"] = "maturefemale"
df.loc[(df["Sex"] == "female") & (df["Age"] > 50), "NEW_SEX_CAT"] = "seniorfemale"
df.head()

df.groupby("NEW_SEX_CAT")["Survived"].mean()
