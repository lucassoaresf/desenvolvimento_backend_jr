# Cadastro de Pessoas - PROJETO

import json
from loguru import logger

def salvar_database(database):
    with open("arquivo.json", 'w', encoding='utf-8') as f:
        json.dump(database, f)

def lista_cadastro(database):
    if len(database) == 0:
        print("Não existem cadastros!!!")

    else:
        for i in database.keys():
            s = f"Código: {i} | " \
                f"Nome: {database[i]['nome']} | " \
                f"Email: {database[i]['email']} | " \
                f"Data: {database[i]['data']}"


            print(s)

database = {}

while True:
    try:
        option = int(input(
            "1 - Cadastrar uma pessoa\n"
            "2 - Listar os cadastros\n"
            "3 - Deletar um cadastro\n"
            "4 - Alterar um cadastro\n"
            "5 - Salvar o database\n"
            "0 - Sair do Programa\n"
            "Digite sua opção: "
        ))

        if option == 1:
            codigo = int(input("Digite seu código de segurança: "))
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            data = input("Digite o dia/mês do seu nascimento: ")

            database[codigo] = {"nome": nome,
                                "email": email,
                                "data": data}
            print("\n")
            logger.success("Cadastro realizado com sucesso!!!")


        elif option == 2:
            print(" --- LISTAGEM DE CADASTROS --- ")
            lista_cadastro(database)
            print("\n")
            logger.info("Listagem finalizada.")


        elif option == 3:
            print(" --- Selecione o item a ser deletado --- ")
            lista_cadastro(database)
            codigo = int(input("Digite o código a ser deletado: "))
            del database[codigo]
            print("\n")
            logger.success("Deletado com sucesso!!!")


        elif option == 4:
            print(" --- Selecione o item a ser alterado --- ")
            lista_cadastro(database)
            codigo = int(input("Digite o código a ser alterado --- "))
            op = int(input(
                "1 - Nome\n"
                "2 - Email\n"
                "3 - Data\n"
                "O que você deseja alterar: "))
            print("\n")
            logger.success("Alterações realizadas com sucesso!!!")


            if op == 1:
                nome = input("Digite o novo nome: ")
                database[codigo]['nome'] = nome
            if op == 2:
                email = input("Digite o novo email: ")
                database[codigo]['email'] = email
            if op == 3:
                data = input("Digite o novo data: ")
                database[codigo]['data'] = data

        elif option == 5:
            salvar_database(database)
            logger.success("Database salva com sucesso!!!")

        elif option == 0:
            break

    except ValueError as error:
    logger.error(f"Valor inválido: {error}")

    except Exception as error:
        logger.error(f"Error: {error}")
        continue