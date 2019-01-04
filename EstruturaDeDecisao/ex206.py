#Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segunda número: '))
n3 = float(input('Insira o terceira número: '))

maior = n1

if n1 > n2 and n1 > n3:
    print('O maior valor é {}'.format(n1))
elif n2 > n3:
    print('O maior número é {}'.format(n2))
else:
    print('O maior valor é {}'.format(n3))
