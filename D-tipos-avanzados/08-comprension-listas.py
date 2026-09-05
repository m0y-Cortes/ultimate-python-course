usuarios = [
    ["Freddy", 4], 
    ["Bonnie", 1],
    ["Foxy", 3]
]

# nombres = []
# for usuario in usuarios:
#   nombres.append(usuario[0])
# print(nombres)

#La sintaxys para TRANSFORMAR una lista en otra de forma mas elegante es:
#nombre_lista = [expresion for item in items]
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

#Y tambien funciona si queremos FILTRAR
nombres2 = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres2)

#Y obviamente podemos hacer las dos al mismo tiempo:
nombres3 = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres3)

#-----------------------------------
#Pero puede que en otros casos me pueda encontrar con casos donde se usan las funciones de MAP y FILTER para hacer estas dos operaciones

nombres4 = list(map(lambda usuario:usuario[0], usuarios))
print(nombres4)

nombres5 = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres5)

nombres6 = list(map(lambda usuario: usuario[0], filter(lambda usuario: usuario[1] > 2, usuarios)))
#como filter() regresa un objeto ITERABLE puedo usar ese objeto como el objeto que itera map()
print(nombres6)