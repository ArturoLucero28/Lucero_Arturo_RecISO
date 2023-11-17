#pedir numero
numero=int(input("Introduce un numero del 1 al 50"))
if 0 < numero < 50:
    #usamos funciones prestablecidas
    binario= bin(numero)
    octal= oct(numero)
    hexadecimal=hex(numero)
    print(f"Representacion binaria: {binario}")
    print(f"Representacion octal: {octal}")
    print(f"Representacion hexadecimal: {hexadecimal}")    
else:
    print("Ese numero no se puede")    