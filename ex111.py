'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = float(input('Digite um número real: '))

print('O dobro do primeiro número com metade do segundo é: {} \nA soma do triplo do primeiro com o terceiro é {} \nO terceiro elevado ao cubo {:.2f}'.format(((n1*2)+(n2/2)), ((n1*3)+n3), (n3**3)))