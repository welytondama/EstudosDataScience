'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
'''


peso = float(input('Insira o peso do peixe em Kg: '))

if peso > 50:
    excesso = float(peso - 50)
    multa = float(excesso * 4)
    print('Você excedeu {:.2f} Kg de peixe, e deve pagar uma multa de R${:.2f}'.format(excesso, multa))
else:
    print('A quantidade de peixe em Kg está dentro do permitido por lei, e não há multa a ser paga')

