


nome = str(input('Digite seu nome: ')).lower().strip()


print(nome.count('a'))

print('A primeira vez em que o valor de a foi entrado {}'.format(nome.find('a')+1))
print('A última vez em que o valor de a foi encontrado {}'.format(nome.rfind('a')+1))
