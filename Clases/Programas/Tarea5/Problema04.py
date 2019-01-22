#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Josue Artemio Hernandez Rodriguez, 316060064
Este programa te pide un número y a partir de
ese te calcula la suma del enesímo termino de la
sucesion de Fibonacci
'''
'''
def fib(n):     
    if n < 2:
        return n
    else:
        #fn = fn-1 + fn-2
            
        return fib(n-1) + fib(n-2)
            #lista.append(fib(n-1) + fib(n-2))
            #print lista
    for x in range(n):
            print(fib(x))         
    '''

def fib(n): 
    fibs = [0, 1] 
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

    
        
        




   
    




