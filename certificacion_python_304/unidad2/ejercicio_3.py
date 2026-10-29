#creando una matriz
letras=[
    ["a","b","c","d"],# filas 0
    ["e","f","g","h"],# filas 1
    ["i"."j","K","l"],# filas 2
    ["m","n","ñ","o"]# filas 3
    ["m","n","ñ"]# filas 4
]
#Obteniendo el letras de filas 
#filas= len(letras)#filas=4
#Obteniendo el letras de columnas
#columnas=len(letras[0])
#Ciclo externo para los indices de las filas(i)
for i in range(0,4):
    #ciclo interno para  los indices de las columnas(j)
    for j in range(0,4):
        print(f"[{i}] [{j}] = {letras[i][j]}")