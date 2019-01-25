#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Lo que hice fue usar la recursividad para que sume los cuadrados de los
n numeros anteriores al numero dado, y si es 1 regrese el 1.
'''



n = input ("Dame el número a calcular: ")

def suma_cuad(n):
    if n == 1:
        return 1
    else :
        return n**2 + suma_cuad(n-1)


def suma_cuad1(n):
     if n == 1:
        return 1
     else :
        return (n*(n+1)*(2*n+1))/6



print (" El resultado es: "), suma_cuad(n)
print (" y con la formula es : "), suma_cuad1(n) 
    


    















































