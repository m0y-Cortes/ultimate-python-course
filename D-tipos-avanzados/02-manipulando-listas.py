mascotas = ["Foxy", "Freddy", "Chica", "Bonnie"]
print(mascotas[0])

mascotas[0] = "Mangle"
print(mascotas)

print(mascotas[:3])
print(mascotas[2:])
print(mascotas[-1])
print(mascotas[::2])

#Un ejemplo para usar los saltos es sacar los numeros pares e impares de una misma lista:
numeros = list(range(1, 21))
print(numeros[1::2])
print(numeros[::2])