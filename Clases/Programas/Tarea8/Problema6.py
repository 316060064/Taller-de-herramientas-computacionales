#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josué Artemio Hernández Rodríguez, 316060064
'''

def moverTorre(altura,origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)

moverTorre(3,"A","B","C")
