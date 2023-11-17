# formatação de string com o método format
a = 'A'
b = 'B'
c = 1.1
# com os valores (índices) dentro das chaves eu não dependo mais da ordem que as variáveis está no format
formato = 'a= {0} a={0} a={0} b={1} c={2:.2f}'.format(a,b,c)

print(formato)