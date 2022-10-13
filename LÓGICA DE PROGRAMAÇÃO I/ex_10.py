# Calculadora de IMC
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura ** 2

print(f"Seu imc é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso normal")
elif imc >= 18.5 and imc <= 24.9:
    print("Você está no peso ideal")
elif imc >= 25.0 and imc <= 29.9:
    print("Você está com excesso de peso")
elif imc >= 30.0 and imc <= 34.9:
    print("Você está com Obesidade Classe I")
elif imc >= 35.0 and imc <= 39.9:
    print("Você está com Obesidade Classe II")
else:
    print("Você está com obesidade Classe III")