# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então  o empréstimo será negado

from time import sleep

casa = float(input('Informe o valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ ')) 
anos = int(input('Quantos anos de finaciamento?: '))

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))

print('PROCESSANDO...')
sleep(3)
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
