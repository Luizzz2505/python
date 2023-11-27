# operadores lógicos
# and (e) or (ou) not (não)
# or - qualquer condição verdadeira avalia toda expressão como verdadeira 
# se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# para permitir as duas versões do 'e'
# colocar parênteses para dar prioridade a uma expressão, porque quanto mais expressão tiver na condição mais complexa ela fica
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# avaliação de curto circuito
