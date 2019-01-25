def lista(gradosC):
    
    graC=[]
    graC.append(gradosC)
    graF = []
    aC = []
    dif = []
    for C in graC:
        F = (9.0/5)*C + 32
        graF.append(F)
        aproxC = (F-30)/2.0
        aC.append(aproxC)
        d = abs(gradosC-aC[0])
        dif.append(d)
    return graF, graC, aC,dif

from Problema1 import lista
def mos_lista(graF,graC,aC,dif):
    for F, C, E,D in zip(graF,graC. aC, dif):
        print '%f %f %f %f ' %(C,F,E,D)






