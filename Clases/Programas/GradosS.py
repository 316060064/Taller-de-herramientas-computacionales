from Grados import *


L1 = listaC(-15,32,10)
L2 = listaF(L1)
mostrarListas(L1,L2)
mostrarListas1(L1,L2)

a=input("Cual es el extremo izquierdo del intervalo")
b=input("Cual es el extremo derecho del intervalo")
n=input("Cuantos subintervalos")


print "   C      F"

L1 = listaC(a,b,n)
L2 = listaF(L1)
mostrarListas(L1,L2)
