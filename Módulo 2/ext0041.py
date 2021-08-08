# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais

num1 = int(input('\033[35mDigite o primeiro valor: '))
num2 = int(input('\033[35mDigite o segundo valor: '))

if num1 > num2:
    print(f'\033[36mO primeiro valor{num1} é maior que o segundo {num2}')
elif num2 > num1:
    print(f'\033[36mO segundo valor {num2} é maior que o primeiro valor {num1}')
elif num1 == num2:
    print(f'\033[36mO valor de {num1} é igual a {num2}')