# conversão de tipo, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

# nesse caso está acontecendo um polimorfismo, porque está sendo usando o mesmo operado para fazer coisas diferentes
print(1 + 1) # somou
print('a' + 'b') # concatenou -> juntou

#  aqui o código dá erro, pois só é permitido concatenar valores do mesmo tipo
# tipagem forte é quando a linguagem não consegue converter os tipos. um tipo de dado não consegue ser tratado como se fosse de outro
# print('1' + 1)

print('1', type('1'))

# fazer a conversão de tipo (coerção)
print(int('1'), type(int('1'))) # esse 1 normalmente seria uma string, por estar entre aspas, 
# mas quando eu fiz a coerção defini para que ele seja inteiro

# para somar string com inteiro
print(int('1') + 1)
print(float(1) + 1) # uma operação de float com inteiro o resultado é float

# teste 
print(float(1), type(float(1)))
print(bool(' '))
print(str(11) + 'b') # aqui faz a concatenação, pois é str com str