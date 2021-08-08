
# frase = ('Testando algo na merda da minha vida.')

# print(frase.split())

# print('''Sinceramente eu não acreditava que isso é possível
# na boa cara salvou minha vida que inferno eu não sabia mesmo!
# kkkkkk puta que pariu isso é muito legal aaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaa
# irrul, python é liberdade vai se fuder.''')



nome = str(input('Digite seu nome completo: ').strip())

lista = nome.split()

print(len(nome) - nome.count(' '))
print(nome.upper())
print(nome.lower())



print(f'O primeiro nome contem {len(lista[0])} letras.')
print(f'Seu primeiro nome tem {nome.find(" ")}')

