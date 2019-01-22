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
    y= 0
    L = []
    R = []
    print "Has introducido: ",txt
    #for i in txt:
        #print  str(i)," Posición ", x
        #x+=1
        
    for i in txt:
        L.append(i)
        
    for i in txt:
        R.append(y)
        y+=1
        
    print zip(L,R)
    
        
        

    #print "Total de letras: ", str(x)



#print    calcula("josue")

    


 


