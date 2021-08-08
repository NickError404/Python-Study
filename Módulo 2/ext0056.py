
frase = str(input('DIgite aqui: '))

palavras = frase.split()

junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)   



