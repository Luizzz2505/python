""""
DocString -> documentação

Python = linguagem de programação
Tipagem = dinâmica / forte -> a linguagem já sabe que tipo de informação eu estou passando / 
str -> string -> texto
Strings são textos que estão dentro de aspas

"""

print(1234)

# aspas simples 
print(1, 'Luiz Francisco', sep="-")

# aspas duplas
print(2, "Linguagem de programação", sep="-")

# escape 
print(3, "Python \'VsCode\'", sep="-") # \' para o interpretador não ler de forma errônia as aspas que eu quero inserir no nome

# melhor forma de colocar aspas numa string 
print(4, 'Estou aprendendo "Python"', sep="-") # começar com aspas simples e usar as duplas depois