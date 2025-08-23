# Aula 14: Estrutura de repetição while
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
c = 0

while c == 0:
    n = int(input('Digite um valor (precione 0 para sair): '))
    if n != 0:
        print('{}'.format(factorial(n)))
    if n == 0:
        c = 2
print('Processo finalizado com sucesso')
