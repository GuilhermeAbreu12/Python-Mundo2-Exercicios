# Aula 14: Estrutura de repetição while
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
maior = 0
menor = 0
salvo = 0
parada = 0
pergunta = ''
c = -1
while parada != 1:
    n = int(input('Digite um número inteiro: '))
    pergunta = str(input('Você quer continuar? [S/N]')).upper()
    if pergunta != 'N':
        if c == -1:
            maior = n
            menor = n
            salvo = n
        if c != -1:
            salvo += n
            if n > maior:
                maior = n
            elif menor > n:
                menor = n
    c += 1
    if pergunta == 'N':
        parada = 1
        media = salvo / c
        print('A média entre os {} números digitados é de {}, o maior número digitado foi o numero {} já o menor número digitado foi o número {}'.format(c, media, maior, menor))
