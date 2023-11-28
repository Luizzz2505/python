"""
fatiamento de strings
012345678
olá mundo
-987654321
fatiamento [i:f:p] início, fim, passo / [::]
obs: a função len retorna a quantidade de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[5]) # aqui vai mostrar a letra correspondente ao que está na variável (sempre começa a contar do zero)

# fatiamento 
print(variavel[4:]) # já que é para ir até o final, não se faz necessário colocar o restante. o final não é incluído. também pode ser usado essa lógica para omitor o começo e só declarar o final

print(len(variavel)) # len vai contar quantos caracteres possui, incluindo os espaços em branco
print(variavel[0:len(variavel):2]) # esse 2 no final é de passo. que é pra informar de quantos em quantos vai ser passado pela variável. nesse exemplo, vai ser mostrado no terminal "Oámno"

print(variavel[::-1]) # nesse caso a string vai ser invertida, deixando a frase de trás para frente
