# Aula 12: Condições Aninhadas
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor = int(input('Qual é o valor da casa que você quer comprar? R$'))
sal = int(input('Qual é o seu salário atual? R$'))
anos = int(input('Em quantos anos você quer comprar essa casa? '))

prestação = valor / (anos * 12)
# valor anual
# valor mensal
mínimo = (sal / 100) * 30
# 30% do salário

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))

if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')

else:
    print('Empréstimo NEGADO!')