


int1 = int(input('\033[32mDigite um número inteiro: '))

int2 = int(input('\033[32mDigite um número inteiro: '))

numreal = int(input('\033[32mDigite um número real: '))

ResultA1 = int2 / 2
resultA2 = int1 * 2

SomaA = ResultA1 + resultA2

SomaB = int1 * 3 + numreal

SomaC = numreal ** 3



print(f'\033[36mo produto do dobro do primeiro com metade do segundo. {SomaA}')

print(f'\033[36ma soma do triplo do primeiro com o terceiro. {SomaB}')

print(f'\033[36mo terceiro elevado ao cubo. {SomaC}')