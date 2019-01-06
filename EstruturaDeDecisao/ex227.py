'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

morangos = float(input('Quantos quilos de morango a cliente está levando? '))
macas = float(input('Quantos quilos de maçãns a cliente vai levando? '))
somado = morangos + macas
if morangos <= 5:
    pmo = morangos * 2.5
elif morangos > 5:
    pmo = morangos * 2.2

if macas <= 5:
    pma = macas * 1.8
elif macas > 5:
    pma = macas * 1.5
precototal = pmo + pma

if somado > 8 or precototal > 25:
    precototal = (precototal * 0.9)

print('O total das compras foi: \n{} Quilos de maçã \n{} quilos de morangos'.format(macas, morangos))

print('O preco total das maçãs é R${:.2f} \nO preço total dos morango é R${:.2f} \nPreço total das compras R${:.2f}'.format(pma, pmo, precototal))