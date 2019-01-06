'''

Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
'''

n1 = float(input('Informe um número inteiro ou decimal à sua escolha: '))

if round(n1) == n1:
    print('Este é um número Inteiro')
else:
    print('Esse é um número decimal')