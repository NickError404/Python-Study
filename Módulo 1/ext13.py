
sexualidade = input('\033[33m Digite seu sexo:\033[m \033[34mM \033[mou \033[35mH \033[m?                                      SEM CAPSLOCK!!!')
h = float(input('Digite sua altura: '))



homens = 72.7 * h - 58

mulheres = 62.1 * h -44.7


if sexualidade == 'm':
    print(f'\033[4;32;47mVocê disse que você é mulher então Seu pedo ideal é {mulheres:.2f}')

elif sexualidade == 'h':
    print(f'\033[4;32mVocê disse que é Homem então Seu pedo ideial é {homens:.2f}')

else:
    print('\033[31mVocê selecionou uma opção inexistente !!')