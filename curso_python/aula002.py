# é usada para imprimir coisas na tela
# elas recebem argumentos
print(12, 34) # a vírgula por padrão cria um espaço no terminal
print(56, 76) # cada print é uma linha nova no terminal

# \r\n -> CRLF (quebra de linha)
print(12, 34, 1011, sep='-') # o sep faz com que o separador dos argumentos (nesse caso não nomeados) seja substituídos pelo que você colocar
print(56, 78, sep=".")

#\n também serve para quebrar a linha. Pode ser usado em alguns caso, se for preciso
print(987, 765, sep='-', end='##') ## o end faz com que no lugar da quebra de linha fique o caracter que eu mandei 
print(777)
