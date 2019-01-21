#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
A partir de un número n dado por el usuario
te calcular su factorial 
'''


print "******Calculo de n factorial******"
from Problema08 import factorial
n = input("Dame el numero al cual calcular su factorial: ")

print "El factorial de %d es el siguiente: %d" % (n,factorial(n))

