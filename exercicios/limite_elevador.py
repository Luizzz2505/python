# Fazer um programa que leia a capacidade de um elevador e o peso de 5 pessoas.Informar se o elevador está liberado para subir ou se excedeu a carga máxima.

elevador = float(input('Informe a capacidade do elevador: '))
p1 = float(input('Peso pessoa 1: '))
p2 = float(input('Peso pessoa 2: '))
p3 = float(input('Peso pessoa 3:'))
p4 = float(input('Peso pessoa 4: '))
p5 = float(input('Peso pessoa 5: '))

total = p1 + p2 + p3 + p4 + p5

if total <= elevador:
    print('Peso dentro do limite')
else:
    print('Este elevador tem mais peso do que ele aguenta. CUIDADO!')