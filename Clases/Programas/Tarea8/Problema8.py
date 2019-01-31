#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Josue Hernandez Rodriguez, 316060064
Este programa te regresa el valor absoluto del maximo
y minimo de una lista de números. Le pondria a la funcion
def absmaxmin(l)
'''

def g(l):
    a = 0

    for i in l:
        for j in l:
            if abs(i-j) > a:
                a = abs(i-j)
    return a



print g([2,9,8,7,45,12])
