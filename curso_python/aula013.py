nome = 'Luiz Francisco'
altura = 1.70
peso = 80
imc = peso / altura ** 2

# formatação de string
# f-strigs
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
# com a utilização do f no começo da string, me permite usar variáveis dentro do texto. E para fazer isso basta envolvê-las  em chaves
# na parte de altura eu adicionei :.2f porque faz com que no terminal seja exibido mais casas decimais. (no lugar do 2 pode ser qualquer outro valor)
# para usar uma vírgula num valor, basta colocar também uma vírgula antes do ponto (:,.2f)
print(linha_1)
print(linha_2)
print(linha_3)