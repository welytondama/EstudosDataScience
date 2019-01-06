'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

n1 = float(input('Qual o primeiro número? '))
n2 = float(input('E qual será o segundo número? '))
operacao = str.lower(input('Qual operação deseja realizar? '))

if operacao in ('menos', 'subtração', '-', 'subtrair'):
    resultado = n1 - n2
    print(resultado)
elif operacao in ('adição', 'somar', 'soma', '+', 'mais'):
    resultado = n1 + n2
    print(resultado)
elif operacao in ('dividir', 'divisão', '/',):
    resultado = n1 / n2
    print(resultado)
elif operacao in ('multiplicar', 'multiplicação', '*'):
    resultado = n1 * n2
    print(resultado)
else:
    resultado = ''
    print('Esta ainda não é uma operação suportada')

if resultado == '':
    print()

elif resultado % 2 == 0:
    print('O resultado é par')
else:
    print('O resultado é impar')

if resultado == '':
    print()
elif resultado == round(resultado):
    print('O resultado é um número inteiro')
else:
    print('O resultado é um número decimal')

if resultado == '':
    print()
elif resultado < 0:
    print('O resultado é um número negativo')
else:
    print('O resultado é um número positivo')