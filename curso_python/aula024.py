# operadores in e not in
# strings são iteráveis  = navegar item por item
# 0 1 2 3 4 5 
# O t á v i o -> iterável
# -6-5-4-3-2-1

# in = está entre 
# in not = não está entre

nome = 'Otávio'
print(nome [2])
print(nome [-4])

print('á' in nome) # se "á" estiver entre as letras da variável, vai ser retornado True
print('z' in nome)
print('vio' in nome) 
print(10 * '-') # usei para deixar meu terminal mais organizado para vizualizações
print('á' not in nome) # se não está
# print('z' not in nome) # retorna True porque not inverte a expressão (não está entre)

nome = input('Digite seu nome: ')
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')