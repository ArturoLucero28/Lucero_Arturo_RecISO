#Realiza un script en python que compare 3 numeros 
#insertados por el usuario en un bucle y nos de el mayor de los 3
#hasta que el usuario ingrese el 0 y finalize
def un_proceso():
    a, b, c = 0, 0, 0
    final = 1
    while final != 0:
        print("Escribe tres números distintos, por favor")
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        c = int(input("Ingrese el tercer número: "))
        if a > b:
            if a > c:
                print("a es el mayor:", a)
            else:
                print("c es el mayor:", c)
        else:
            if b > c:
                print("b es el mayor:", b)
            else:
                print("c es el mayor:", c)

        print("¿Quiere finalizar el proceso? Teclee 0 para salir.")
        final = int(input())

un_proceso()
