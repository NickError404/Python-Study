def typee(escc):
    print('='*count)
    print(escc)
    print('='*count)

esc = str(input('\033[35mDigite qualquer coisa: ')).strip()
count = len(esc)
typee(esc)
