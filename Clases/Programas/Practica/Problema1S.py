#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Lo que hice fue crear una lista graC, graF, aC, y dif.
Y el valor dado como gradosC se mete en la lista graC
y asi sucecivamente con los demás, y luego generar
una lista de listas con los datos con la funcion zip.
'''


from Problema1 import lista
def mos_lista(graF,graC,aC,dif):
    for F, C, E,D in zip(graF,graC. aC, dif):
        print '%f %f %f %f ' %(C,F,E,D)

print "Escribe lista(#)"
