# Aula 14: Estrutura de repetição while
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
parada = 0
c = 0
soma = 0
while parada != 999:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        parada = 999
    if n != 999:
        c += 1
        soma += n
print('Ao todo foram digitados {} numeros'.format(c))
print('E a soma entre eles é de {} '.format(soma))
