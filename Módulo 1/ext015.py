



salario = float(input('\033[33mDigite seu salário: '))

sindicato = salario * 5 / 100

inss = salario * 8 / 100

imposto_de_renda = salario * 11 / 100

print('=' * 10)
print(f'\033[32mSalário Bruto : R${salario} \n -IR(-11%) \n R$ {salario - imposto_de_renda}, \n -INSS(-8%) \n R$ {salario - imposto_de_renda - inss}, \n -Sindicato(-5%) \n R$ {salario - inss - imposto_de_renda - sindicato}, \n Salário Líquido \n R$ {salario - inss - imposto_de_renda - sindicato}')
print('=' * 10)
