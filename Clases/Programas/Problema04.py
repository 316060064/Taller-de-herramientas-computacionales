x = 0
x = 1
def fib(x):
    
    if x == 1:
        print 0

    if x == 2:
        print 1

    if x == 3:
        print 1

    if x >= 4:
        x = (x-1)+(x-2) 

    return x 



print fib(4)
print fib(5)
