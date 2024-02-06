vendas = [100, 50, 130, 80, 120, 200]
#          0    1   2   3    4    5  - posição dos valores na lista. Sempre começando do 0]

print(vendas[0]) # primeiro elemento

# para pegar o último valor, basta usar o -1. Usar o número negativo faz com que pegue os valores da direita para a esquerda
print(vendas[-1]) # último elemento
print(vendas[-2]) # penúltimo elemento

# para fazer a soma dessa lista, basta usar o sum + o nome que foi atribuído a ela

total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(f'Você fez {len(vendas)} vendas') # teste de len com fstring

valor_max = max(vendas)
valor_min = min(vendas)
print(f'A maior venda foi de {valor_max}')
print(f'A menor venda foi de {valor_min}')

# descobrir posição na lista

posicao = vendas.index(130)
print(posicao)

# verificar se tal produto existe na minha lista 

# produtos = ['iphone', 'ipad', 'airpod']
# produto_usuario = input('digite onome de um produto: ')
# print(produto_usuario in produtos)

# editar valores 

produtos = ['iphone', 'ipad', 'airpod']
precos = [4000, 8000, 2000]

print('iphone' in produtos)
precos[0] = precos[0] * 1.1 # 10% de aumento
print(precos)
