# Contador de palavras de livros

def contador_palavras(filename):

    with open(filename, "r", encoding="utf-8") as file_object:
        conteudo = file_object.read()

    palavras = conteudo.split()

    return len(palavras)

while True:

    option = int(input(
        "1 - The Prince\n"
        "2 - Hamlet\n"
        "3 - Darkwater\n"
        "4 - A Little Princess\n"
        "5 - Grimm's\n"
        "0 - Sair \n"
        "Escolha uma opção: "
    ))

    if option == 1:
        print(f"O livro The Prince possui {contador_palavras('the_prince.txt')} palavras.")
    elif option == 2:
        print(f"O livro Hamlet possui {contador_palavras('hamlet.txt')} palavras.")
    elif option == 3:
        print(f"O livro Darkwater possui {contador_palavras('darkwater.txt')} palavras.")
    elif option == 4:
        print(f"O livro A Little Princess possui {contador_palavras('little_prince.txt')} palavras.")
    elif option == 5:
        print(f"O livro Grimm`ss possui {contador_palavras('grimm.txt')} palavras.")
    else:
        break
