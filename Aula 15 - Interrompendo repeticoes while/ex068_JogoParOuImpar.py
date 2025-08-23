# Aula 15: Interrompendo repetições while
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import choice
print('=-'*50)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*50)

vitoria = 0

while True:
    valor = int(input('Digite um valor: '))
    alternativa = str(input('Par ou Ímpar? [P/I] ')).upper()
    bot = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    soma = int(valor + bot)
    if soma % 2 == 0:  # Par
        if alternativa == 'P':
            # Quando a soma for Par e o usuario tiver escolhido Par
            print('--'*50)
            print('Você jogou {} e o computador {}. Total de {} DEU {}'.format(valor, bot, soma, 'PAR' ))
            print('--'*50)
            print('Você VENCEU!')
            vitoria += 1
        elif alternativa == 'I':
            # Quando a soma for Par, mas o usuario tiver escolhido Ímpar
            print('--'*50)
            print(f'Você jogou {valor} e o computador {bot}. Total de {soma} DEU PAR')
            print('Você perdeu!')
            print('E conseguiu {} vitórias consecutivas'.format(vitoria))
            break
            
    else:  # impar
        if alternativa == 'P':
            # Quando a soma for ímpar, mas o usuario tiver escolhido Par
            print('--'*50)
            print(f'Você jogou {valor} e o computador {bot}. Total de {soma} DEU ÍMPAR')
            print('Você perdeu!')
            print(f'E conseguiu {vitoria} vitórias consecutivas')
            break
        if alternativa == 'I':
            # Quando a soma for Ímpar e o usuario tiver escolhido Ímpar
            print('--'*50)
            print(f'Você jogou {valor} e o computador {bot}. Total de {soma} DEU ÍMPAR')
            print('--'*50)
            print('VOCÊ GANHOU!')
            vitoria += 1
    print('Vamos jogar novamente...')
