#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa realiza la conversion de grados
centigrados a farenheit, y viceversa.
'''

from Problema03 import grados
x = input ("¿Qué quieres convertir \n" +
           "1.-Cª - Fª o 2.- Fª - Cª?: ")
x = input ("Cantidad: ")

print (grados(x))
