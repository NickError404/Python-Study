# Exercício Python 083:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.



expressão = str(input('Enter your numeric expression: ')).strip().lower()

cont = len(expressão)
left_p = 0
right_p = 0
for s in expressão:
    if s in '(':
        left_p += 1
    if s in ')':
        right_p += 1

print(f'\033[33mExpressão feita: {expressão}')
if left_p == right_p:
    print('\033[32mSua expressão está correta!')
else:
    print('\033[31mSua expressão está incorreta!')
