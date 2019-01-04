#Faça um Programa que leia três números e mostre-os em ordem decrescente.


n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o segunda número: '))
n3 = float(input('Insira o terceira número: '))

lista = [n1, n2, n3]
lista.sort(reverse=True)

print(lista)
