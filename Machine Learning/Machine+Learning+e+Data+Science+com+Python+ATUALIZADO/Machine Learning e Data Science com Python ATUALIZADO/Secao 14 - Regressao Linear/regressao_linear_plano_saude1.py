import pandas as pd
import numpy as np

base = pd.read_csv('plano_saude.csv')

X = base.iloc[:, 0].values
y = base.iloc[:, 1].values

import numpy as np
correlacao = np.corrcoef(X, y)

X = X.reshape(-1,1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

# b0
regressor.intercept_

# b1
regressor.coef_

import matplotlib.pyplot as plt
plt.scatter(X, y)
plt.plot(X, regressor.predict(X), color = 'red')
plt.title ("Regressão linear simples")
plt.xlabel("Idade")
plt.ylabel("Custo")

# previsão pessoa com 40 anos
previsao1 = regressor.intercept_ + regressor.coef_ * 40
previsao2 = regressor.predict(np.array(40).reshape(1, -1))

score = regressor.score(X,y)

from yellowbrick.regressor import ResidualsPlot
visualizador = ResidualsPlot(regressor)
visualizador.fit(X, y)
visualizador.poof()
