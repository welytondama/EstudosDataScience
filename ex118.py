'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

from math import ceil
tamanho = float(input('Qual o tamanho do arquivo para download expresso em MB? '))
velocidade = float(input('Qual a velocidade da internet para download expresso em kbytes por segundo? '))

tempo = ((tamanho * 1024) / velocidade) / 60

print('Para baixar {}MB com uma velocidade de {}Kbps vai demorar {} minutos'.format(tamanho, velocidade, ceil(tempo)))