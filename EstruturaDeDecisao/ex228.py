'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
 porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara
 o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o
 tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações
 da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a
 pagar.
'''

print('Nosso cardápio oferece as seguintes carnes:')
print('File Duplo \nAlcatra \nPicanha')
carne = str.title(input('Qual a carne deseja levar? '))
peso = float(input('Quantos quilos de {} deseja? '.format(carne)))
pagamento = str.lower(input('Deseja pagar com cartão tabajara credi? s/n '))
if peso <= 5:
    if carne == 'File Duplo':
        preco = peso * 4.9
    if carne == 'Alcatra':
        preco = peso * 5.9
    if carne == 'Picanha':
        preco = peso * 6.9
if peso > 5:
    if carne == 'File Duplo':
        preco = peso * 5.8
    if carne == 'Alcatra':
        preco = peso * 6.8
    if carne == 'Picanha':
        preco = peso * 7.8

if pagamento == 's':
    print('O preço a pagar seria R${:.2f}, mas com cartão Tabajara credi você pagará apenas R${:.2f} na sua carne com corte de {}'
          .format(preco, (preco - ((preco*5)/100)), carne))
else:
    print('O preço a pagar é R${:.2f}, na sua {}'.format(preco, carne))
