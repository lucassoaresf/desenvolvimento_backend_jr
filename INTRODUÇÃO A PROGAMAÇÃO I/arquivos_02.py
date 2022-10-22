# Caminho e nome do arquivo guardado na variável
file = "path/arquivo.txt"

# Abrindo um arquivo como leitura
with open(file, "r", encoding="utf-8") as file_object:

    # Criando uma "repetição" para ler por linhas
    for linha in file_object:

        print(linha.rstrip())