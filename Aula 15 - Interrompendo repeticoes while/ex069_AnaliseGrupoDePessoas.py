# Aula 15: Interrompendo repetições while
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
""" 
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos.
"""
maior = 0
menor = 0
homens = 0
pessoas = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu gênero [M/F]: ')).upper()
    pessoas += 1
    continuar = input('Quer continuar? [S/N]').upper()
    if sexo != 'M' and sexo != 'F':
        print('Você digitou o gênero errado: ')
        break
    if sexo == 'M':
        homens += 1
    if idade > 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    if continuar == 'N':
        break

print(f'Das {pessoas} pessoas que se cadastraram aqui:')
print(f'{maior} tem mais de 18 anos')
print(f'{homens} são homens')
print(f'{menor} mulheres que tem menos de 20 anos de idade')