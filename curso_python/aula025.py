"""
interpolarização báasica de strings = parecido com o format 
s - string
d e i - int
f - float
x e X Hexadecimal (ABCDEF0123456789)
"""
# isso vem do C

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)