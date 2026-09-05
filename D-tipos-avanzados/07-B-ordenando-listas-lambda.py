usuarios2 = [["Freddy", 4], ["Bonnie", 1], ["Foxy", 3]]

#def ordena(elemento):
#    return elemento[1]

usuarios2.sort(key=lambda el:el[1]) 
#Al usar una funcion lambda/anonima indicamos el argumento que vamos a mandar y el valor de retorno (argumento:retorno)
#Si esa funcion no es usada en nunguna otra parte del código y es algo simple se puede usar una funcion lambda como esta
# #que hace lo mismo que la funcion ordena() original 
print(usuarios2)