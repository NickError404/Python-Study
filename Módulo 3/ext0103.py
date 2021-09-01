# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro
# da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função
# anterior.
from random import randint

numeros = list()
pares = list()
somarPar = 0
def sortear():
    for c in range(0, 5):
        numeros.append(randint(0, 100))
    print(numeros)
    return numeros

def somarPar(lsd):
    for i in lsd:
        if i % 2 == 0:
            pares.append(i)
    print(f'Os valores pares da lista são: {pares}')
    print(f'A soma de todos os valores pares da listas: {sum(pares)}')
    return (pares)

sortear()
somarPar(numeros)
