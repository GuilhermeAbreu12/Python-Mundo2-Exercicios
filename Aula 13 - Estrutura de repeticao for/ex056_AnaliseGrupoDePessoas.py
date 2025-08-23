# Aula 13: Estrutura de repetição for
""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos de idade """

menor = 0
mascnome = ''
salvo = 0
soma = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}º pessoa '.format(c)))
    idade = int(input('Digite a idade da {}º pessoa '.format(c)))
    sexo = str(input('Digite o sexo da {}º pessoa '.format(c)))
    soma += idade
    if sexo == 'Masculino' and idade > salvo:
        salvo = idade
        mascnome = nome
    if sexo == 'Feminino' and idade < 20:
        menor += 1

media = soma / 4
print('A média da idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(salvo, mascnome))
print('No grupo há {} mulheres que têm menos de 20 anos'.format(menor))
