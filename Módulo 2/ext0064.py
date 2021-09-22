# Refaça o DESAFIO 51, lendo o primeiro termo e a razao
# de uma PA, mostrando os 10
# primeiros termos da progressao usando a 
# estrutura while.


# primeiro_termo = int(input('Primeiro Termo: '))
# Razão = int(input('Razão: '))
# decimo = primeiro_termo + (10 - 1) * Razão
# for c in range(primeiro_termo, decimo + Razão, Razão):
#     print(c)



primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
termo = primeiro_termo

while cont != 11:
    print(termo)
    cont += 1
    termo += razão
print('Fim')
