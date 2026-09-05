animal = "Cerdo fELIZ"
print(animal.upper()) #Convierte a upper case
print(animal.lower()) #Convierte a lower case
print(animal.capitalize())
print(animal.title())
print(animal.strip()) #Elimina los espacios en blanco de hasta la izquierda y derecha de los strings, no los que estan entre el string
print(animal.lstrip()) #Solo elimina los espacios en blanco de la izquierda (left)
print(animal.rstrip()) #Solo elimina los espacios en blanco de la derecha (right)
print(animal.find("do")) #Encuentra el indice donde estan los caracteres a buscar
print(animal.replace("fELIZ", "Triste")) #Case sensitive
print("Cerdo" in animal) #Se puede usar su variable 'not in' para saber si NO esta dentro del string

