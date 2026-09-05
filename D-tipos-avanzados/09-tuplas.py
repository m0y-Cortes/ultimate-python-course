#Las tuplas son "lo mismo" que las listas, la unica diferencia es que son INALTERABLES
numeros = (1, 2, 3)
print(numeros)

#podemos concatenar las tuplas
numeros += (4, 5, 6)
print(numeros)

punto = tuple([1, 2]) #la funcion tuple() recibe CUALQUIER OBJETO ITERABLE transformandolo en una tupla

menosNUmeros = numeros[:2] #podemos seccionar una tupla hacia otra variable que guarde la nueva tupla seccionada
print(menosNUmeros)

primero, segundo, *otros = numeros #Y podemos desempaquetar las tuplas dentro de otras variables
print(primero, segundo, otros)

listaNumeros = list(numeros)
listaNumeros[0] = "Freddy"
print(listaNumeros)
#Por lo que podemos seccionar y filtrar datos de la tupla siempre y cuando sea dentro de otra variable y sin modificar la tupla