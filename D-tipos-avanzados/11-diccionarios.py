#Los diccionarios usan un sistema de key-value para guardar sus valores
punto = { 
    "x": 25,      
    "y": 50
}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)

#Los diccionarios cuentan con la funcion get() que si no encuentra
#el la llave mencionada solo devuelve un None en lugar de dar un error:
print(punto.get("x"))       # = 25
print(punto.get("lala", 97))    # = None (Y podemos pasar un valor por defecto = 97)

for valor in punto.items():
    print(valor)

usuarios = [
    {"id": 1, "nombre": "Freddy"},
    {"id": 2, "nombre": "Foxy"},
    {"id": 3, "nombre": "Bonnie"}
]
for usuario in usuarios:
    print(usuario["nombre"])