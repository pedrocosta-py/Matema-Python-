"""
by: sudoAptIPedro

Calculo de funções trigonométricas:

"""
from math import pi, sin

#define uma função senoidal
def funcaoSin(x):
    return 2*sin(x/4)

t = funcaoSin(pi/2) #usa a função funcaoSin() em radianos para o argumento pi/2

print('\n')
print("O resultado da função funcaoSin em radianos para o argumento pi/2 é: ", t)

t = funcaoSin(3*pi) #usa a função funcaoSin() em radianos para o argumento 3*pi

print('\n')
print("O resultado da função funcaoSin em radianos para o argumento 3*pi é: ", t)