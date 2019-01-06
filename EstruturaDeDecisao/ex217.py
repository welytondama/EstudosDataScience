'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se
este ano é ou não bissexto.
'''

ano = int(input('Insira um ano para ser verificado se ele é bissexto: '))

if (ano % 4) == 0:
    print('{} é um ano Bissexto!'.format(ano))
else:
    print('{} Não é um ano bissexto!'.format(ano))
