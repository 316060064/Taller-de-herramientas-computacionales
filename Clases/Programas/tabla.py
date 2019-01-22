
gradosC = [-10,-5,0,5,10]
gradosF = [-10*9.0/5 +32, -5*9.0/5+32, 0*9.0/5+32, 5*9.0/5+32, 10*9.0/5+32]
'''list(zip(gradosC,gradosF))
for c, f in zip(gradosC,gradosF):
    print ("{} grados centigrados: {} grados Farenheit".format(c,f))'''




table = [[C,F] for C,F in zip(gradosC,gradosF)]

print table
from pprint import pprint

pprint(table)

    



