# Aula 12: Condições Aninhadas
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa. calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso;
# - Entre 18.5 e 25: peso ideal;
# - 25 até 30: sobrepeso;
# - 30 até 40: obesidade; 
# - Acima de 40: obesidade mórbida. 
peso = float(input('Quanto você pesa em kg '))
altura = float(input('Qual é a sua altura em metros? '))
imc = float(peso / altura)
print(imc)

if imc < 18.5:
    print('Você está abaixo do peso')
if imc in float(range(18.0, 25.0)):
    print('Parabéns você está com o peso ideal!')
elif imc in float(range(25.0, 30.0)):
    print('Infelizmente você está acima do peso')
elif imc in float(range(30.0, 40.0)):
    print('Sinto muito, mas você está com as características de obesidade')
elif imc > 40.0:
    print('Infelizmente você está com obesidade mórbida')