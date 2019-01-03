#Faça um Programa que converta metros para centímetros.

metros = float(input('Digite a quantidade de metros que deseja converter para centímetros: '))

centimetros = metros * 100

print('{:.2f} metros equivalem a {:.2f} centímetros.'.format(metros, centimetros))