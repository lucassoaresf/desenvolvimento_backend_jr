#Calculadora Delta
import math
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = math.pow(b, 2) - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"Considerando que Delta é {delta} valor de X1 é {x1:.2f} e o valor de X2 é {x2:.2f}.")
#else:
 #   print("Reduza os valores.")