# %%
import pandas as pd

df = pd.read_csv("data/points_tmw.csv")
df.head()

# %%

print("Estatísticas de Posição para Transacoes:")

minimo = df["qtdPontos"].min()
print("Mínimo:", minimo)

media = df["qtdPontos"].mean()
print("Média:", media)

quartil_1 = df["qtdPontos"].quantile(0.25)
print("1o Quartil:", quartil_1)

mediana = df["qtdPontos"].median()
print("Mediana:", mediana)

quartil_3 = df["qtdPontos"].quantile(0.75)
print("3o Quartil:", quartil_3)

maximo = df["qtdPontos"].max()
print("Máximo:", maximo)

variancia = df["qtdPontos"].var()
print("Variância:", variancia)

desvio_padrao = df["qtdPontos"].std()
print("Desvio Padrão:", desvio_padrao)

amplitude = df["qtdPontos"].max() - df["qtdPontos"].min()
print("Amplitude:", amplitude)

df["qtdPontos"].describe()

# %%

print("\n\n##########################\n")
print("Estatísticas de Posição para Usuários:\n")

usuarios = (df.groupby(["idUsuario"])
              .agg({
        "idTransacao":"count",
        "qtdPontos":"sum",
    }).reset_index())

# %%

summario = usuarios[['idTransacao', 'qtdPontos']].describe()
print(summario.to_string())