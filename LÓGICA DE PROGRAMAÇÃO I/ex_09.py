# Conversão de Celsius em Fahrenheit, e de Fahrenheit em Celsius
cel = float(input('Digite o valor da temperatura em Celcius: '))
fah = cel * 1.8 + 32
print('{:.1f}°C é igual a {:.1f}°F!'.format(cel, fah))
fah2 = float(input('Digite o valor da temperatura em Fahrenheit: '))
cel2 = (fah2 - 32) / 1.8
print('{:.1f}°F é igual a {:.1f}°C!'.format(fah2, cel2))