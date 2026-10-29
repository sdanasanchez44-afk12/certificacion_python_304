try:
    alumnos=["america","leonel","brian","michel","carlitos"]
    calificaciones=["8.9","9.0","7.9","6.0","9.5"]
    print("alumno:",alumnos[2],"calificacion:",calificaciones[2])
    print("alumno:",alumnos[4],"calificacion:",calificaciones[4])

except IndexError:
    print("no se encontro ese alumno y/o la calificacion")