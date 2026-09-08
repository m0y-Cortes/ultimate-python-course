lista1 = [1, 2, 3, 4]
print(lista1) #Imprime la lista como tal
print(*lista1) #Imprime cada elemento de unobjeto iterable
lista2 = [5, 6]
combinada = ["Hola", *lista1, "Mundo", *lista2] #Deja de ser una lista de listas ya que pasas los elementos desempaquetados y no listas
#print(combinada)
#------------------------------------------------------------------------------------------------------------------------------
punto1 = {"x": 92, "y": "Hola"}
punto2 = {"y": 13}

nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}
#La forma en la que funciona es que va leyendo de izquierda a derecha los valores y si a la derecha se vuelve a asignar un valor a una
#llave que ya existia ese valor se sobreescribe.
print(nuevoPunto)
#Entonces en este caso se imprime: lista1(con "y" sobreescrito) -> "lala" -> punto2 no porque solo reescribio la llave que ya existia en punto1 -> "z"