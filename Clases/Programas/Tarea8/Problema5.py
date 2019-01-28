'''L= []

l1 = [True, True, True]
l2 = [False, False, False]
l3 = [True, True, True]

L.append(l1)
L.append(l2)
L.append(l3)'''


'''
L = [[True, True,  True, True],
    [False, False, False, False],
    [True,  True,  True, True]]

L1 = [[1, 1,  1],
    [0, 0, 0],
    [1,  1,  1]]

def resolver(L,e):
    n = len(L[0])
    x = e[0]
    y = e[1]
    #if hay salida:
    if y == n-1:
        return e[0]+1,e[1]+1 
    else:
        if L[x][y+1] == False:
            e = [x,y+1]
            return resolver(L,e)

        
e= [1,0]        
r =resolver(L,e)'''

L =[[ True, True,   True, True],
    [False, False, False, True],
    [True,  True,  False, True]]

L1 = [[1, 1,  1, 1],
      [0, 0,  0, 1],
      [1, 1,  0, 1]]

def resolver(L,e):
    print e
    n = len(L[0])
    m=len(L)
    x = e[0]
    y = e[1]
    #if hay salida:
    if y == n-1 or x == m-1:
        return e[0]+1,e[1]+1 
    else:
        if L[x][y+1] == False:
            e = [x,y+1]
            return resolver(L,e)
       # else:
        #        if L[x+1][y] == False:

        elif L[x+1][y] == False:
                e = [x+1,y]
                print e
                return resolver(L,e)
        else:
            print "ya no puede avanzar al frente"
            
                
           
type(L)                      
e= [1,0]        
r =resolver(L,e)
import numpy as np
print (np.matrix(L))
    
    
    
