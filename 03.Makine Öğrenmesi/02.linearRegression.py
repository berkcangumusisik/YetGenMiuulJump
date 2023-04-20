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

# Tahmin Başarısı
y_pred = regModel.predict(X)
mean_squared_error(Y, y_pred)
Y.mean()
Y.std() # standart sapma

# RMSE => Kök Ortalama Kare Hatası
np.sqrt(mean_squared_error(Y, y_pred))

# MAE => Ortalama Mutlak Hata
mean_absolute_error(Y, y_pred)

# R-Kare => Modelin başarı oranı. Bağımlı değişkenin varyansının % kaçını açıklıyor.
regModel.score(X, Y)

# Çoklu Doğrusal Regresyon

df = pd.read_csv("03.Makine Öğrenmesi/datasets/advertising.csv")

X = df.drop("sales", axis=1)
y = df[["sales"]]

# Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1) # Burada random_state=1 vermemizin sebebi her seferinde aynı sonuçlar almak için.
X_train.shape
X_test.shape
y_train.shape

reg_model = LinearRegression().fit(X_train, y_train)

# sabit (b - bians)
reg_model.intercept_

# coefficients (w - weights)
reg_model.coef_


# Tahmin
"""
Aşağıdaki gözşem değerlerine göre satışın beklenen değeri nedir?

TV = 30
Radio = 10
Newspaper = 40
Sales = 2.90 + TV * 0.04 + Radio * 0.17 + Newspaper * 0.002
"""
2.90 + 30*0.04 + 10*0.17 + 40*0.002
yeni_veri = [[30], [10], [40]]
yeni_veri = pd.DataFrame(yeni_veri).T
reg_model.predict(yeni_veri)


# Tahmin Başarısını Değerlendirme
y_pred = reg_model.predict(X_train)
np.sqrt(mean_squared_error(y_train, y_pred))


# TRAIN R-Kare
reg_model.score(X_train, y_train)
# Yeni değişken eklenince R-Kare değeri arttı.

# TEST RMSE
y_pred = reg_model.predict(X_test)
np.sqrt(mean_squared_error(y_test, y_pred))

# TEST R-Kare
reg_model.score(X_test, y_test)

# 10 Katlı CV RMSE
np.mean(np.sqrt(-cross_val_score(reg_model, X, y, cv=10, scoring="neg_mean_squared_error")))

# 5 Katlı CV R-Kare
np.mean(np.sqrt(-cross_val_score(reg_model, X, y, cv=5, scoring="neg_mean_squared_error")))

# Gradient Descent ile Doğrusal Regresyon
def cost_function(Y,b,w,X):
   m = len(Y)
   sse = 0
   for i in range(m):
       y_hat = b + w * X[i]
       y = Y[i]
       sse += (y_hat - y) ** 2
   mse = sse / m
   return mse

def update_weights(Y, b, w, X, learning_rate):
   m = len(Y)
   b_deriv_sum = 0
   w_deriv_sum = 0
   for i in range(m):
       y_hat = b + w * X[i]
       y = Y[i]
       b_deriv_sum += (y_hat - y)
       w_deriv_sum += (y_hat - y) * X[i]
   new_b = b - (learning_rate * b_deriv_sum) / m
   new_w = w - (learning_rate * w_deriv_sum) / m
   return new_b, new_w

def train(Y, initialB, initialW, X, learningRate, num_iters):

    print("Starting gradient descent at b = {0}, w = {1}, mse = {2}".format(initialB, initialW,
                                                                   cost_function(Y, initialB, initialW, X)))

    b = initialB
    w = initialW
    costHistory = []

    for i in range(num_iters):
        b, w = update_weights(Y, b, w, X, learningRate)
        mse = cost_function(Y, b, w, X)
        costHistory.append(mse)


        if i % 100 == 0:
            print("iter={:d}    b={:.2f}    w={:.4f}    mse={:.4}".format(i, b, w, mse))


    print("After {0} iterations b = {1}, w = {2}, mse = {3}".format(num_iters, b, w, cost_function(Y, b, w, X)))
    return costHistory, b, w

df = pd.read_csv("03.Makine Öğrenmesi/datasets/advertising.csv")

X = df["radio"]
Y = df["sales"]

# hyperparameters
learning_rate = 0.001
initial_b = 0.001
initial_w = 0.001
num_iters = 100000

cost_history, b, w = train(Y, initial_b, initial_w, X, learning_rate, num_iters)
