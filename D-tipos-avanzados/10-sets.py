# Los set tambien es conocido como grupo o CONJUNTO

#Los sets no almacenan valores repetidos y son NO ordenados
primero = {1, 1, 2, 3, 4}
print(primero)

primero.add(5)
primero.remove(1)
print(primero)

segundo = [3, 4, 5, 6]
segundo = set(segundo)
print(segundo)

#Lo interesante de los sets son las 'Operaciones de Conjunto'
print("Union", primero | segundo) #UNION
print("Interseccion", primero & segundo) #INTERSECCION
print("Diferencia", primero - segundo) #DIFFERENCIA se encarga de quitarle los elementos del segundo set al primero, una resta pues
print("Diferencia Cimetrica", primero ^ segundo) #Decolvera los elementos que NO esten dentro de ambos sets

#El detalle con los sets es que al ser no ordenados no podemos acceder a sus valores por indice:
#segundo[0] X
#Pero si podemos saber si el elemento se encuentra dentro del set:
if 5 in segundo:
    print("Si se encuentra dentro del set")