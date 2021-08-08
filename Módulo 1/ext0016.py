





área = int(input('\033[33mDigite a área que deve ser pintada em m²: '))

litros_de_tinta = área / 3

valor_latas_de_tinta = 80

latas_de_tinta = litros_de_tinta / 18

valor = valor_latas_de_tinta * latas_de_tinta



print(f'\033[32mVocê precisará no total {latas_de_tinta:.2f} latas de tinta para pitar todo o local \n o orçamento total é {valor:.2f}')