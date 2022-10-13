''' # Funções

def somar(num1, num2):
    resultado = num1 + num2
    print(resultado)

soma = somar(1, 10)
print(soma)

def junta_nome(nome, sobrenome):
    nome_completo = nome + " " + sobrenome
    return nome_completo

nome = "Lucas"
sobrenome = "Soares"

print(junta_nome(nome, sobrenome)) '''

# Função - Calculadora com números gerados de forma aleatoria

from random import randint

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

while True:
    controle = int(input(
        "1 - Somar\n"
        "2 - Subtrair\n"
        "3 - Multiplicar\n"
        "4 - Dividir\n"
        "0 - Sair\n"
        "Digite a opção desejada: "))
    if controle != 0:
        numero1 = randint(1, 1000)
        numero2 = randint(1, 1000)

        print(f"O primeiro número é {numero1}!")
        print(f"O segundo número é {numero2}!")
        match controle:
            case 1:
                print(somar(numero1, numero2))
            case 2:
                print(subtrair(numero1, numero2))
            case 3:
                print(multi(numero1, numero2))
            case 4:
                print(dividir(numero1, numero2))
    else:
        break