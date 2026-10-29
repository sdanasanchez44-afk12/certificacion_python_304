tabla = [
    ["nombre","edad","calificacion"],
    ["sdana",16,8.0],
    ["mery",15,9.0],
    ["leonel",15,9.0],
    ["emely",16,9.0],
    ["carlos",16,9.0],
    ["luis",16,9.0],
    ["carlos",16,9.0],
    ["brian",16,9.0],
    ["kimberly",15,9.0]
]
filas=len(tabla)
columnas=len(tabla)
nombre=len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == nombre:
            print(f"tabla encontrado en la posicion [{i}][{j}]")
