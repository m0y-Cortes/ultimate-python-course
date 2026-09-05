"""
Ejercicio 1: Verificación de Tweets 
Descripción.
Este programa solicita al usuario que ingrese un tweet y verifica si cumple con el límite de 20 caracteres. 
• Si el tweet excede los 20 caracteres, muestra un mensaje indicando que se ha sobrepasado el límite. 
• Si el tweet tiene 20 caracteres o menos, indica que el tweet ha sido publicado. 
• No se aceptan tweets vacíos. Variables.• tweet (str): El tweet ingresado por el usuario. 
Pruebas.
1. Entrada: "Hola, este es un tweet" (20 caracteres). Salida: "Su tweet ha sido publicado". 
2. Entrada: "Hola, este es un tweet muy largo" (más de 20 caracteres). Salida: "Ha sobrepasado el límite de su publicación". 
3. Entrada: "" (vacío). Salida: "No se puede publicar un tweet vacío”. 
"""
tweet = input("Crea un nuevo tweet: \n")
len_tweet = 0
for chara in tweet:
    if chara != " ":
        len_tweet +=1
if len_tweet > 20:
    print("Ha sobrepasado el límite de su publicación")
elif len_tweet == 0:
    print("No se puede publicar un tweet vacío")
else:
    print("Su tweet ha sido publicado")

