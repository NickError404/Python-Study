#interactive help
#help()
#(commands.__doc__)

#parametros opcionais
# if não ouver nenhum valor para receber na {i} inicial
#                                           {f} final
#                                           {p} pulos
# ele seta o valor padrão como for informado
#             123  123  123
#              |    |    |
# def contador(i=0, f=0, p=0):
    # """
    #       Dockstring
    # param i = valor inicial
    # param f = valor final
    # param p = aos valores evitados sequencialmente
    # """
    # c = i
    # while c <= f:
    #     print(f'{c}', end='..')
    #     c += p

# contador(10, 154, 2)
#         or
# contador(i=12, f=55, p=2)
#         or
# contador(i=44, p=54)


# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se
# uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


# Os alfabetizados maiores de 18 e menores de 70 anos são, por lei, obrigados a votar.
# O voto não é obrigatório para os analfabetos, os maiores de 70 anos,
# nem para os maiores de 16 e menores de 18 anos. Quando o eleitor completa 18 anos,
# o voto passa a ser obrigatório.


cadastro = dict()
cadastro['nome'] = str(input('Your name: ')).strip()
anos = int(input('Year of Birth: '))



def voto_idade(id):
    from datetime import date   
    atual = date.today().year
    cadastro['idade'] = ((anos - atual) *-1)
    if id < 16:
        cadastro["status de voto"] = 'NEGADO'
    elif 18 <= id <= 70:
        cadastro['status de voto'] = 'OBRIGATÓRIO'
    elif id > 70 or 16 <= id < 18:
        cadastro['status de voto'] = 'OPCIONAL'
    return (cadastro['status de voto'], cadastro['idade'])

voto_idade(anos)

for k, v in cadastro.items():
        print(f'O valor de {k} é {v}')
