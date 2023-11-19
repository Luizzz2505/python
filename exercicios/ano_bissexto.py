# Crie um programa que verifica se um ano é bissexto. Um ano é bissexto se for divisível por 4, exceto anos que são divisíveis por 100 mas não por 400.

ano = int(input('Informe o ano para saber se ele é bissexto ou não: '))

if ano % 4 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))