# Observando por idade se já pode votar e/ou tirar a CNH
ano = int(input("Digite o ano do seu nascimento: "))
idade = 2022 - ano

if idade >= 16 and idade == 17:
    print(f"Você já pode votar, já que sua idade é {idade} anos!!")
elif idade >= 18:
    print(f"Já pode dirigir e votar, já que sua idade é {idade} anos!!")
else:
    print(f"Você só tem {idade} anos. Sua hora vai chegar!!")