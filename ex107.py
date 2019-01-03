#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

altura = float(input('Qual a altura do quadrado? '))
largura = float(input('Qual a largura do quadrado? '))
if altura == largura:
        area = altura * largura
        print('O dobro da áea do quadrado é {:.2f}'.format(area*2))
else:
    print('As medidad especificadas não correspondem a um quadrado!')
