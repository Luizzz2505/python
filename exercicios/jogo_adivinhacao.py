# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
# escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint # importar o random
from time import sleep # importei essa função para o programa demorar alguns segundos antes de executar os comandos seguintes
computador = randint(0, 5) # este comando faz o computador sortear um número no intervalo que eu defini

print('-=-' * 24)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar se for capaz')
print('-=-' * 24)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('Você conseguiu me vencer!')
else:
    print('ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))
print('Fim do programa!')

