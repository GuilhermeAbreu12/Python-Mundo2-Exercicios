# Aula 12: Condições Aninhadas
# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
import random
chute = input('''Escolha uma das opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Digite aqui: ''')

escolha = random.choice(['Pedra', 'Papel', 'Tesoura'])

