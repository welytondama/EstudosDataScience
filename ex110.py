#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temperatura = float(input('Qual a temperatura atual em ºCelcius? '))

farenheit = temperatura * 1.8 + 32

print('{}º Ceiucius equivales a {}ºFarenheit'.format(temperatura, farenheit))