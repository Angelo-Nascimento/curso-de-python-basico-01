# Desafio 07
# Desenvola um programa que leia as duas notas de um aluno. Calcule e mostre a sua média

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1+nota2)/2
print('A média entre {:.2f} e {:.2f} é igual a {:.2f}'.format(nota1, nota2, media))
