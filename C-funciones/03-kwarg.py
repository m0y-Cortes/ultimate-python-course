#Key Word Arguments
def get_product(**datos):
    #print(datos) #si imprimimos datos nos arroja un DICCIONARIO
    print(datos["name"], datos["id"])

get_product(id = "11",
            name = "Samsung",
            desc = "Telefono marva samsung") #Al usar kwarg NECESITAS especificar el nombre del argumento que estas pasando a la funcion