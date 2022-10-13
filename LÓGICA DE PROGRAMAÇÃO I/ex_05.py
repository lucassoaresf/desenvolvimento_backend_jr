# Calculando quantidades de latas para pintar um cilindro e o valor final
raio = float(input("Digite o Raio: "))
h = float(input("Digite a Altura: "))
PI = 3.14

areaCilindro = (PI * (raio ** 2)) + (2 * PI * raio * h)
qtdLitros = areaCilindro / 3
qtdLatas = qtdLitros / 5

valorFinal = qtdLatas * 50.0

print("Para pintar o cilindro precisamos de: ")
print(f"{qtdLatas:.2f} latas de tinta.")
print(f"O custo final foi de {valorFinal:.2f}")