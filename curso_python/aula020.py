# EXERCÍCIO

primeiro_valor = input('Informe um valor: ')
segundo_valor = input('Informe outro valor: ')

# f-strings
if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'Os valores são iguais')
else:
    print(f'{segundo_valor} é maior que {primeiro_valor}')