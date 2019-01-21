#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa le pide al usuario una cadena, y
la invierte, es decir invierte el orden de las
letras empezando desde la última hasta la primera
'''
from Problema09 import inversa

cadena = input("Dame una palabra cualquiera entre comillas: ")

print 'La inversa de la palabra es: ', inversa(cadena)
