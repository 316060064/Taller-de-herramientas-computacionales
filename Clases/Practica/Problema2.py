n = input ("Dame el numero a calcular: ")

def suma_cuad(n):
    if n == 1:
        return 1
    else :
        return n**2 + suma_cuad(n-1)


def suma_cuad1(n):
     if n == 1:
        return 1
     else :
        return (n*(n+1)*(2*n+1))/6



print (" El resultado es: "), suma_cuad(n)
print (" y con la formula es : "), suma_cuad1(n) 
    


    















































