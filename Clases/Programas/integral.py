#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
En este problema se busca el máximo común divisor
de dos numeros especificados por el usuario.
'''




import numpy as np

def funcion(x):
    y = -6*x**3+5*x**2+2*x+12
    return y

b= float(input("Introduce el limite superior: "))

a =float(input("Introduce el límite inferior: "))
n = (input("Introduce el número de trapecios: "))
x =  np.zeros([n+1])
h= (b-a)/n
x[0]= a
x[n]= b
suma=0

for i in np.arange(1,n):
    x[i]= x[i-1]+h
    suma = suma + funcion(x[i])

integral =(h/2)*(funcion(x[0])+2*suma+funcion(x[n]))
print "El resultado de la suma es: ", integral
