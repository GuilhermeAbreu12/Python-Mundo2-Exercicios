# Aula 13: Estrutura de repetição for
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
pares = 0
soma = 0

for c in range(1, 7):
    n = int(input('Digite o {}º número'.format(c)))
    if n % 2 == 0:
        pares += n
print('A soma dos números pares digitados é {}'.format(pares))
