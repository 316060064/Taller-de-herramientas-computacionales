
# -*- coding: utf-8 -*-

 
def es_primo(n):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
    
    for i in range(2,n):
        if (n%i) == 0:
            return "No es primo"
    return 'El numero %d es primo' %(n)


