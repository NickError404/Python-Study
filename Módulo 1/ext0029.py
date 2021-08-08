



nome = str(input('Digite seu nome: ')).strip()

nome_separado = nome.split()

num = len(nome_separado)

print(f'O seu primeiro nome é {nome_separado[0]}, e seu último nome é {nome_separado[num - 1]}')

