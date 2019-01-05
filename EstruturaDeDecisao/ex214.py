'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao
longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

if media <= 4:
  conceito =str('E')
elif media <= 6:
  conceito = str('D')
elif media <= 7.5:
  conceito = str('C')
elif media <= 9:
  conceito = str('B')
elif media <= 10:
  conceito = str('A')

if conceito in ('A','B','C'):
  print('APROVADO! com conceito {}'.format(conceito))
else:
  print('REPROVADO! com conceito {}'.format(conceito))