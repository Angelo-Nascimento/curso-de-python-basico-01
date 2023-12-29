# Desafio 017
"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o 
comprimento da hipotenusa.
"""
from math import sqrt, pow, hypot
num = float(input('Digite o comprimento do cateto oposto: '))
num2 = float(input('Digite o comprimento do cateto adjacente: '))

# Usando ** para elevar um número ao quadrado e sqrt para fazer a raiz quadrada
valor01 = num**2 + num2**2
print('A hipotenusa vai medir: {:.2f}'.format(sqrt(valor01)))
print('\n')

# Usando pow para elevar um número ao quadrado e sqrt para fazer a raiz quadrada
valor02 = pow(num, 2) + pow(num2, 2)
print('A hipotenusa vai medir: {:.2f}'.format(sqrt(valor02)))
print('\n')

# Usando hypot para calcular
valor03 = hypot(num, num2)
print('A hipotenusa vai medir: {:.2f}'.format(valor03))
