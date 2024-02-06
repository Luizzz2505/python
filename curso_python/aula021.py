# operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# são considerados falsy (para aquela condição é falsa, mas para outras não necessariamente é falsa também) (que você já viu)
# 0 0.0 '' False
# também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida: # esse bloco do if só será executado se toda a expressão for verdadeira (por causa do and)
    print('Entrar')
else:  # como eu não usei o elif, qualquer outra coisa diferente de E que for digitado vai para o bloco do else (diferente de S também)
    print('Sair')

# avaliação de curto circuito
print(True and False and True) # se tiver um False no meio, ele não checa mais nada que tiver depois e retorna na tela o valor False
