import pandas as pd

base = pd.read_csv('risco_credito2.csv')
previsores = base.iloc[:,0:4].values
classe = base.iloc[:,4].values
                  
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])

from sklearn.linear_model import LogisticRegression
classificador = LogisticRegression()
classificador.fit(previsores, classe)
print(classificador.intercept_)
print(classificador.coef_)

# história boa, dívida alta, garantias nenhuma, renda > 35
# história ruim, dívida alta, garantias adequada, renda < 15
resultado = classificador.predict([[0,0,1,2], [3, 0, 0, 0]])
resultado2 = classificador.predict_proba([[0,0,1,2], [3, 0, 0, 0]])
print(resultado)
print(resultado2)