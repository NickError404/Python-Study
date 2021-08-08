



nota_1 = float(input('\033[32mDigite a nota do primeiro semestre: '))

nota_2 = float(input('\033[32mDigite a nota do seu segundo semestre: '))

média_de_reprovação = 5.0

média_de_recuperação = 5.0, 6.9

média_de_aprovação = 7.0



True_Média = (nota_1 + nota_2) / 2

if True_Média < média_de_reprovação:
    print(f'\033[31mReprovado!')

elif True_Média >= 5 and True_Média < 7:
    print(f'\033[33mFicou de Recuperação!')


elif True_Média >= média_de_aprovação:
    print(f'\033[32mAprovado!')

else:
    print(f'\033[31mTem algo de errado com seu código!!!!!')