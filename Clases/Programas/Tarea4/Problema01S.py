#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
En este problema se busca el máximo común divisor
de dos numeros especificados por el usuario.
'''
from Problema01 import mcd

n1 = input("Introduce el primer numero: ")
n2 = input("Introduce el segundo numero: ")
 
print "El máximo común divisor de %d y %d es %d" % (n1, n2, mcd(n1,n2))




