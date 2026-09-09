"""
mostrar lista d eprecio y prodcuto -> ingresar opción y cantidad -> agregar producto a la lista de productos -> generar ticket(enlistar y sumar cantidades de producto -> imprimir producto Xcantidad $precio \n precio total) 
"""

def mostrar_productos(catalogo):
    count = 1
    for producto, precio in catalogo.items():
        print(f"0{count} {producto} - ${precio}")
        count += 1
    return

def agregar_producto(nombre, catalogo, lista):
    if nombre not in catalogo:
        print("Producto no encontrado!")
        return
    precio = catalogo[nombre]
    lista.append({"nombre": nombre, "precio": precio})
    print(lista)
    return

def generar_ticket(productos):
    contador_productos = {}
    total = 0

    for producto in productos:
        nombre = producto["nombre"]
        if nombre in contador_productos:
            contador_productos[nombre]["cantidad"] += 1
        else:
            contador_productos[nombre] = {"precio": producto["precio"], "cantidad": 1}

    print("-----------------")
    print("Ticket de compra:")
    print("-----------------")
    for nombre, info in contador_productos.items():
        cantidad = info["cantidad"]
        subtotal = cantidad * info["precio"]
        total += subtotal
        print(f"{nombre} X{cantidad} - ${subtotal}")
    print("-----------------")
    print("Total: $", total)
    print("-----------------")
    return

productos_disponibles = {
    "Manzana": 4.1, 
    "Naranja": 6.2,
    "Leche": 10.3,
    "Detergente": 20.4,
    "Cereal": 15.5,
}
lista_productos = []
print("Selecciona un producto por INDICE")
mostrar_productos(productos_disponibles)
opcion = " "
while True:
    opcion = input().strip().capitalize()
    if opcion == "":
        break
    agregar_producto(opcion, productos_disponibles, lista_productos)
generar_ticket(lista_productos)