#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str.lower(input('Digite uma letra para descobrir se é vogal ou consoante: '))

if letra in ('a', 'e', 'i', 'o', 'u'):
    print('Esta é um vogal!')
else:
    print('Esta letra é uma consoante!')
