'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
 o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o
 valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do
 litro do álcool é R$ 1,90.
'''

combustivel = str.lower(input('Qual tipo de combustível deseja abastecer? A-álcool, G-gasolina '))
litros = float(input('E quantos litros deseja abastecer no carango? '))

if combustivel == 'g':
    if litros <= 20:
        preco = (litros * 2.5) - (litros * 0.04)
    elif litros > 20:
        preco = (litros * 2.5) - (litros * 0.06)
    print('O valor a ser pago, já com desconto é R${:.2f}'.format(preco))
else:
    if litros <= 20:
        preco = (litros * 1.9) - (litros * 0.03)
    elif litros > 20:
        preco = (litros * 1.9) - (litros * 0.04)
    print('O valor a ser pago, já com desconto é R${:.2f}'.format(preco))