# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

print('Qual o salário do funcionário?')
salario = float(input('R$: '))
novo = salario + (salario * 0.15)
print('Um funcionário que ganhava R$: {:.2f}, com 15% de aumento, passa a receber: R$: {:.2f}'.format(salario, novo))
