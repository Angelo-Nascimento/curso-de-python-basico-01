# Aula 07 - Operadores aritméticos
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão inteira
# % Resto da divisão
#------------------------
# Ordcm de precedência
# 1 - ()
# 2 - **
# 3 - *  /  //  %
# 4 - +  -

num01 = int(input('Enter the first number: '))
num02 = int(input('Enter the second number: '))
sum = num01 + num02
subtraction = num01 - num02
multiplication = num01 * num02
division = num01 / num02
integerDivision = num01 // num02
potentiation = num01 ** num02
print('The sum is: {} \nThe subtraction is: {}'.format(sum, subtraction)) # Use o ( \n ) para quebrar uma linha
print('The multiplication is: {:.2f}'.format(multiplication), end=' ') # User o ( end='' ) para colocar a linha de baixo a frente
print('The division is: {:.2f} \nThe integer division is: {} \nThe potentiation is: {}'.format(division, integerDivision, potentiation))

# Extra
print('-'*20) # Pode multiplicar valores em string
print('What is your name?')
name = input('Type here: ')
print('Nice to meet you, {:10}!'.format(name)) # Tamanho de caracteres exibidos, mas não limita a exibição
print('Nice to meet you, {:>10}!'.format(name)) # Alinhar a esquedar
print('Nice to meet you, {:<10}!'.format(name)) # Alinhar a direita
print('Nice to meet you, {:^10}!'.format(name)) # Centralziar
print('Nice to meet you, {:-^10}!'.format(name)) # Preencher os caracteres vazios ( - ou = )
