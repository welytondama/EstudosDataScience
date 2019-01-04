#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('Insira o primeiro produto: '))
p2 = float(input('Insira o segunda produto: '))
p3 = float(input('Insira o terceira produto: '))

barato = p1

if p1 < p2 and p1 < p3:
    print('Você deve comprar o primeiro produto de  R${}'.format(p1))
elif p2 < p3:
    print('Você deve comprar o primeiro produto de  R${}'.format(p2))
else:
    print('Você deve comprar o primeiro produto de  R${}'.format(p3))