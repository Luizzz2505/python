# Crie um programa que solicite dois números ao usuário e exiba a soma, subtração, multiplicação e divisão desses números usando f-strings.

# aqui eu fiz a coerção porque a função input define os dados como str
numero_1 = float(input('Insira um número: '))
numero_2 = float(input('Insira outro número: '))

# aqui vou fazer com todos os operadores lógicos para fixar 
adicao = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
potenciacao = numero_1 ** numero_2
divisao_int = numero_1 // numero_2
mod = numero_1 % numero_2

print(f'Soma: {adicao}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Potenciação: {potenciacao}')
print(f'Divisão inteira: {divisao_int}')
print(f'Mod: {mod}')