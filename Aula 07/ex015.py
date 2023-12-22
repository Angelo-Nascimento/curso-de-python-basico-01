# Desafio 015
# Escreva um programa que pergunte a quantidade de KM percorridos por um carro e a quantidade de 
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$: 60 por dia
# e R$: 0.15 por KM rodado.

print('Quantos dias você ficou com o carro?')
dias = float(input("Quantidade: "))
print('Quantos Km você pecorreu?')
km = float(input('Km: '))

valor = (dias * 60) + (km * 0.15)

print('O valor a ser pago por ter usado {:.2f} dias e percorrido: {:.2f} Km é: R$:{:.2f}'.format(dias, km, valor))
