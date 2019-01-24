def fib(n):

    '''Calcula el enesimo termino
de la sucecsion de fibonacci con n natural
'''


    if n> 2:
        return fib(n-1) +fib(n-2)
    else:
        return 1

    


fib(1)

fib(2)
fib(5)
fib(10)



def suma(n):
    
    if n == 1:
        return 1
    else:
        n = n+suma(n-1)
    return n


def suma(n):
    
    if n>1:
        return n + suma(n-1)
    else:
        return (1)


def printR(L):
    
    if L:
        print L[0],
        printR(L[1:])
    else:
        None


def printR1(L):
    #global T
    T =25
    if len(L)> 1:
        print L[0],
        printR(L[1:])
        
    else:
        print(L[0])


def f1():
    return 2*x

T=[-8,5,4,5,-3]
L=[-8,5,4.5,3]
printR([8,7,4,5,3,2,1,5])
printR1([8,7,4,5,3,2,1,5])
print "*------------*"        
x=15
print f1()
print T



