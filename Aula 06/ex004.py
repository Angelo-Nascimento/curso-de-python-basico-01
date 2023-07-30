# Exercício 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
value = input('Enter something: ')
print('The primitive type of this value is: ', type(value))
print('There is only space? ', value.isspace())
print('Is it a number? ', value.isnumeric())
print('Is it alphabetical? ', value.isalpha())
print('Is it alphanumeric? ', value.isalnum())
print('Is it in upper case? ', value.isupper())
print('Is it in lower case? ', value.islower())
print('Is it capitalized? ', value.istitle())
