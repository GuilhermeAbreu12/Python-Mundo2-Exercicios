# Aula 12: Condições Aninhadas
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele AINDA VAI SE ALISTAR ao serviço militar;
# - Se é a HORA DE SE ALISTAR;
# - Se já PASSOU DO TEMPO do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import time

nascimento = int(input('Em que ano você nasceu?'))

ano = int(time.strftime('%Y'))

futuro = ano - nascimento
if futuro < 18:
    print('Você irá se alistar daqui a {} anos'.format(nascimento + 18 - ano))
elif futuro == 18:
    print('Você deve se alistar ao exército {}IMEDIATAMENTE!!!{}'.format('\033[31m', '\033[m'))
else:
    print('Você se alistou a {} anos atrás'.format(nascimento + 18 - ano))
