# and, or, not

gas = True
encendido = True
edad = 15

if gas and (encendido or edad > 17): #usamos () para señalar la gerarquia u orden de evaluación
    print("Puedes avanzar")
else:
    print("No puedes avanzar")


# OPERADORES DE CORTO CIRCUITO
# Python recorre las evaluaciones de izquierda a derecha -->, para el caso del operador and si no se 
# cumple la condicion de la izquierda se ignora la de la derecha, esto es util cuando existen evaluaciones 
# complejas o que requieren un mayor esfuerzo de computo y que se pueden ahorrar, para esto todos los operadores
# necesitan ser del mismo tipo:
if gas and encendido and edad > 17:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")

# Lo mismo pasa para las comparaciones con or, en este caso si se cumple minimo una de las condiciones se ejecuta, 
# por lo que el resto es ignorado ya que se acepto como valida la operación:
if gas or encendido or edad > 17:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")