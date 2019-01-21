#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa realiza la conversion de grados
centigrados a farenheit, y viceversa.
'''

def grados(x):
    g = 0
    if x == 1:
        x = (x * 9/5.0) + 32
    else:
        x = (x - 32) * 5.0/9
        
    return x



        
