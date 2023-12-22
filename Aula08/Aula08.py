# Aula 08
# import DOCE - nesse exemplo importa todos os doces
# from DOCE import pudim - nesse exemplo importa somente o pudim
# SITE DO PYTHON: https://docs.python.org/3.12/library/index.html

# Exemplo importando toda a biblioteca
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a: {:.2f}'.format(num, raiz))

# Exemplo importanto funções especificas de uma biblioteca
from math import sqrt, floor # sqrt é raiz quadrada e floor arredonda pra baixo
num1 = int(input('Digite um número: '))
raiz1 = sqrt(num)
print('A raiz de {} é igual a: {:.2f}'.format(num1, floor(raiz1)))

# Exemplo para gerar números aleatórios
from random import randint
num2 = randint(1, 10) # Gerar um número aleatório entre 1 e 10
print(num2)
