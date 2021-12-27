#declarando variáveis que receberam os numeros:
numOne = int(input("Digite um numero: "))
numTwo = int(input("Digite um outro numero: "))

#criação das funções:
#função de soma:
def somar(a, b):
    return a + b

#função de subtração:
def subtrair(a, b):
    if a > b:
        return a - b 
    else:
        return ((a - b)* -1)

#função de multiplicar:
def multiplicar(a, b):
    return a*b

#função de dividir:
def dividir(a, b):
    return a/b

#imprimindo valores:
print('valor da adição eh: ', somar(numOne, numTwo))
print('valor da subtração eh: ', subtrair(numOne, numTwo))
print('valor da multiplicação eh: ', multiplicar(numOne, numTwo))
print('valor da divisão eh: ', dividir(numOne, numTwo))
