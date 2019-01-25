#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Lo que hice fue hacer la funcion con if, elif,
y else, donde los valores que dan 1 y 0 ponerlos dentro de
if y elif y todos los valores que no sean los que tiene de
condicion if y elif los puse en else.
El inciso b) solo es hacer la funcion que me pida en el shell un
número y apartir de ahi calcule mediante las condiciones dadas.

'''


from math import sin
from math import pi
def H_eps(x, eps=0.01):
    if x < -eps:
        return 0
    elif x > eps:
        return 1
    else:
        H_eps = 1/2.0 + float(x/2*eps) + float(1/2*eps)* float(sin((pi*x)/eps))
        return H_eps


from math import sin
from math import pi
x = input("Dame un número tal que cumpla lo siguiente \n" +
          "(x < -0.01,  x = -0.01,  x=0,  x = 0.01 , x > -0.01): ")
def prueba_H_eps(x, eps=0.01):
     
    if x < -eps:
        return 0
    elif x > eps:
        return 1
    else:
        H_eps = 1/2.0 + float(x/2*eps) + float(1/2*eps)* float(sin((pi*x)/eps))
        return H_eps

print prueba_H_eps(x, eps=0.01)

    
    
    
    
