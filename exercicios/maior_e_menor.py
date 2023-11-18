# Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

primeiro = int(input('Insira um número: '))
segundo = int(input('Insira outro número: '))
terceiro = int(input('Insira mais um número: '))

maior = primeiro
menor = segundo

# maior valor
if primeiro > segundo and primeiro > terceiro:
    maior 
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

# menor valor
if primeiro < segundo and primeiro < terceiro:
    menor = primeiro 
if segundo < primeiro and segundo < terceiro:
    menor = segundo 
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')