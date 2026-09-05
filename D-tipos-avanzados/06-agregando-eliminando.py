mascotas = ["Freddy", "Foxy", "Bonnie", "Chica", "Freddy"]

mascotas.insert(1, "Mangle") #EN insert es necesario usar el INDICE donde lo quieres agregar dentro de la lista
mascotas.append("Pupet")

mascotas.remove("Freddy") #Solamente elimina la primera instancia donde aparece el elemento
mascotas.pop() #Remueve el ultimo elemento de la lista
#mascotas.pop(1) Se puede usar pop con indice pero hay otra forma para eliminar por indice:
del mascotas[0] #Keyword del

mascotas.clear() #Para eliminar todos los elementos de la lista
print(mascotas)