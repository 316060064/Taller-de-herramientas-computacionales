def L_ig(m,n):
    if m == n:
        print ("Son iguales")
    else:
        print("No, tienen por lo menos un elemento distinto")




        lista1=["paco","pepe","luis"]
lista2=["diego","mari","luis"]
comparacion = []
 
for item in lista1:
  if item in lista2:
    comparacion.append(item)
 
if len(comparacion) > 0:
  print 'Ambas listas contienen estos elementos'
  for item in comparacion: print '%s' % item
else:
  print 'No existe ningun elemento igual en las listas'
