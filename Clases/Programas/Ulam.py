# -*- coding: utf-8 -*-
def ulam(x):
    #if (x/2)*2-x == 0:
    if x%2 == 0:  # Estuve atorado usando solo con una funcion, e intentando
                   #   con las formulas de impar y par, es decir 2*x y 2*x-1. Y ademas pense que
                   #   podría realizarlo con un while dentro de un if

        return x/2
    else :
        return 3*x + 1

def suc(x):
    i=0
    #while x>1:
    while x!=1:
        x=ulam(x)
        i=i+1
    return i
        


print suc(7)
print suc(26)
print suc(52)
print suc(1024)
print suc(72)
print suc(1524927)
print suc(2)



    



    
