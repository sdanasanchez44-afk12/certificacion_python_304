#creando un diccionario
persona={
    "nombre":"sdana",
    "edad":16,
    "profecio":"programacion",
    "estudiante":False
}
print(persona)
#Accediendo a un valor en especifico 
print(persona["edad"])
#Sed puede usar el metodo get()
#Es util porque marca error si el valor no xiste 
print(persona.get("profecion"))
#modificar un valor existente
persona["Edad"]=18
print(persona["Edad"])