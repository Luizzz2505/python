# Leia a distancia em ˆ Km e a quantidade de litros de gasolina consumidos por um carro
# em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com
# a tabela abaixo:
# CONSUMO (Km/l) MENSAGEM
# menor que 8 Venda o carro!
# entre 8 e 14 Economico! ˆ
# maior que 12 Super economico!

distancia = float(input('Informe quantos KMs seu carro percorreu: '))
litros = int(input('Quantos litros de gasolina seu carro consumiu? '))

consumo = distancia / litros 

if consumo < 8:
    print('Venda o carro!')
elif 8 <= consumo <= 14:
    print('Econômico')
else:
    print('Super econômico')
