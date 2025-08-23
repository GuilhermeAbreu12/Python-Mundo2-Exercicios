# Aula 13: Estrutura de repetição for
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
t = 0
for c in range(1, 6):
    peso = float(input('Digite o peso em KG da {}º pessoa '.format(c)))
    if peso > maior:
        maior = peso
    if c == 1:
        t = peso
        continue
    if c != 1 and peso < t:
        t = peso


print('O maior peso foi o de {}Kg, e o menor peso foi o de {}Kg'.format(maior, t))

