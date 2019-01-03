#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite a altura da pessoa em metros: '))

peso = (72.7*altura) - 58

print('O peso ideal para uma pessoa dessa altura seria cerca de {:.2f} KG'.format(peso))