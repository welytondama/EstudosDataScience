#Faça um Programa que peça dois números e imprima a soma.

n1 = float(input('Informe o primeiro número que será utilizado na soma: '))

n2 = float(input('Informe o segundo número que será utilizado na soma: '))

resultado = n1 + n2

print('  {} \n+ {}\n_______\n{:.2f}'.format(n1, n2, resultado))
