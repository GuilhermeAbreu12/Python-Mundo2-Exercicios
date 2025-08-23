# Aula 13: Estrutura de repetição for
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores, considere a maioridade como 21 anos.

from datetime import date
atual = date.today().year
maior = 0
menor = 0


for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa '.format(c)))
    calculo = atual - nasc
    if calculo < 21:
        menor += 1
    elif calculo >= 21:
        maior += 1

print('Das 7 pessoas {} atingiram a maioridade e {} ainda não atingiram a maioridade'.format(maior, menor))
