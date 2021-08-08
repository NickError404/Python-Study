import random



n2 = input('Digite um nome: ')
n1 = input('Digite um nome: ') 
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')

nomes = [n1, n2, n3, n4]


random.shuffle(nomes)


print(nomes)    