#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa le pide al usuario una cadena, y
la invierte, es decir invierte el orden de las
letras empezando desde la última hasta la primera
'''



def inversa(cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida







