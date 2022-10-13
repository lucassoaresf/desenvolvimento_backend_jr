# Calculando peso ideal por sexo
h = float(input("Digite sua altura: "))
sex = input("Seu sexo é Masculino ou Feminino: ")

if sex == "Masculino":
    print(f'O seu Peso ideal é: {((72.7 * h) - 58):.2f}')
elif sex == "Feminino":
    print(f'O seu Peso ideal é: {((62.1 * h) - 44.7):.2f}')