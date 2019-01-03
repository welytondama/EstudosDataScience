'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

valhora = float(input('Quanto você ganha por hora? '))
horas = float(input('Quantas horas você trabalhou no último mês? '))

salario = valhora * horas

print('Salário bruto R${:.2f}'.format(salario))
print('Descoto de Imposto de Renda R${:.2f}'.format(salario*0.11))
print('Descoto do INSS R${:.2f}'.format(salario*0.08))
print('Descoto sindical R${:.2f}'.format(salario*0.05))
print('Salário líquido R${:.2f}'.format(salario*0.76))