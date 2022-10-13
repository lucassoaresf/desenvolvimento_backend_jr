# Tabuada de 1 a 10, e ao fim você pode escolher um número e ver sua tabuada
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

num = int(input("Digite um número: "))
for h in range(1, 11):
    print(f"{num} x {h} = {num * h}")