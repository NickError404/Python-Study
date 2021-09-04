# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
# digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa
# se encerrará. Importante: use cores.

from time import sleep

c = ('\033[0;30;41m',
'\033[0;30;43m',
'\033[m')

def MiniSistema(msg):
    conti = False
    while conti == False:
        s = input(msg)
        print(c[0])
        print('Processando...')
        print(c[2])
        if s.lower() not in 'fim':
            print(c[1])
            print(f'\033[1;35m{help(s)}')
            print(c[2])
        else:
            conti = True
            print(f'\033[1;91mEncerrando...')
        s = ' '

MiniSistema('\033[1;91mPergunte-me algo:\033[m ')
