# variáveis são usadas para salvar algo na memória do computador 
# PEP8: inicie variáveis com letras minúsculas, pode usar número e underline
# o sinal de = é o operador de atribuição. Ele é usado para atribuir valor a  um nome (variável)
# uso: nome_variavel = expressão

# variáveis
nome_completo = 'Luiz Francisco Costa Neto'
soma_dois_mais_dois = 2 + 2
int_um = int('1') # aqui eu fiz a coerção de str para int (o 1 está estre aspas)

print(int_um, type(int('1')))
print(nome_completo, soma_dois_mais_dois)

# variáveis são usadas para deixar o código mais legível e não precisar estar repetindo sempre a mesma expressão

nome = 'Luiz'
idade = 19
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade', idade)
print('É maior?', maior_de_idade)
