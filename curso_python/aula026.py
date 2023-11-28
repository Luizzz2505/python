"""
formatação básica de strings 
s - strings 
d - int
f - float
. <número de dígitos>f
x ou X - Hexadecimal 
(Caractere) (><^) (quantidade)
> - esquerda
< - direita
^ centro
Sinal  - + ou -
Ex: 0>-100,.1f
Conversaion flags - !r !s !a
"""

variavel = 'ABC' 

print(f'{variavel}')
print(f'{variavel:>10}') # path -> com isso vai criar a quantidade de espaços que você determinar. 
#como essa variável já possui 3 casas, vai ser criado mais 7, já que eu defini 10. 
# e o sinal de maior ou menor determina que lado vai ser criado os espaços. depende do lado que o sinal está aberto
print(f'{variavel:<10}')
print(f'{variavel:^10}')
print(f'{1000.4879823839842:,.1f}') # essa vírgula adiciona também uma vírgula depois do primeiro número no terminal 
