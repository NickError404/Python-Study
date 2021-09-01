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
def contador(i=0, f=0, p=0):
    """
          Dockstring
    param i = valor inicial
    param f = valor final
    param p = aos valores evitados sequencialmente
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p

# contador(10, 154, 2)
#         or
# contador(i=12, f=55, p=2)
#         or
# contador(i=44, p=54)
