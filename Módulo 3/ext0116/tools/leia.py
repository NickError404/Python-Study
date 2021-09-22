


# def leiaInt(msg):
#     válido = False
#     while not válido:
#         Num = str(input(msg)).strip()
#         if Num.isalpha() or Num == '':
#             print('Incorreto!')
#         elif Num.isnumeric():
#             válido = True
#             return int(Num)
#         else:
#             print('Incorreto!')

# def LeiaFloat(msg):
#     válido = False
#     while not válido:
#         Num = str(input(msg)).replace(',', '.').strip()
#         if Num.isalpha() or Num == '':
#             print('Incorreto!')
#         elif Num.isnumeric:
#             válido = True
#             return float(Num)
#         else:
#             print('Incorreto!')


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro, Por favor tente novamente!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário encerrou o programa.')
            return 0
        else:
            return num
