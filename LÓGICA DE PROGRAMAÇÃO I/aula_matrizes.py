# Matrizes

matriz = [
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9],
]
print(matriz[0][0])

# Questão 9 da Lista 2

from random import randint

matriz = []

for linha in range(5):
    lista_auxiliar = []
    for coluna in range(5):
        lista_auxiliar.append(randint(1, 100))
    matriz.append(lista_auxiliar)

for m in matriz:
    print(m)

maior = {'mv': 0, 'linha': None, 'coluna': None}

for linha in matriz:
    for coluna in linha:
        if coluna > maior['mv']:
            maior['mv'] = coluna
            maior['linha'] = matriz.index(linha)
            maior['coluna'] = linha.index(coluna)

print(maior)