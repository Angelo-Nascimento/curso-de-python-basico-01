# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a 
# quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m²

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura: '))

area = altura * largura
litros = area/2

print('Sua parede tem a dimensão de {:2}x{:2} e sua área é de: {:.2f}m²'.format(altura, largura, area))
print('Para pintar essa parede, você precisará de {:.2f} Litros de tinta.'.format(litros))
