nombre = "Moises"
apellido = "Cortes"
#Esta es una forma de concatenar strings dentro de una variable, sin embargo es la forma fea
nombre_completo = nombre + " " + apellido
#La forma adecuada de concatenar strings es usando el operador de formateo
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)
#También podemos usar otros operadores dentro del operador de formateo
nombre_completo = f"{nombre[0]} {2 + 3}"
print(nombre_completo)