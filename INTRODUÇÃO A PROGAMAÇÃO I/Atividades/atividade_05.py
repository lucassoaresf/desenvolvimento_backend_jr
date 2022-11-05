import csv

lista = []
filme = ''
maior_renda = 0.0

with open("filmes.csv", newline='', encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        if linha[9] != "Renda (R$) no ano de exibição":
            if maior_renda < float(linha[9]):
                maior_renda = float(linha[9])
                filme = linha[2]


print(f"O filme {filme} teve a renda de R${maior_renda}")

