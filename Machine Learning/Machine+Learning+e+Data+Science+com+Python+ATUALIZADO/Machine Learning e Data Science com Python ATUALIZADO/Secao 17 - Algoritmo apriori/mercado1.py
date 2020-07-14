import pandas as pd

dados = pd.read_csv('mercado.csv', header = None)
transacoes = []
for i in range(0, 10):
    transacoes.append([str(dados.values[i,j]) for j in range(0, 4)])

from apyori import apriori
regras = apriori(transacoes, min_support = 0.3, min_confidence = 0.8, min_lift = 2, min_length = 2)

resultados = list(regras)
resultados

resultados2 = [list(x) for x in resultados]
resultados2
resultadoFormatado = []
for j in range(0, 5):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
resultadoFormatado
