import pandas as pd

base = pd.read_csv('credit_data.csv')
base = base.dropna()

from pyod.models.knn import KNN
detector = KNN()
detector.fit(base.iloc[:,1:4])

previsoes = detector.labels_
confianca_previsoes = detector.decision_scores_

outliers = []
for i in range(len(previsoes)):
    #print(previsoes[i])
    if previsoes[i] == 1:
        outliers.append(i)
        
lista_outliers = base.iloc[outliers, :]
    