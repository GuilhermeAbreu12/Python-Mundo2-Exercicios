# Aula 14: Estrutura de repetição while
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# 0 - 1 - 1 - 2 - 3 - 5 - 8 

elementos = int(input('Quantos termos da sequência de Fibonacci quer mostrar? '))
c = 2

n1 = 0
n2 = 1
print('{} '.format(n1), end='')

while c <= elementos:
    print('➡  {} '.format(n2), end='')
    soma = n1 + n2
    n1 = n2
    n2 = soma
    c += 1

# n1 sempre recebe o valor de n2
# n2 sempre recebe o valor da soma