# operador lógico "not"
# usado para inverter expressões 
# not True = False 
# not False = True 

senha = input('Senha: ')

if not senha:
    print('Entrou')
else:
    print('Senha incorreta.')

print(not True) # False 
print(not False) # True