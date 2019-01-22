#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
A partir de un número n dado por el usuario
te calcular su factorial.

Tenia la idea de que me preguntara por cuantos
valores ingresar, darlos y calcularle su factorial
pero no encontre la forma y me fui atorando más.
'''


def factorial(n):   
    L=[]
    f = 1
    cache = n
    while n > 1:
        f *= n
        n -= 1
        
    L.append(f)
    return L
            
        








