#Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('Qual o primeiro número que deseja comparar? '))
n2 = float(input('Qual o segundo número que deseja comparar? '))

if n1 > n2:
    print('O maior número dentre os dois, foi {}'.format(n1))
else:
    print('O maior número dentre os dois, foi {}'.format(n2))