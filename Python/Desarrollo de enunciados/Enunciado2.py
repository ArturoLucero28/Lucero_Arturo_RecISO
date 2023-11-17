#Crear variables y asignar cadena el numero
numero=input("Introduce un número:")
cadena=str(numero)
#Se invierte
numero_invertido=cadena[::-1]
if cadena == numero_invertido:
    print("El numero es capicúa")
else:
    print("El numero no es capicúa")