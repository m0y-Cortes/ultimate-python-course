mascotas = ["Freddy", "Foxy", "Bonnie", "Chica"]

for mascota in enumerate(mascotas): #enumerate nos devuelve cada elemento de la lista en forma de tupla
    print(mascota, mascota[0], mascota[1]) #esto nos permite obtener el indice de cada elemento
    
#O podemos usar el mismo principio de desempaquetar con las tuplas permitiendonos guardar los elementos por indice y valor en variables separadas
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
