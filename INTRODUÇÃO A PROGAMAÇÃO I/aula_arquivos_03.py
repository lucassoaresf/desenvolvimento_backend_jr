# Escrita

filename = "path/arquivo_escrita.txt"

with open(filename, "w") as file_object:
    file_object.write("Quero dormir!\n")
    file_object.write("Tô com sono!")
