def hola(nombre, apellido = "Feliz"): #Podemos agregar valores por default a los parametros de las funciones por si no se envía un valor
    print(f"Hola {nombre} {apellido}\n")

hola("Adrian", "Cortes")

hola("Adrian")

hola(apellido = "Saldler", nombre = "Adam") #es NECESARIO especificar TODOS cual argumentos es cual aunque solo se cambie el orden de uno

