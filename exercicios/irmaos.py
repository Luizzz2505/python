# Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

irmao = input('Você tem irmãos: ')

if irmao.lower() == 'sim':
    quantidade = input('Que legal! Quantos irmãos você tem? ')
    print(f'Bom saber que você tem {quantidade} irmãos')
elif irmao.lower() == 'não':
    queria = input('Você gostaria de ter? ')
    print('Entendi')
else:
    print('Fim do programa')

