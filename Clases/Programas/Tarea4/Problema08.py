#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
A partir de un número n dado por el usuario
te calcular su factorial 
'''


def factorial(n):
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f




