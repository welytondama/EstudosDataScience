#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

temperatura = float(input('Qual a temperatura atual em graus Farenheit? '))

c = (5 * (temperatura-32) / 9)

print('{} Farenheit equivalem a {:.2f}ºC'.format(temperatura, c))
