i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # minimum field
  #imprime el minimo entero

print '"%5d"' % i      # field of width 5 characters
  #imprime con 5 unidades de enteros

print '"%05d"' % i     # pad with zeros
   #imprime con 5 unidades rellenando los demas con ceros

print '"%g"' % r       # r is big number so this is scientific notation
  #Imprime el numero mas grande proximo en formato cientifico

print '"%G"' % r       # E in the exponent
 # Imprime el numero mas grande proximo en formato cientifico con E mayuscula


print '"%e"' % r       # compact scientific notation
  #imprime en notacion cientifica con el numero compacto
  
print '"%E"' % r       # compact scientific notation
   #imprime en notacion cientifica con el numero compacto con E mayuscula

print '"%20.2E"' % r   # 2 decimals, field of width 20
   #imprime usando solamente 20 unidades y 2 decimales

print '"%30g"' % r     # field of width 30 (right-adjusted)
   #imprime con 30 unidades ajustando a la derecha 


print '"%-30g"' % r    # left-adjust number
  #imprime con 30 unidades ajustando a la izquierda


print '"%-30.4g"' % r  # 3 decimals
  #Recorre el punto decimal hasta la tercera cifra decimal

print '%s' % i   # can convert i to string automatically
  # %s convierte en una cadena automaticamente

print '%s' % r
  # %s convierte en una cadena automaticamente

# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % (5.1, 346, 5.1/100*346)

  # para colocar el simbolo de porcentaje a una cifra se coloca %%


