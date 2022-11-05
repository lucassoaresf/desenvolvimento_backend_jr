import csv

maior_bilheteria = 0
maior_renda = 0.0
filme, filme_b = '', ''
lista_selecionada = []

with open("filmes.csv", newline='', encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        if linha[9] != "Renda (R$) no ano de exibição":
            if maior_renda < float(linha[9]):
                maior_renda = float(linha[9])
                filme = linha[2]

            if maior_bilheteria < int(float(linha[8])):
                maior_bilheteria = int(float(linha[8]))
                filme_b = linha[2]


print(f"O filme {filme} teve a renda de R$ {maior_renda}")
print(f"O filme {filme_b} teve a bilheteria de {maior_bilheteria}")

