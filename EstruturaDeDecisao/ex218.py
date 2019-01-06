'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

dia = int(input('Digite o Dia: '))
mes = int(input('Digite o Mês: '))
ano = int(input('Digite o Ano: '))

if mes in (1, 3, 5, 7, 8, 10, 12) and dia <= 31:
    print('{}/{}/{} é uma data válida'.format(dia, mes, ano))
elif mes in (4, 6, 9, 11) and dia <= 30:
    print('{}/{}/{} é uma data válida'.format(dia, mes, ano))
elif (ano % 4) == 0 and dia <= 29 or (ano % 4) != 0 and dia <= 28:
    print('{}/{}/{} é uma data válida'.format(dia, mes, ano))
else:
    print('{}/{}/{} não é uma data válida'.format(dia, mes, ano))
