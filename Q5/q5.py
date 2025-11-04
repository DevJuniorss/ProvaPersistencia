from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    conteudo = file.read()

soup = BeautifulSoup(conteudo, "html.parser")

linhas = soup.find_all("tr")[1:]
vitorias_player1 = 0

def jogador1_vence(p1, p2):
    p1 = p1.strip().lower()
    p2 = p2.strip().lower()
    if (p1 == "pedra" and p2 == "tesoura") \
       or (p1 == "tesoura" and p2 == "papel") \
       or (p1 == "papel" and p2 == "pedra"):
        return True
    return False

for linha in linhas:
    colunas = linha.find_all("td")
    if len(colunas) != 2:
        continue

    jog1 = colunas[0].text.strip()
    jog2 = colunas[1].text.strip()

    if jogador1_vence(jog1, jog2):
        vitorias_player1 += 1

print(f"Vitórias do Jogador 1: {vitorias_player1}")