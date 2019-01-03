'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

altura = float(input('Digita a altura da pessoa '))
genero = str(input('Qual seu gênero h - homem ou m - mulher? '))
if genero == 'm':
    peso = (62.1 * altura) - 44.7
else:
    peso = (72.7 * altura) - 58


print('De acordo com a altura informada, o peso ideal é {} KG'.format(peso))