# input é uma função que solicita ao usuário para ele inserir dados
input('Qual o seu nome? ') # recomenda-se deixar um espaço em branco ao final da str do input
# ela sozinha não faz nada com os dados

# aqui quando o usuário inserir o dado, ele vai sair da função e ir para a variável. Sempre em forma de string
# então as vezes vai se fazer necessário fazer a coerção do tipo do dado
 nome = input('Qual o seu nome? ')
 print(f'O seu nome é {nome}')


numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
# aqui vai haver a concatenação porque são duas strings e não int ou float
print(f'A soma dos número é: {numero_1 + numero_2}')

# para resolver esse problema, eu posso criar uma nova variável e nela colocar a coerção da variável que eu quero
int_numero_1 = int(numero_1) # agora sim a variável de cima seria somada
int_numero_2 = int(numero_2)
# aqui sim vai haver a soma dos números
# mas se o valor for uma string, o código quebra no terminal
print(f'A soma dos número é: {int_numero_1 + int_numero_2}')
