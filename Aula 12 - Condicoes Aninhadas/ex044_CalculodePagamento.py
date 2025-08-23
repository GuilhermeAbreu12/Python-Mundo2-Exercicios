# Aula 12: Condições Aninhadas
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto;
# - À vista no cartão: 5% de desconto;
# - Em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros.
valor = float(input('Qual é o preço do produto? R$'))
dinheiro = valor - ((valor / 100) * 10)
credito = valor - ((valor / 100) * 5)
credito2 = valor
credito3 = valor + ((valor / 100) * 5)
print('''Selecione uma função para definir a forma de pagamento
[ 1 ] PAGAMENTO À VISTA NO DINHEIRO
[ 2 ] A VISTA NO CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x ou mais NO CARTÃO''')
condição = input('Digite aqui: ')
if condição == '1':
    print('O pagamento à vista em dinheiro custará R${:.2f}'.format(dinheiro))
if condição == '2':
    print('O pagamento à vista no cartão custará R${:.2f}'.format(credito))
if condição == '3':
    print('O pagamento em 2 vezes no cartão custará R${:.2f}'.format(credito2))
if condição == '4':
    print('O pagamento em 3 vezes no cartão ou mais custará R${:.2f}'.format(credito3))
