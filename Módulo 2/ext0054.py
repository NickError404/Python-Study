



primeiro_termo = int(input('Primeiro Termo: '))
Razão = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * Razão
for c in range(primeiro_termo, decimo + Razão, Razão):
    print(c)
