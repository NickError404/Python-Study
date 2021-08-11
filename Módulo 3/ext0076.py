# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

tabela = ('Atlético-MG',
'Palmeiras',
'Fortaleza',
'Red Bull Bragantino',
'Flamengo',
'Athletico PR',
'Ceará',
'Santos',
'Atlético-GO',
'Bahia',
'Internacional',
'Corinthians',
'Fluminense',
'Juventude',
'Sport',
'São Paulo',
'América-MG',
'Cuiabá-MT',
'Grêmio',
'Chapecoense')

while True:
    select = int(input(f'''
    [1] Os primeiros 5 times.
    [2] Os últimos 4 colocados
    [3] times em ordem alfabéticas
    [4] Em que posição está o time da Chapecoense.
    '''))

    if 4 >= select >= 1:
        break
if select == 1:
    for i in range(0, 4):
        print(tabela[i])
elif select == 2:
    for c in range(-4, -0):
        print(tabela[c])
elif select == 3:
    n = len(tabela)
    tabela_sorted = sorted(tabela)
    for c in range(0, n):
        print(tabela_sorted[n])
elif select == 4:
    chapecó = tabela.index('Chapecoense')+1
    print(f'Chapecoense está na {chapecó}° Posição. ')
