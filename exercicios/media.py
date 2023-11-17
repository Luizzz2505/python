# Crie um programa que solicite ao usuário as notas de três disciplinas e calcule a média. Exiba o resultado formatado usando f-strings.

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
nota3 = float(input('Informe sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f'Sua média foi de {media}')