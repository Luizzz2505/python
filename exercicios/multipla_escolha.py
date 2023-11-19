# Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

print('Qual a capital do Brasil: ')
print('a) Brasília',  'c) Rio de Janeiro')
print('b) São Paulo',  'd) Porto Alegre')

resposta = input('Insira a letra: ')

if resposta == 'a':
    print('Você acertou!')
else:
    print('Você errou!')