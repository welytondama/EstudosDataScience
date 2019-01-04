#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sequissu = str((input('Infor seu sexo, M - Masculino ou F - Feminino'))

if sequissu == 'M':
    print('Masculino')

elif sequissu == 'F':
    print('Feminino')
else:
    print('Sexo Inválido')
