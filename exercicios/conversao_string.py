# Peça ao usuário para digitar um número como string. Tente converter a string para um inteiro usando int(). Use try/except para lidar com a situação em que a entrada não é um número válido.

try:
    numero = input('insira um número: ')
    numero_int = int(numero)
    print(f'Você digitou {numero_int}')
except ValueError:
    print('Error!!')