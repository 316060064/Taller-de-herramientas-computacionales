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

print "***SUMA DE LOS N PRIMEROS TERMINOS****"
from Problema05 import suma_n
#from Problema05 import sumalista
n = input("Dime hasta que número 'n' quieres sumar: ")

print 'La suma es:',suma_n(n)


               

