#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Pide al usuario una palabra, te dice que
posicion ocupa cada letra (es decir su indice)
y además de cuantas letras esta compuesta
'''
def calcula(txt):
    x=0
    print "Has introducido: ",txt
    for i in txt:
        print  str(i)," Posición ", x
        x+=1

    print "Total de letras: ", str(x)

    


 


