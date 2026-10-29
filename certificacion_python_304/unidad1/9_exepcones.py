try:
    numero1=float(input("ingresa el primer numero"))
    numero2=flaot(input("ingrsa el segundo numero"))
    resultado=numero1/numero2
except ValueError:
    print("solo intrdouec numeros")
except ZeroDivisionError:
    print("Division entre cero")
else:
    print("El resultado es",resultado)
finally:
    print("programa finalizado")

