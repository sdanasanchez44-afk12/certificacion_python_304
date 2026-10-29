#creando una tupla
coordenadas=(10.5,20.3,30.5)#tupla numerica
nombres=("sdana","ana","angel")#tupla de cadena de texto

for indice,coordenadas in  enumerate(coordenadas):
    print(f"[{indice}]coordenadas[{coordenadas}]")