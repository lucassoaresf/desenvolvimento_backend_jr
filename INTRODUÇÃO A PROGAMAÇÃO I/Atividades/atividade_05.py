import csv

lista = []
filme = ''
maior_renda = 0.0

with open("filmes.csv", newline='', encoding="utf-8") as f:
    leitor = csv.reader(f)
    for i in leitor:
        if i[1] != "Ano de exibição":
            if maior_renda < float(i[9]):
                filme = i[2]
                maior_renda = float(i[9])


print(f"Nome do filme: {filme} e Renda: {maior_renda}")

