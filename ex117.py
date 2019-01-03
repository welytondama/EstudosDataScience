'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

from math import ceil

altura = float(input('Qual a altura da área a ser pintada? '))
largura = float(input('Qual a lagura da área a ser pintada? '))
area = float((altura * largura) * 1.1) #área acrescida de 10% de folga
litros = area / 6

lata = ceil(litros / 18)
lata_m = round(litros / 18)

print('Comprando apenas latas de 18 litros você vai utilizar {} lata(s) para pintar uma área de {:.0f} metros quadrados. E vai custar R${:.2f}'.format(ceil(litros/18), (area), (lata * 80)))
print('Se preferir pode compra apenas latas de 3.6 litros, neste caso seria {} lata(s) para pintar {:.0f} metros quadrados. Que vai custar R${:.2f}'.format(ceil(litros/3.6), (area), ((ceil(litros/3.6)) * 25)))


if ((lata_m * 18) * 6) < area:
    latinha = ceil((litros % 18) / 3.6)
    print(
        'Afim de evitar desperdício de tinta, você pode comprar {} lata(s) de tinta de 18 litros que vai custar R${:.2f} e {} galão de tinta de 3.6 litros que vai custar R${:.2f} \nQue será um valor total de R${:.2f}'.format(
            lata_m, (lata_m * 80), latinha, (latinha * 25), ((lata_m * 80) + (latinha * 25))))
else:
    print(
        'Afim de evitar desperdício de tinta, você pode comprar {} lata(s) de tinta de 18 litros que vão custar R${:.2f}'.format(lata, (lata * 80)))


