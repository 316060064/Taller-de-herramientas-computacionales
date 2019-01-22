#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
En este problema se busca el máximo común divisor
de dos numeros especificados por el usuario.
'''
from Problema01 import mcd
n = []
n1= input("Introduce el primer número: ")
n2 =input("Introduce el segundo número: ")
n.append(n1)
n.append(n2)
 
print "El máximo común divisor de %d y %d es %d" % (n[0],n[1], mcd(n1,n2))





