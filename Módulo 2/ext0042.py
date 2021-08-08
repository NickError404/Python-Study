
# idade = int(input('\033[36mDigite a sua idade: '))


# if idade <= 17:
#     print(f'Você ainda é muito jovem para se alistar')
#     new_idade = (idade - 18)
#     alist = new_idade * -1
#     print('\033[33mA idade correta para o alistamento é daqui {} anos'.format(alist))
# elif idade > 18:
#     new_idade = (idade -18)
#     print('\033[31mVocê é muito velho para se alistar, a idade permitida é somente 18 anos isso foi a {} anos.'.format(new_idade))
# elif idade == 18:
#     print('\033[32mÉ hora de você se alistar, você já fez {}anos.'.format(idade))



from datetime import date

atual = date.today().year

nasc = int(input('Ano de nascimento: '))

idade = atual - nasc

print('\033[32mQuem nasceu em {} tem {} anos no ano de {}'.format(nasc, idade, atual))


if idade <=17:
    saldo = idade - 18
    print(f'\033[31mVocê é muito novo para o alistamento, você ainda tem {idade} anos, você só deverá se alistar daqui {saldo * -1} anos')
    print(f'Você deverá se alistar no ano de {atual+saldo}')
elif idade > 18:
    saldo = idade - 18
    print(f'\033[31mVocê é muito velho para se alistar você tem {idade} anos, você deveria ter se alistado a {saldo} anos')
    print(f'Você deveria ter se alistado no ano de {atual - saldo}')
elif idade == 18:
    print(f'\033[32mÉ momento de se alistar já!, você já tem {idade} anos') 