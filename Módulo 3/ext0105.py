# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor
# lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def factorial(num, show=False):
    from math import factorial
    if show == True:
        fact = 1
        for i in range(1, num+1):
            fact = fact * i
            if i < num:
                print(f'{fact} X ', end='')
            else:
                print(f'= {fact}')
    else:
        print(factorial(num))


print(factorial(5, show=True))
