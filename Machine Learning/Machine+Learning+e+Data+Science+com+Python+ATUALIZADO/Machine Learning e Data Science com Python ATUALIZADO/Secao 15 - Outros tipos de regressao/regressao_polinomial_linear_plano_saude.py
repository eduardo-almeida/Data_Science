import pandas as pd
import numpy as np

base = pd.read_csv('plano_saude2.csv')

X = base.iloc[:, 0:1].values
y = base.iloc[:, 1].values

# Regressão linear simples
from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(X, y)
score1 = regressor1.score(X, y)

regressor1.predict(np.array(40).reshape(1, -1))

import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.plot(X, regressor1.predict(X), color = 'red')
plt.title('Regressão linear')
plt.xlabel('Idade')
plt.ylabel('Custo')

# Regressão polinomial
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 4)
X_poly = poly.fit_transform(X)

regressor2 = LinearRegression()
regressor2.fit(X_poly, y)
score2 = regressor2.score(X_poly, y)

regressor2.predict(poly.transform(np.array(40).reshape(1, -1)))

plt.scatter(X, y)
plt.plot(X, regressor2.predict(poly.fit_transform(X)), color = 'red')
plt.title('Regressão polinomial')
plt.xlabel('Idade')
plt.ylabel('Custo')