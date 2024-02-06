# Escreva um programa que solicite dois números do usuário e exiba o resultado da divisão do primeiro número pelo segundo. Use try/except para tratar o caso em que o segundo número é zero.

try: 
    n1 = int(input('Insira um valor: '))
    n2 = int(input('Insira outro valor: '))
    
    divisao = n1 / n2
    print(f'A divisão de {n1} com {n2} é {divisao}')
except ZeroDivisionError:
    print('Erro! Não é possível dividir por zero')
except ValueError:
    print('insira valores válidos')


