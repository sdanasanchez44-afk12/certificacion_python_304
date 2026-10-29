#Ciclo externo para el nunero de la base de la tabla
for i in range(1,4):
    print(f"---tabla del{i}---")
    #Ciclo interno nos multiplica la base(i) por el numero(j)
    for j in range (1,11):
        print(f"{i} x {j} =  {i*j}")
    print(f"AQUI TERMINA LA TABLA DEL {i}")