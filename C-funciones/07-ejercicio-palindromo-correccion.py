#LO LOGRASTE AL PRIMER INTENTO, STAND PROUD YOU CAN CODE
#Pero existen pequeñas cosas que puedo mejorar:
#1- Usar el Single Responsability Principle, cada funcion se debe de encargar de una sola cosa
#2- Se recorre toda la palabra al momento de revisar si es un palindromo, pero mi solucion solo necesita recorrer la mitad de la palabra para saber si es o no
#3- No regresa nada, solo imprimre si es palindromo o no, pero si quiero usar esa funcion dentro de otra funcion que cuente los palindromos no funcionaría
def quitar_espacios(palabra):
    nueva_palabra = ""
    palabra = palabra.lower().strip()
    for letra in palabra:
        if letra != " ":
            nueva_palabra += letra
    return nueva_palabra

def es_palindromo(palabra):
    nueva_palabra = quitar_espacios(palabra)
    tamaño = len(nueva_palabra)
    for i in range(round(tamaño/2)):
        #print(nueva_palabra[i])
        if nueva_palabra[i] != nueva_palabra[-(i+1)]:
            return False
    return True

palabra_input = input()
print(palabra_input, "es palindromo?" ,es_palindromo(palabra_input))


#Y recuerda que hay otra solución para invertir la lectura de la palabra: 
#creando una nueva variable que almacene la palabra invertida concatenando de manera inversa los caracteres

def invertir_palabra(palabra):
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida #De esta forma se concatena de manera inversa