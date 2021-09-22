import json
def escrever(msg):
    with open('date.json', 'w', encoding='utf8') as f:
        json.dump(msg, f, ensure_ascii=False, indent=4, separators=(',', ':'))

def ler():
    with open('date.json', 'r', encoding='utf8') as f:
        return json.load(f)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n