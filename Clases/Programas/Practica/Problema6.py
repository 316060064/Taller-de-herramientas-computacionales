#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Lo que hice fue usar while, y poner como
condicion que mientras n sea mayor a 1 se repita el pro-
ceso hasta que no sea 1
'''

def fac(n):
    
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f
 
    
