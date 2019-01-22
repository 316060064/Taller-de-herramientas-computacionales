#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa realiza la conversion de grados
centigrados a farenheit, y viceversa.
Intente realizar las dos versiones, es decir
Problema03 y S, con listas y me due imposible :(

'''
'''
from Problema03 import grados
x = input ("¿Qué quieres convertir \n" +
           "1.-Cª - Fª o 2.- Fª - Cª?: ")
x = input ("Cantidad: ")

print grados(x)'''


#from Problema03 import grados

lista = []
r= 0
s=0
for x in range(1):
    x = input ("¿Qué quieres convertir \n" +
           "1.-Cª - Fª o 2.- Fª - Cª?: ")
    lista.append(x)
    
    x = input ("Cantidad: ")
    lista.append(x)
    s = s + lista[0]
    r = r + lista[1]

    if s == 1:
            y = ( r* 9/5.0) + 32    
    
    else:
            y = (r - 32) * 5.0/9

    print y
    



