'''filas = int(input ("Introduzca el numero de filas de sus matrices: "))
columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))

matriz1 = []
matriz2 = []
matriz3 = []
for i in range (filas):
	matriz1.append( [0] * columnas)
	matriz2.append( [0] * columnas)
	matriz3.append( [0] * columnas)

print 'Ingrese su Matriz 1'
for i in range(filas):
		for j in range(columnas):
			matriz1[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))
print 'Ingrese su Matriz 2'
for i in range(filas):
	for j in range(columnas):
			matriz2[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))

for i in range(filas):
	for j in range(columnas):
			matriz3[i][j] += matriz1[i][j] + matriz2[i][j]
print ('Su matriz resultante es')
print matriz3
'''


filas = int(input ("Introduzca el numero de filas de sus matrices: "))
columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))

matriz1 = []
matriz2 = []

for i in range (filas):
	matriz1.append( [0] * columnas)
	matriz2.append( [0] * columnas)
print 'Ingrese su Matriz 1'
for i in range(filas):
    for j in range(columnas):
        matriz1[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))
print matriz1

for i in range(len(matriz1)):
    print ("Suma de la fila ",i + 1, "=", sum(matriz1[i]))

for i in range(len(matriz1)):
    suma = 0
    for j in range(len(matriz1[0])):
        suma = suma + matriz1[j][i]
    print ("Suma de la columna ",i + 1, "=", suma)

'''
print ('Su matriz resultante es')
print matriz2
	'''
