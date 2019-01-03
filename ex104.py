#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Qual foi a segunda nota? '))
n3 = float(input('Qual foi a terceira nota? '))
n4 = float(input('Qual foi a quarta nota? '))

media = (n1+n2+n3+n4)/4

print('A média das notas é {:.2f}'.format(media))