# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input('Insira um número para saber o dia correspondente a ele:'))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-feira')
elif dia == 3:
    print('terça-feira')
elif dia == 4:
    print('Quarta-feira')
elif dia == 5:
    print('Sexta-feira')
elif dia == 6:
    print('Sábado')
else:
    print('Número inválido')