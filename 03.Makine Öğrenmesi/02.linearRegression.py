import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv("03.Makine Öğrenmesi/datasets/advertising.csv")
df.head()

X = df[["TV"]]
Y = df["sales"]

# Model
regModel = LinearRegression().fit(X, Y)
#sabit (b- bians)
regModel_intercept = regModel.intercept_
print(regModel_intercept)

regModel.coef_

# 150 birimlik TV harcaması olsa ne kadar satış olması beklenir?

regModel.intercept_ + regModel.coef_*150

# 500 birimlik tv harcaması olsa ne kadar satış olur?

regModel.intercept_ + regModel.coef_*500

df.describe().T

# Modelin Görselleştirilmesi
g = sns.regplot(x=X, y=Y, scatter_kws={'color': 'b', 's': 9},
                ci=False, color="r")

g.set_title(
    f"Model Denklemi: Sales = {round(regModel.intercept_, 2)} + TV*{round(regModel.coef_, 2)}")
g.set_ylabel("Satış Sayısı")
g.set_xlabel("TV Harcamaları")
plt.xlim(-10, 310)
plt.ylim(bottom=0)
plt.show()