# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

nome = input('Informe seu nome: ')
senha = input('Insira sua senha: ')

while senha == nome:
    print('Erro! A senha não pode ser igual ao nome')
    senha = input('Insira sua senha novamente: ')
print('Acesso Liberado!')
