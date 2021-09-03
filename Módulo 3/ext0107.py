# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor
# numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    tot = False
    while tot == False:
        n = str(input(msg))
        if n.isnumeric():
          tot = True
          value = int(n)
        else:
            print('Erro')
    return value

print(leiaInt('Digite um valor: '))
