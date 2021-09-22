from ferramentas.dados import *
from time import sleep
nomes = ler()
list(nomes)
def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(f'\033[1;32m{linha()}')
    print(txt.center(42))
    print(linha())

def menu(lista= ['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair']):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mSua Opção: \033[m')
    select(opc)

def select(num):
    if num == 1:
        lista_nomes = ler()
        list(lista_nomes)
        sleep(1.5)
        for c, item in enumerate(lista_nomes):
            print(f'\033[1;36m{c+1}\033[m - \033[1;32m{item}')
        sleep(1.5)
        menu()
    elif num == 2:
        while True:
            nome = (str(input('\033[1;35mDigite o nome para ser adicionado: ')))
            sleep(1)
            verificação = str(input(f'\033[1;33mDeseja realmente adicionar o nome: {nome} a lista? [Y/N] '))
            sleep(0.5)
            print('\033[1;32mOperação Concluída')
            if verificação in 'Yy':
                nomes.append(nome)
                escrever(nomes)
                sleep(1)
                return menu()
            elif verificação in 'Nn':
                sleep(1)
                return menu()
            else:
                print('\033[1;31mOpção Inválida!')
                sleep(2)
