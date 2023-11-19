# Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.

numero = int(input('Insira um valor para saber se ele é par ou ímpar: '))

if numero % 2 == 0:
    print('{} é par'.format(numero))
else:
    print('{} é ímpar'.format(numero))