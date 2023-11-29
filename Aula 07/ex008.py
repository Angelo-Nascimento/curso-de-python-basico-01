# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input("Digite um valor em metros: "))
print('{} metros em centimetros é: {} cm'.format(metros, (metros*100)))
print('{} metros em milimetros é: {} mm'.format(metros, (metros*1000)))
