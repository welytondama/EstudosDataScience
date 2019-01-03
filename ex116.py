'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

from math import ceil

altura = float(input('Qual a altura da área a ser pintada? '))
largura = float(input('Qual a lagura da área a ser pintada? '))

tinta = (altura * largura) / 3

if tinta > 18:
    latas = ceil(tinta/18)
    print('serão utilizados {} litros de tinta ou seja {} latas de tinta para pintar a área especificada, e isso vai custar R${} reais'.format(tinta, latas, (latas*80)))

else:
    print('Você vai precisar de apenas uma lata de tinta que custa R$80,00 para pintar {} metros quadrados'.format(altura * largura))
