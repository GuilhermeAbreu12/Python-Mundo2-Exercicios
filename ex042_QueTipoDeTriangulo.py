# Aula 12: Condições Aninhadas
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais;
# - ISÓSCELES: dois lados iguais;
# - ESCALENO: todos os lados diferentes.
from time import sleep
print('-=' * 20)
print('{}Analizador de Triângulos{}'.format('\033[34m', '\033[m'))
print('-=' * 20)

n = float(input('Digite o comprimento da primeira reta '))
n2 = float(input('Digite o comprimento da segunda reta '))
n3 = float(input('Digite o comprimento da terceira reta '))

a = n + n2 > n3
b = n2 + n3 > n
c = n + n3 > n2

if a == True and b == True and c == True:
    print('É possivel sim formar um triângulo')
    print('{}Analizando o triângulo...{}'.format('\033[34m', '\033[m'))
    sleep(1)

    if n == n2 and n == n3 and n2 == n3:
        print('O triângulo criado será Equilátero')
    elif n == n2 or n == n3 or n2 == n3:
        print('O triângulo criado será Isósceles')
    elif n != n2 and n != n3 and n2 != n3:
        print('O triângulo criado será Escaleno')
else:
    print('Não é possivel formar um triângulo')
