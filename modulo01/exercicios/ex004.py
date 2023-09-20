palavra = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(palavra)}')
print(f'''Só tem espaços? {palavra.isspace()}
É um número? {palavra.isnumeric()}
É alfabético? {palavra.isalpha()}
É alfanúmerico? {palavra.isalnum()}
Está em maiúsculas? {palavra.isupper()}
Está em minúsculas? {palavra.islower()}
Está cpitalizada? {palavra.istitle()}''')
