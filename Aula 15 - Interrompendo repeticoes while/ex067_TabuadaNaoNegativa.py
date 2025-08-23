# Aula 15: Interrompendo repetições while
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n = 1
while n > 0:
    print('-'*100)
    n = int(input('Digite um valor para descobrir sua tabuada: '))
    print('_'*100)
    if n <= 0:
        break
    for c in range(1,11):
        print('{} X {} = {}'.format(n, c, n*c))
