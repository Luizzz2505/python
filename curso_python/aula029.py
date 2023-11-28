"""
introdução ao try / except 
try -> tentar executar o código
except -> ocorreu erro ao tentar executar 
"""

numero_str = input('Vou dobrar um número que você digitar: ')

# print(numero_str.isdigit()) # checa se o usuário digitou apenas números (ponto não conta). retornando um boolean

# print(f'O dobro de {numero_str} é {numero_str * 2}') # dessa forma vai somente concatenar os valores porque minha variável está definida como string no input 

# # para resolver o problema eu fiz a conversão (essa foi usada pelo professor. eu prefiro usar diretamente no input)
# numero_float = float(numero_str)
# print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')