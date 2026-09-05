saludo = "Hola global"
#Las variables que estan en la parte superios se les conoce como 'globales'
#y no se recomienda usar variables globales ya que es una mala practica
#relacionada con que puede ser mal interpretada como otra variable usada
#en una funcion pero si se le asigna un tipo de dato incorrecto la aplicacion
#puede dejar de funcionar

def saludar():
    saludo = "Hola mundo"
    print(saludo)

def saludar_global():
    global saludo   #Si fuera completamente necesario usar una variable global dentro de una funcion se usa la keyword 'global'
    saludo = 23
    #En este caso se demuestra el porque es peligroso usar variables globales ya que 
    #al cambiarse el tipo de la variable y esto puede romper futuras llamadas a la funcion
    print(saludo)

def saluda_chanchito():
    saludo = "Hola chanchito"
    print(saludo)

print(saludo)
#Aqui manda error (si la variable global saludo esta comentada)
#ya que la variable 'saludo' solo existe dentro de sus respectivas
#funciones y no puede ser accedida desde fuera de la funcion