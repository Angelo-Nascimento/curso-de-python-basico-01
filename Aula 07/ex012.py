# Desafio 012
# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Qual o preço do produto?')
valor = float(input('R$: '))
final = valor - (valor*0.05)
print('O produto que custava R$:{:.2f}, na promoção com desconto de 5% vai custar: R$: {:.2f}'.format(valor, final))
