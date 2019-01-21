#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa te pide diez números, y a partir
de estos de dice cual es el mayor, el menor y
su promedio.
'''

from Problema07 import mayor
from Problema07 import menor
from Problema07 import prom

n1,n2,n3,n4,n5,n6,n7,n8,n9,n10 = input("Dame díez números separados con comas \n"  +
                                       "y te dire cúal es el mayor, menor y su \n"
                                       "promedio: ")

print 'El numero mayor es: ', mayor(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
print 'El numero menor es: ', menor(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
print 'El promedio es: ', prom(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
