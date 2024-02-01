cantidad = 0
#bucle que tiene que cumplirse que el resto de cantidad entre 5 sea diferente que 0 o cantidad este entre 0 y 3000
while cantidad % 5 != 0 or cantidad <= 0 or cantidad > 3000:
    cantidad = int(input("Introduce una cantidad de dinero (múltiplo de 5 y como máximo 3000): "))
#realizamos los calculos
billetes_100 = cantidad // 100
cantidad %= 100
billetes_50 = cantidad // 50
cantidad %= 50
billetes_20 = cantidad // 20
cantidad %= 20
billetes_10 = cantidad // 10
cantidad %= 10
billetes_5 = cantidad // 5
#Y los mostramos en pantalla 
print("La cantidad de ${}:".format(cantidad))
print("- {} billetes de 100".format(billetes_100))
print("- {} billetes de 50".format(billetes_50))
print("- {} billetes de 20".format(billetes_20))
print("- {} billetes de 10".format(billetes_10))
print("- {} billetes de 5".format(billetes_5))
