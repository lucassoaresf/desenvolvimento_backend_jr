# Calculadora de saldo
valor_conta = 1000

dep = float(input("Adicione um valor: "))
valor_conta = dep + valor_conta

saque = float(input("Digite o valor do saque: "))

if saque > valor_conta:
    saldo = (valor_conta - saque) * - 1
    print(f"Saldo insuficiente, você precisa de: R$ {saldo:.2f}")
else:
    saldo = (valor_conta - saque)
    print(f"Restou em sua conta: R$ {saldo:.2f}")