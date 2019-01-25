#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Similar al problema anterior. solo cambia el
numero al que se eleva la función. Usando la recursividad
se resuelve, dado un numero n, se calculo la suma de los
cubos anteriores a esa n

'''
n = input ("Dame el número a calcular: ")

def suma_cub(n):
    
       
    if n == 1:
        return 1
    else :
        #suma = n**3 + suma_cub(n-1)
        return n**3 + suma_cub(n-1)
    
        
def suma_cub1(n):
    if n == 1:
        return 1
    else:
        p = (n*(n+1)/2)**2
        return p

print (" El resultado es: "), suma_cub(n)
print (" y con la suma es : "), suma_cub1(n) 
    



    















































