p = float(input('Qual é o preço do produto? '))
print(f'O produto que custava R${p:.2f}, na promoção com desconto de 5% vai custar R${p - (p / 100 * 5):.2f}')
