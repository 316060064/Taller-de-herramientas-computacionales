
n = input ("Dame el numero a calcular: ")

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
    



    















































