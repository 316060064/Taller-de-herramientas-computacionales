#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josué Artemio Hernández Rodríguez

Cuenta el numero de letras en una cadena, entonces le pondria
def contador(l)
'''


def f(l):
    a = 0
    b = 0
    for i in l:
        if i > 0:
            a += 1
        else:
            a -= 1
    return a + b
