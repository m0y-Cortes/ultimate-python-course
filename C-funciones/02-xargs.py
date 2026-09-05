#para casos en los que no sabemos cuantos argumentos vamos a recibir usamos un Iterable como parametro que guarda todos los argumentos
def suma(*numeros): 
    resultado = 0
    for numero in numeros: #Este Iterable lo podemos recorrer con un for para obtener cada uno de los argumentos
        resultado += numero
    print(resultado)

suma(2, 5, 7)
suma(2, 5)
suma(2, 5, 45, 32)
