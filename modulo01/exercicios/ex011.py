largura = float(input('Largura da parede? '))
altura = float(input('Altura da parede: '))
d = largura * altura
print(f'Sua parede tem a dimensão de {largura}X{altura} e sua área é de {d}m².')
print(f'Para pintar essa parede, você precisará de {d / 2:.1f}L de tinta.')