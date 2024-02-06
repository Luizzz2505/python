""""
O bloco 'try/except' é usado para tratar exceções, ou seja, para tratar erros na execução do código. 

"""

# nunca é bom deixar um bloco de 'try/except' genérico. É sempre bom especificar o tipo de erro que você está esperando
try:
    numero = int(input('Digite um número: '))           
    print(numero)

    10/0
except ZeroDivisionError: # esssa linha eu especifico que o tipo de erro que espero é que divisão por zero não é possível
    print('Divisão por zero não é possível')
except ValueError:
    print('Digite um valor válido')
except:
    print('Erro inesperado')
finally: # aqui independente de qual erro o dado cair, esse trecho sempre será executado
    print('Sempre executa')