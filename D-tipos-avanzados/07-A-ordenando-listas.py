numeros = [2, 8, 5, 7, 8, 3, 10]

#numeros.sort(reverse=True)
numeros2 = sorted(numeros) #sorted() crea un nuevo elemento aparte al que esta ordenando
print(numeros)
print(numeros2)

usuarios = [[4, "Freddy"], [1, "Bonnie"], [3, "Foxy"]]
usuarios.sort()
print(usuarios)

#Pero si los elementos no tienen su indice como primero valor dentro de sus listas sort() las ordenara de otra manera, en este caso alfabeticamente
usuarios2 = [["Freddy", 4], ["Bonnie", 1], ["Foxy", 3]]

#Entonces creamos una funcion que devuelva el elemento en donde este el indice
def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena) #sort() no toma argumentos posicionales a no ser de que se indiquen con 'key='
print(usuarios2)
#Pero la forma de arriba no es la mejor 