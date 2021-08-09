total = mil = menor_preço = cont = 0
vx = True
while vx == True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: '))
    if cont == 0:
        menor_preço = preço
        produto_menor_preço = produto
    elif cont >= 1:
        if preço < menor_preço:
            menor_preço = preço
            produto_menor_preço = produto
    conti = ' '
    while conti not in 'yn':
        conti = str(input('Deseja continuar?: y/n')).strip().lower()[0]
        cont += 1
    if conti == 'y':
        vx = True
    elif conti == 'n':
        vx = False
    total += preço
    if preço > 1000:
        mil += 1
print(f'''
O total gasto é de {total}
{mil} Produtos custam mais de 1000 R$
O produto mais barato é {produto_menor_preço}, custando {menor_preço}
''')

