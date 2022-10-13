# Visualizando por idade e tipo de ingresso a entrada em festas
idade = int(input("Digite a sua idade: "))
ingresso = input("Ingresso VIP ou PISTA: ")

if idade >= 18 and ingresso.upper().strip() == "VIP":
    print("Liberado pra vibe, siga para o próximo piso!!!")
elif idade >= 18 and ingresso.upper().strip() == "PISTA":
    print("Liberado pra vibe, siga para parte inferior!!!")
else:
    print("Passa logo pra casa!!!")