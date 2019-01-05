'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não
deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre
o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
from math import sqrt

a = float(input('Qual o valor de da variável "a" na equação? '))

if a == 0:
    print('A equação não é do segundo grau')
else:
    b = float(input('Informe o valor da variável "b" na equação: '))
    c = float(input('Informe o valor da variável "c" na equação: '))

    resultado = (b) ** 2 - 4 * a * c

    if resultado > 0:
        x1 = (-(b) + (sqrt(resultado))) / (2 * a)
        x2 = (-(b) + (sqrt(resultado))) / (2 * a)

        r1 = x1 ** 2 -5 * x1 + 6
        r2 = x2 ** 2 -5 * x2 + 6

        if r1 < 0:
            print('A equação não possui raizes reais.')
        elif r1 == 0:
            print('A equação possui apenas uma raiz real que é {}'.format(r1))
        else:
            print('A quação possui duas raiz reais, são elas {:.2f} e {:.2f}'.format(r1, r2))
