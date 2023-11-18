# #  Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

nome = input('Digite seu nome: ')
resposta = input(f'Olá, {nome}! Você gosta do seu nome? Digite sim ou não: ')

# aqui usei o .lower para caso o usuário digitar uma letra maiúscula, o programa força ela para virar minúscula
if resposta.lower() == 'sim':
    print(f'Que bom, {nome}! Amor próprio é tudo')
elif resposta.lower() == 'não':
    print('Putz! Sinto muito')
else:
    print('Resposta inválida!')