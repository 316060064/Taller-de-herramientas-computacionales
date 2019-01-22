#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa realiza la suma de los primero
n naturales, donde esa n la da el usuario.
Estaba comentiendo el error en el for, el cual
estaba alineado con el anterior, y este deberia
estar dentro.
'''
'''
def suma_n(n):
    n >=1
    r = n*(n+1)/2

    return r  '''

'''
def suma_n(n): 
    L = [0,1] 
    for i in range(1, n):
        L.append(len(L))
        suma=0
    for i in L:
            suma += i
    return suma'''


def suma_n(n): 
    L = [0,1] 
    for i in range(1, n):
        L.append(len(L))
        suma=0
        for i in L:
            suma += i
    return suma







    
    













