# Peça ao usuário para inserir os comprimentos dos lados de um triângulo e determine se é equilátero, isósceles ou escaleno.

from time import sleep

lado1 = float(input('Primeiro lado do triângulo: '))
lado2 = float(input('Segundo lado do triângulo: '))
lado3 = float(input('Terceiro lado do triângulo: '))

print('PROCESSANDO...')
sleep(2)
# equilátero
if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Seu triângulo é equilátero')
# isósceles
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Seu triângulo pe isósceles')
else:
    print('Seu triângulo é escaleno')

# fim
print('Fim do Programa!')