# Utilizando If, Elif e Else
numero = float(input('Digite aqui um valor: '))

if numero > 0:
    print(f'O número {numero:.0f} é positivo!')
elif numero == 0:
    print(f'O número {numero:.0f} é neutro!')
else:
    print(f'O número {numero:.0f} é negativo!')