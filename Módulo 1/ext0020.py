import math

n = float(input('Digite um valor: '))

cosseno = math.cos(math.radians(n))
seno = math.sin(math.radians(n))
tangente = math.tan(math.radians(n))


print(f'O valor de cosseno é {cosseno}, o valor de seno é {seno}, e o valor de tangente é {tangente}')