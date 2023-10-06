dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilometros rodados? '))
PreçoDiario = dias * 60
PreçoKM = km * 0.15
tot = PreçoDiario + PreçoKM
print(f'O total a pagar é de R${tot:.2f}')
