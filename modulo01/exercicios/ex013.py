salario = float(input('Qual é o salário do funcionário? R$'))
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${salario + (salario / 100 * 15):.2f}')
