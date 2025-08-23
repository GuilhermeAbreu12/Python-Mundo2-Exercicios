# Aula 13: Estrutura de repetição for
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

for c in range(0, 11):
    sleep(1)
    print(10 - c)
print('BOOOM! BOOM!!!')
