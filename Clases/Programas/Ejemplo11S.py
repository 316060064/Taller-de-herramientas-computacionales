# -*- coding: utf-8 -*-
#/usr/bin/python



n = input ("¿Cuantos valores?: ")
L = []
for i in range(n):
    valor = input("Dame el valor")
    L.append(valor)

M = range(n)
for i in M:
    valor = input("Dame el valor")
    M[i](valor)

N= range(n)
j=0
while j<n:
    valor = input("Dame el valor")
    N[i](valor)
    
             

L = range(n)
print "La lista es de tamaño %d" % (len(L))
print L




