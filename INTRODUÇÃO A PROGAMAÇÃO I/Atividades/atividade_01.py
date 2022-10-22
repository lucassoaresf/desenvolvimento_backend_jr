# Criando um programa que realiza a contagem de quantas palavras existem em um livro.

filename = "the_prince.txt"

with open(filename, "r", encoding="utf-8") as file_object:
    conteudo = file_object.read()

quantidade_palavras = conteudo.split()
print(len(quantidade_palavras))