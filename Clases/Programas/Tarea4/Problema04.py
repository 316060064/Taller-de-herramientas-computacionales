#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa te pide un número y a partir de
ese te calcula la suma del enesímo termino de la
sucesion de Fibonacci
'''


def fib(n):
    
    if n < 2:
        return n
    else :
        return fib(n-1) + fib(n-2)




