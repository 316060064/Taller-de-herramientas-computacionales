#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Te pide diez numeros separados con comas, y de
estos te calcula el promedio.
Me ayudo bastante el ejercico anterior para que
este me quedara mas rápido
'''

'''
def prom(a,b,c,d,e,f,g,h,i,j):
    s = a+b+c+d+e+f+g+h+i+j
    r = s/10.0
    return r'''



def prom(n): 
    L = []
    for i in range(n):
        valor = input("Dame el numero: ")
        L.append(valor)
        suma=0
        for i in L:
            suma += i
            p = float(suma)/n
    return p





