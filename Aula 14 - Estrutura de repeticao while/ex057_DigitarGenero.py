# Aula 14: Estrutura de repetição while
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto
cadastrado = 0
sexo = str(input('Digite o seu gênero: ')).strip().upper()[0]
while cadastrado == 0:
    if sexo == 'M' or sexo == 'F':
        cadastrado += 1
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Dado inválido. Por favor, informe seu sexo: ')).strip().upper()[0]
        if sexo == 'M' or sexo == 'S':
            cadastrado += 1
print('Cadastro efetuado com sucesso')
