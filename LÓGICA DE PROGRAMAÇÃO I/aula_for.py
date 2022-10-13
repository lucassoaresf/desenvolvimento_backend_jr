''' # Exemplo de FOR - 1
for num in range(5):
   print(f"O valor de num é: {num}")

for num in range(3, 5):
   print(f"O valor de num é: {num}")

for num in range(10, 50, 5):
   print(f"O valor de num é: {num}") '''

''' # Exemplo de FOR - 2

from random import randint

minha_lista2 = []
for n in range(100):
   minha_lista2.append(randint(1, 500))
print("Exemplo 2")
print(minha_lista2) '''

''' # Exemplo de FOR - 3

from random import randint

lista_num = []

for n in range(10):
   lista_num.append(randint(1,30))

val_pares = 0
val_impares = 0

for i in lista_num:
   if (i % 2) == 0:
       val_pares += 1
   else:
       val_impares += 1

print(f"A minha lista é: \n {lista_num}")
print(f"A quantidade de valores pares: {val_pares}")
print(f"A quantidade de valores impares: {val_impares}") '''