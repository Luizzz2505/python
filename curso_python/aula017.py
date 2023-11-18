# if / elif       / else
# se / se não se / se não 

# else: # contrário de if

condicao1 = False 
condicao2 = False
condicao3 = True
condicao4 = True

# SEMPRE executa somente uma condição do bloco inteiro

if condicao1:
    print('Código para condição 1')
elif condicao2: # caso eu tenho outra condição, ela deve ser um elif
    print('Código para condição 2')
elif condicao3: # como essa condição foi verdadeira, qualquer bloco depois desse será pulado, mesmo sendo verdadeiro também
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else: # else já vem com os dois pontos
    print('Nenhuma condição foi satisfeita')

if 10 == 10:
    print('Outro if')

print('Fora do if') # aqui já não está mais do bloco do if porque não está no padrão da identação