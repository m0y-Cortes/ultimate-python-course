def es_palindromo(palabra):
    palindromo = ""
    palabra = palabra.lower().strip()
    for letra in palabra:
        if letra != " ":
            palindromo += letra

    tamaño = len(palindromo)
    for i in range(tamaño):
        print(palindromo[i])
        if palindromo[i] != palindromo[-(i+1)]:
            print("No es un palindromo")
            return
    print("Es un palindromo")

palabra_input = input()
es_palindromo(palabra_input)
#LO LOGRASTE AL PRIMER INTENTO, STAND PROUD YOU CAN CODE
#Pero existen pequeñas cosas que puedo mejorar:
#1- Usar el Single Responsability Principle, cada funcion se debe de encargar de una sola cosa
#2- Se recorre toda la palabra al momento de revisar si es un palindromo, pero mi solucion solo necesita recorrer la mitad de la palabra para saber si es o no
#3- No regresa nada, solo imprimre si es palindromo o no, pero si quiero usar esa funcion dentro de otra funcion que cuente los palindromos no funcionaría