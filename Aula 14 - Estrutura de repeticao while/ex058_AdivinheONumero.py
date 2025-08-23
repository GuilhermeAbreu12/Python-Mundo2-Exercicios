# Aula 14: Estrutura de repetição while
# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import choice

ia = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print('-=' * 30)
print('\033[94mEstou pensando em um número, tente adivinhar qual é      \033[m ==')
print('-=' * 30)

chute = int(input('\033[92mDigite aqui de 0 : 10: \033[m'))
contador = 1
while chute != ia:
    contador += 1
    if chute != ia and ia > chute:
        chute = int(input('Tente mais alto! '))
    if chute != ia and ia < chute:
        chute = int(input('Tente mais baixo '))

if chute == ia:
    print('Você ACERTOU!!! Mas precisou de {} tentativas para conseguir acertar! Ganhou {} pontos'.format(contador, 10 - contador))
