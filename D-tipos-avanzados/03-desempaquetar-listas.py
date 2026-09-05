numeros = [0, 1, 2, 3, 4, 5]

#cero, uno, dos, tres, cuatro, cinco = numeros
#print(cero, uno, dos, tres, cuatro, cinco)

#No podemos asignar solo o algunos de los valores de una lista usando el desempaquetado, a menos de que agreguemos una variable iterativa
primero, segundo, *otros, ultimo = numeros
print(primero, segundo, otros, ultimo)