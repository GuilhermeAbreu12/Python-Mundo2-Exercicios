# Aula 13: Estrutura de repetição for
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
divisivel = 0

for c in range(1, num + 1):

    if num % c == 0:
        print('\033[34m', end=' ')
        divisivel += 1
    else:
        print('\033[31m', end=' ')

    print(c, end='')
print('\033[m')
if divisivel != 2:
    print('O número {} foi dividido {} vezes e por isso ele NÃO É um número PRIMO!'.format(num, divisivel))
else:
    print('O número {} foi dividido {} vezes e por isso ele É um número PRIMO!'.format(num, divisivel))
