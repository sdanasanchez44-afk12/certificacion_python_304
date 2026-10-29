carrito=[]
n_productos=int(input("ingresa  el numero de productos"))
for i in range(n_productos):
    producto=input("ingresa el producto a tu carrito")
    carrito.append(producto)
print("lista creada correctamente")
print(f"tu carrito contine{carrito}")
carrito[0]="barritas"
print(f"tu carrito contiene{carrito}")
print(carrito[0])
print(carrito[1])
print(carrito)