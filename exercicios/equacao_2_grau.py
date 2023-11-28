# faça um programa que resolva uma equação de segundo grau

a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = -b + delta ** 0.5
    x2 = -b - delta ** 0.5
    print(f'Duas raízes reais e distintas: {x1}, {x2}')
elif delta == 0:
    x = -b / (2 * a)
    print(f'Uma raiz real (raiz dupla): {x}')
else:
    parte_real = -b / (2 * a)
    parte_imaginaria = (abs(delta) ** 0.5) / (2 * a)
    print(f'Raízes complexas: {parte_real} + {parte_imaginaria} i e {parte_real} - {parte_imaginaria} i')

