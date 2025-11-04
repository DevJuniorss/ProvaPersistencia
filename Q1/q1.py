with open("dados_alunos.txt", "r", encoding="utf-8") as file:
    linhas = file.readlines()

    alunos = []
    notas = []

for linha in linhas:
    linha = linha.strip()
    partes = linha.split("#")
    if len(partes) != 3:
        print(f"Linha ignorada (formato inválido): {linha}")
        continue

    nome = partes[0]
    curso = partes[1]
    nota = float(partes[2])

    alunos.append({"nome": nome, "curso": curso, "nota": nota})
    notas.append(nota)

if len(alunos) == 0:
    print("Arquivo vazio.")
else:
    media = sum(notas) / len(notas)
    maior_nota = max(alunos, key=lambda a: a["nota"])
    menor_nota = min(alunos, key=lambda a: a["nota"])

    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior_nota['nota']} ({maior_nota['nome']})")
    print(f"Menor nota: {menor_nota['nota']} ({menor_nota['nome']})")