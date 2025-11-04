import pandas as pd

nomes = ["Luca Brasi", "Peter Clemenza", "Sal Tessio", "Tom Hagen", "Michael Corleone"]
receitas = [12000, 17500, 14300, 16000, 19500]

dados = pd.Series(receitas, index=nomes)
print("-------------------------------")
print("Dinheiro da Semana em Doletas:")
print(dados)
print("-------------------------------")
print("\n")
print("-------------------------------")
total = dados.sum()
print(f"Dinheiro da protecao da semana: ${total}")
print("-------------------------------")
print("\n")
print("-------------------------------")
media = dados.mean()
print(f"Média: ${media:.2f}")
print("-------------------------------")
print("\n")
print("-------------------------------")
maior_nome = dados.idxmax()
maior_valor = dados.max()
print(f"Maior valor: {maior_nome} (${maior_valor})")
print("-------------------------------")
print("\n")
print("-------------------------------")
acima_media = dados[dados > media]
print("Membro da familia que recebeu acima da media:")
print(acima_media)
print("-------------------------------")