# Crie um programa que solicite ao usuário seu nome, idade e cidade de residência, e depois exiba essas informações formatadas usando f-strings.

nome = input('Informe seu nome: ')
idade = int(input('Insira sua idade: '))
cidade = input('Informe sua cidade: ')

print(f'Seu nome é: {nome}')
# aqui eu não usei o f-strings para treinar outra forma
print('Você tem:', idade, 'anos')
print(f'Você mora em: {cidade}')