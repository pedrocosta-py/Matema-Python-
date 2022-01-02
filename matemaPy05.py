"""

by: sudoAptIPedro
Operações com polinômios:
º Adição
º Subtração
º Divisão
º Multiplicação

"""
from numpy import *

print("Bem Vindo ao programa de operações com polinômios! \n Por favor, digite seus os dados numéricos abaixo: \n")
#atribuição dos valores:

#primeiros polinômios:
# ax**2
a = int(input("Entre com o valor de ax**2:")) 
#bx
b = int(input("Entre com o valor de bx:"))
#c
c = int(input("Entre com o valor de c:"))

#segudos polinômios:
# ax**2
a2 = int(input("Entre com o valor de ax**2:")) 
#bx
b2 = int(input("Entre com o valor de bx:"))
#c
c2 = int(input("Entre com o valor de c:"))

#variavel auxiliar que recebe os valores e tranforma em lista
aux = [a, b, c]
aux2 = [a2, b2, c2]

#criação das funções:

#função de adição:
def polySoma(value1, value2):
    return polyadd(value1, value2)

#função de subtração: 
def polySub(value1, value2):
    return polysub(value1, value2)

#função de divisão:
def polyDiv(value1, value2):
    return polydiv(value1, value2)

#função de multiplicação de polinômios:
def polyMulti(value1, value2):
    return polymul(value1, value2)

#interção com o usuário:
option= int(input("Qual função deseja escolher? \n [1] soma \n [2] subtração \n [3] divisão \n [4] multiplicação \n -->"))
 
if(option == 1):
    print(polySoma(aux, aux2))

elif(option==2):
    print(polySub(aux, aux2))

elif(option==3):
   print(polyDiv(aux, aux2))

elif(option==4):
    print(polyMulti(aux, aux2))

else:
    print(" \n Digite um valor válido!! \n ")


