#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
En este problema se busca el máximo común divisor
de dos numeros especificados por el usuario.
'''

def mcd(a, b):
	resto = 0
	while b > 0:
		resto = b
		b = a % b
		a = resto
	return a
