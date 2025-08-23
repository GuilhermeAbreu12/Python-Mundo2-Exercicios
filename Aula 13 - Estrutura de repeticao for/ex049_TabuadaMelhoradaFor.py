# Aula 13: Estrutura de repetição for
# Refaça o Desafio 009, mostrando a tabuada de um número que o usuario escolher, só que agora utilizando um laço for
num = int(input('Digite um número para saber a tabuada: '))

for c in range(0, 11):
    print('{} . {} = {}'.format(num, c, num*c))
