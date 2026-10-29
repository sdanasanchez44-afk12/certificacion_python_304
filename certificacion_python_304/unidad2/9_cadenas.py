cadena1='hola'
cadena2='mundo'
multilinia="""esto es una cadenada
de variables lineas"""
print(cadena1 + cadena2)#print(f"{cadena1}")
#cadenas y repeticion
eco="ja"*3
print(eco)
#cambiar una cadena de minuscula a mayusculas
tu_nombre='sdana'
print(tu_nombre.upper())
#cambiar una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#remplazar texto en una cadena
frase="me gusta programacion"
print(frase.replace("programacion","filosofia"))
#formatos de cadenas (f-string)
edad=16
nombre="sdana"
mensaje=f"hola, me llamo {nombre} y tengo {edad} años"
print(mensaje)
#contar los caracteres de una cadena
texto= "¡¡¡felicidades por una continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(texto,cantidad_caracteres)
#comprobr si un texto contiene una palabra
oracion="Aprender python es divertido"
if "java" in oracion:
    print("encontrado")
else:
 print("No esta")
#validar contenido de una cadena
nlista="sdana"
print(nlista.isalpha())
print(nlista.isdigit()) 