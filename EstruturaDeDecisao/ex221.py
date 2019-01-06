'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque
e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de
1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não
deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
 quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

saque = int(input('Qual valor deseja sacar? '))
if saque > 600 or saque < 10:
    print('Não é possível realizar um saque maior que R$600,0 ou menor que R$10,0')

cem = saque // 100
print('{} nota(s) de Cem'.format(cem))
restante = saque % 100

while restante >= 1:
    if restante > 50:
        cinquenta = restante // 50
        print('{} nota(s) de Cinquenta'.format(cinquenta))
        restante = restante % 50
        #print(restante)

    elif restante > 10:
        dez = restante // 10
        print('{} nota(s) de Dez'.format(dez))
        restante = restante % 10
        #print(restante)

    elif restante > 5:
        cinco = restante // 5
        print('{} nota(s) de Cinco'.format(cinco))
        restante = restante % 5
        #print(restante)

    elif restante >= 1:
        um = restante // 1
        print('{} nota(s) de Um'.format(um))
        restante = restante % 1
        #print(restante)

print('Retire o dinheiro no local indicado.')


