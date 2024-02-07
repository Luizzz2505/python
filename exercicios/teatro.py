# Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deve calcular e mostrar:
# a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.
# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.

custo = float(input('Informe de quanto foi o custo para organizar a apresentação no teatro: '))
ingresso = float(input('Informe o valor do ingresso: '))

alcancar = custo / ingresso 
lucro = alcancar * 1.23

print(f'Você deve vender {alcancar:.2f} ingressos para arrecadar o mesmo valor gasto para fazer a apresentação')
print(f'Você deve vender {lucro:.2f} ingressos para ter um lucro de 23%')