# Aula 14: Estrutura de repetição while
""" Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. """

from time import sleep
c = 0
maior = 0
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
while c != 5:
    sleep(0.5)
    print('O que gostaria de fazer?')
    print("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sai do programa """)
    escolha = int(input(''))

    if escolha == 1:
        print('O resultado da soma de {} e {} é {}'.format(n1, n2, n1+n2))
        sleep(1)
    elif escolha == 2:
        print('O resultado da multiplicação de {} e {} é {}'.format(n1, n2, n1*n2))

    elif escolha == 3:
        if n1 == n2:
            print('Os dois números são iguais')
        elif n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        if n1 != n2:
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif escolha == 4:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    if escolha == 5:
        c = 5
print('Finalizado com sucesso')
