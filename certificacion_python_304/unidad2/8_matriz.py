#creando una matriz
numero=[
    [1,2,3],# filas 0
    [2,3,4],# filas 1
    [5,6,7],# filas 2
    [7,8,9]
]
#Obteniendo el numero de filas 
#filas= len(numero)#filas=3
#Obteniendo el numero decolumnas
#columnas=len(numero[0])
#Ciclo externo para los indices de las filas(i)
for i in range(0,3):
    #ciclo interno para  los indices de las columnas(j)
    for j in range(0,3):
        print(f"[{i}] [{j}] = {numero[i][j]}")