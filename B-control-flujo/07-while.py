comando = ""

while comando != "salir":
    print("Hola de nuevo")
    comando = input("$ ")
    comando = comando.strip().lower()
    if comando == "salir":
        print("Hasta luego!")
        break #agregar el break es adecuada para casos donde el bucle no tiene una condición de parada definido, como crear un 'while True:'