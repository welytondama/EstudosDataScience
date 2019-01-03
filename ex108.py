#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valhora = float(input('Quanto você ganha por hora? '))
horas = float(input('Quantas horas você trabalhou no último mês? '))

salario = valhora * horas

print('Você vai receber um salário de R${:.2f}'.format(valhora))
print('Por dia você recebe R${}, considerando uma jornada de 8 horas diárias'.format(valhora*8))