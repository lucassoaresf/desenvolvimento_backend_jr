# Criando um caminho para leitura
path = "path/"
file = "arquivo.txt"

file_path = path + file

with open(file_path, "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

# Abrindo um arquivo para leitura
with open("path/arquivo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)
