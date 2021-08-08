


# primeiro_termo = int(input('Primeiro Termo: '))

# if primeiro_termo == 0 or primeiro_termo <0:
#     print(primeiro_termo)
#     print('\033[31mPrograma encerrado!')
#     exit()

# razão = int(input('Razão: '))
# cont = 1
# termo = primeiro_termo
# PA = 0
# more = 10
# while more != 0:
#     PA = PA + more
#     while cont <= PA:
#         print(termo)
#         termo += razão
#         cont += 1
#     more = int(input('Quantos termos deseja mostrar a mais? '))
# print('\033[33mPrograma encerrado!')

primeiro_termo = int(input('Primeiro Termo: '))

if primeiro_termo == 0 or primeiro_termo < 0:
    print(primeiro_termo)
    print('\033[31mPrograma encerrado: ')
    exit()

razão = int(input('Digite Razão: '))
cont = 1
termo = primeiro_termo
more = 10
end = 10
while more != 0:
    end = end + more
    while cont <= end:
        print(termo)
        termo += razão
        cont += 1
    more = int(input('Deseja continuar? Digite mais valores então: '))
print(f'\033[33mO fim da prograssão foi feito, ao total foram feitos {end} progressões, terminando no valor de {termo}')


















