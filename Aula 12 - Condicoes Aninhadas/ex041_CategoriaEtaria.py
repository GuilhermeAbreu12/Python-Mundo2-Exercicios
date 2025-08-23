# Aula 12: Condições Aninhadas
# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM;
# - Até 14 anos: INFANTIL;
# - Até 19 anos: JUNIOR;
# - Até 20 anos: SÊNIOR;
# - Acima: MASTER.
import time
for c in range(0, 5):
    print('=-' * 50)
    nasc = int(input('{}Em que ano você nasceu?:{} '.format('\033[34m', '\033[m')))
    data = int(time.strftime('%Y'))
    calculo = data - nasc

    if calculo <= 9:
        print('{}Bom dia!! Você está na classe mirim.{}'.format('\033[34m', '\033[m'))
    elif calculo in range(10, 15):
        print('Bom dia! Você é da classe Infantil')
    elif calculo in range(15, 20):
        print('Bom dia! Você é da classe Junior')
    elif calculo == 20:
        print('Bom dia meu jovem! Você é da classe Sênior!')
    else:
        print('Bom dia! O senhor é da classe Master')
