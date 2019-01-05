'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input('Qual o salário atual do funcionário da empresa Tabajara? '))
reajustado = 0
if salario <= 280:
    reajustado = salario * 1.2
    print('Foi aplicado um reajuste de 20% ao salário')
    print('O salário sofreu acréscimo de R${:.2f}'.format(reajustado - salario))
elif salario <=700:
    reajustado = salario * 1.15
    print('Foi aplicado um reajuste de 15% ao salário')
    print('O salário sofreu acréscimo de R${:.2f}'.format(reajustado - salario))
elif salario <=1500:
    reajustado = salario * 1.1
    print('Foi aplicado um reajuste de 10% ao salário')
    print('O salário sofreu acréscimo de R${:.2f}'.format(reajustado - salario))
else:
    reajustado = salario * 1.05
    print('Foi aplicado um reajuste de 5% ao salário')
    print('O salário sofreu acréscimo de R${:.2f}'.format(reajustado - salario))

print('O salário que antes era de R${:.2f} passou a ser R${:.2f}'.format(salario, reajustado))
