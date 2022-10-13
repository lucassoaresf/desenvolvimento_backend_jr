# Exemplo de dicionario
nome = {'nome': 'Lucas', 'idade': 26, 'email': 'lucassoaresf@outlook.com'}
print(nome['nome'])
print(nome['idade'])
nome['cidade'] = 'Itabaiana'
print(nome)
print(f"O email é: {nome['email']}")
del nome['idade']
print(nome)

comida = {
    'Ste': 'Sushi',
    'Alenira': 'Bolo',
    'Arleide': 'Café',
    'Lucas': 'Churrasco'
}
print(comida)