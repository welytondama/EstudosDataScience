'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
ele será classificado como "Inocente".
'''

p1 = str.lower(input('Telefonou para a vítima? S/N '))
p2 = str.lower(input('Esteve no local do crime? S/N '))
p3 = str.lower(input('Mora perto da vítima? S/N '))
p4 = str.lower(input('Devia para a vítima? S/N '))
p5 = str.lower(input('Já trabalhou com a vítima? S/N '))
suspeita = 0
if p1 == 's':
    suspeita += 1
else:
    suspeita += 0
if p2 == 's':
    suspeita += 1
else:
    suspeita += 0
if p3 == 's':
    suspeita += 1
else:
    suspeita += 0
if p4 == 's':
    suspeita += 1
else:
    suspeita += 0
if p5 == 's':
    suspeita += 1
else:
    suspeita += 0

if suspeita == 2:
    print('Essa pessoa é suspeita')
elif suspeita in (3, 4):
    print('Este deve ser o cúmplice ')
elif suspeita == 5:
    print('Assassino, com certeza!')
else:
    print('Inocente')
