# Calculadora de vendas de maçãs
n = int(input("Quantas maças você deseja: "))

if n > 11:
    total = n * 1.24
else:
    total = n * 1.37

print(f"O valor final da compra é {total}")