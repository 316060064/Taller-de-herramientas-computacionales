#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Similar a la del problema de la pelota, pero en este se busca
son los timpos en que alcanza una altura especifica.
'''
import math
def tiempo(h):

    v0 = 34
    g = 9.81
    t1= ((-v0) + math.sqrt(v0**2-2*g*(h)))/(-g)
    t2= ((-v0) - math.sqrt(v0**2-2*g*(h)))/(-g) 
    return t1, t2
    




