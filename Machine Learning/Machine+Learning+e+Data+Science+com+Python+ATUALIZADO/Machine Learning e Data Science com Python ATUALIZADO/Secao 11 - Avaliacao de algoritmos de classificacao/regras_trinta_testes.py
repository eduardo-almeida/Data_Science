import pandas as pd
import Orange
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

base = Orange.data.Table('credit_data.csv')

resultados30 = []
for i in range(30):
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state = i)
    resultados1 = []
    for indice_treinamento, indice_teste in kfold.split(base, np.zeros(shape=(2000, 1))):
        cn2_learner = Orange.classification.rules.CN2Learner()
        classificador = cn2_learner(base[indice_treinamento])
        previsoes = classificador(base[indice_teste])
        
        precisao = accuracy_score(base.Y[indice_teste], previsoes)
        resultados1.append(precisao)
    resultados1 = np.asarray(resultados1)
    media = resultados1.mean()
    resultados30.append(media)
    
resultados30 = np.asarray(resultados30)    
resultados30.mean()
for i in range(resultados30.size):
    print(str(resultados30[i]).replace('.', ','))

