# Observando a maior e a menor altura entre 15 pessoas
altura_menor = 0
altura_maior = 0
altura = []


for x in range(0, 15):
   altura.append(float(input("Informe sua altura: ")))
   if x == 0:
       altura_maior = altura_menor = altura[x]
   else:
       if altura[x] > altura_maior:
           altura_maior = altura[x]
       if altura[x] < altura_menor:
           altura_menor = altura[x]

print(f"A maior altura é: {altura_maior:.2f}m.")
print(f"A menor altura é: {altura_menor:.2f}m.")