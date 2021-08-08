# faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'm' or 'f'
# caso esteja errado peça  digitaçao novamente ate ter um valor correto






sexo = str(input('\033[33mDigite seu sexo: ')).strip().lower()[0]
while sexo not in 'FfMm':
    sexo = str(input(f'\033[31mOps, Tende novamente: {sexo} não é uma respota válida!')).strip().lower()[0]
print('\033[32mSexo selecionado com sucesso!')