# WHILE
x = 1
while x <= 1000:
    print(f"O número da rifa é {x}!!!")
    x += 1
print(f"A última rifa é {x}!!!")

''' # Brincadeira usando WHILE
nome = ""
while nome != "seu nome".upper():
    nome = input("Digite 'seu nome':").upper()
print("Obrigado por participar!") '''

 # Loop com WHILE

from random import randint

controle = 10

minha_lista = []

while controle >= 1:
   minha_lista.append(randint(1, 20))
   print(f"A minha variável de controle: {controle}")
   print(f"A minha lista: {minha_lista}")
   controle = controle - 1
print(minha_lista)