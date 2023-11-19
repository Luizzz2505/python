 # Faça um programa que pergunte o nome do aluno, a quantidade de dias na semana e o tipo de curso (B para básico, I para intermediário e A para avançado)     Mostre o nome do aluno e o valor a ser pago. O valor total é calculado com base nas informações abaixo:
# ●    Caso a opção escolhida for Básico, deverá fazer a seguinte conta:○    Valor Total = (Quantidade de dias na semana *7)*15
# ●    Caso a opção escolhida for Intermediário, deverá fazer a seguinte conta:○    Valor Total = (Quantidade de dias na semana *8,5)*20
# ●    Caso a opção escolhida for Avançado, deverá fazer a seguinte conta:○    Valor Total = (Quantidade de dias na semana *10)*25

nome = input('Insira seu nome: ')
dias = int(input('Informe quantos dias na semana você vai para o curso: '))
curso = input('B - básico I - intermediário A - avançado. Informe qual tipo é o seu curso: ')

if curso.lower() == 'b':
    valor_total = (dias * 7) * 15
elif curso.lower() == 'i':
    valor_total = (dias * 8.5) * 20
elif curso.lower() == 'a':
    valor_total = (dias * 10) * 25
else:
    print('Erro. FIM DO PROGRAMA!')

print(f'{nome} deverá pagar R${valor_total:.2f} no curso')