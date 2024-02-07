# Escreva um programa que receba três números quaisquer e apresente:
# a) a soma dos quadrados dos três números;
# b) o quadrado da soma dos três números.

a = float(input('Insira um número: '))
b  = float(input('Insira o segundo valor: '))
c = float(input('Insira o terceiro valor: '))

soma_quadrado = a**2 + b**2 + c**2
quadrado_soma = (a + b + c)**2

print(f'A soma dos dos quadrados é de {soma_quadrado:.1f}')
print(f'O quadrado da soma é de {quadrado_soma:.1f}')