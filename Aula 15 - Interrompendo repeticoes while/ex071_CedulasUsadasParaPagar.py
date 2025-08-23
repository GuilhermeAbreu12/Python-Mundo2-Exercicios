# Aula 15: Interrompendo repetições while
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
valor = int(input('Que valor você quer sacar? R$ '))
c50 = int(0)
c20 = 0
c10 = 0
c1 = 0

while valor >= 50:
    valor = valor - 50
    c50 += 1
    
while valor >= 20:
    valor = valor - 20
    c20 += 1

while valor >= 10:
    valor = valor - 10
    c10 += 1

while valor >= 1:
    valor = valor - 1
    c1 += 1

print('Você receberá: ')
if c50 >= 1:
    print(f'{c50} Cédulas de R$50,00')
if c20 >= 1:
    print(f'{c20} Cédulas de R$20,00')
if c10 >= 1:
    print(f'{c10} Cédulas de R$10,00')
if c1 >= 1:
    print(f'{c1} Moedas de R$1,00')