"""
by sudoaptipedro
operações com potenciação utilizando numeros inteiros
"""
#declarando as variaveis que receberam os valores
numberOne = int(input("Digite seu numero: "))
numberTwo = int(input("Digite mais um numero: "))

#definição das funções de potenciação com bases ja definidas:

#elevado ao quadrado
def quadrado(x):
    return x**2

#
def cubo(y):
    return y**2

#
def quartaPotencia(z):
    return z**2

#definição das funções de potenciação definidas com bases definidas pelos usuarios:
def potenciaUser(a, b):
    return a**b

#impressão dos resultados:
print("O valor de", numberOne, "elevado ao cubo é:", cubo(numberOne))
print("O valor de", numberOne, "elevado ao quadrado é:", quadrado(numberOne))
print("O valor de", numberOne, "elevado a quarta potência é:", quartaPotencia(numberOne))
print("O valor de", numberOne, "elevado a", numberTwo, "é:", potenciaUser(numberOne, numberTwo))

