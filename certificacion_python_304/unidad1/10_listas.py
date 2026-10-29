try:
    #Declara una lista 
    materias=["programacion"," filosofia","matematicas","ingles"]
    print(materias[0])
    materias.append("lengua y comunicacion")
    print(materias)
    materias[1]="Biologia"
    print(materias)
    materias.remove("programacion")
    print(materias)
except IndexError:
    print("indice incorrecto")
