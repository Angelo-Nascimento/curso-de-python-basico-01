# Desafio 016
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import floor, trunc
num = float(input('Digite um número: '))

# Removendo as casas decimais
print('O número {} tem a parte inteira {:.0f}'.format(num,num))
print('\n')

# Removendo as casas decimais com o trunk
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
print('\n')

# Arredondando para baixo
print('O número {} tem a parte inteira {}'.format(num, floor(num)))
print('\n')

# Convertendo para inteiro
print('O número {} tem a parte inteira {}'.format(num, int(num)))
