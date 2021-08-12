# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.




palavras = ('banana', 'casa', 'curso', 'guanabara', 'lucas', 'life',
'vida', 'octa', 'vinte', 'loop', 'entretenimento', 'aviao', 'home',
'escola', 'inferno', 'hell', 'local')



for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for palavras in p:
        if palavras.lower() in 'aeiou':
            print(palavras, end=' ')    