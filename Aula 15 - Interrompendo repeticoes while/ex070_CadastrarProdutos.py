# Aula 15: Interrompendo repetições while
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
"""
A) Qual é o total gasto na compra;
B) Quantos produtos custam mais de R$1000;
C) Qual é o nome do produto mais barato.
"""
total = 0
caros = 0
barato = 0
nomebarato = ''
c = 0
while True:
    produto = input('Produto: ')
    preco = float(input('Preço: R$ '))
    c += 1
    total += preco
    if preco > 1000:
        caros += 1
    if c == 1:
        barato = preco
        nomebarato = produto
    elif c != 1 and preco < barato:
        barato = preco
        nomebarato = produto

    continuar = input('Quer continuar? [S/N]: ').upper()
    if continuar == 'N':
        break
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer continuar? [S/N]: ').upper()
print(f'O total gasto na compra é de {total:.2f}')
print(f'{caros} produtos custam mais de R$1000,00')
print(f'O produto mais barato é o {nomebarato}')