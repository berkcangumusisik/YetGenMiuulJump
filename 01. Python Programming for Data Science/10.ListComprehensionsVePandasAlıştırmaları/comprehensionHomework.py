# Görev 1
"""
List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
harfe çeviriniz ve başına NUM ekleyiniz.
Beklenen Çıktı:
['NUM_TOTAL', 'NUM_SPEEDING', 'NUM_ALCOHOL', 'NUM_NOT_DISTRACTED', 'NUM_NO_PREVIOUS', 'NUM_INS_PREMIUM', 'NUM_INS_LOSSES', 'ABBREV']
"""
import seaborn as sns
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

df = sns.load_dataset("car_crashes")
df.info()

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

# Görev 2
"""
List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
değişkenlerin isimlerinin sonuna "FLAG" yazınız.
Beklenen Çıktı:
['TOTAL_FLAG', 'SPEEDING_FLAG', 'ALCOHOL_FLAG', 'NOT_DISTRACTED_FLAG', 'NO_PREVIOUS_FLAG', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV_FLAG']
"""

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


# Görev 3
"""
List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz

Beklenen Çıktı:
total speeding alcohol not_distracted ins_premium ins_losses
18.800 7.332    5.640      18.048       784.550     145.080
18.100 7.421    4.525      16.290       1053.480     133.930
18.600 6.510    5.208      15.624       899.470     110.350
22.400 4.032    5.824      21.056       827.340     142.390
12.000 4.200    3.360      10.920       878.410     165.630

Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.
"""


og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


