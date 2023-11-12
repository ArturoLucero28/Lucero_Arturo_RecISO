#Realiza un script en python que compare 3 números 
#insertados por el usuario, en un bucle donde nos de 
#el mayor de los 3 hasta que el usuario ingrese el 0 y finalize

def un_proceso():
    a, b, c, final = 0, 0, 0, 1

    while final != 0:
        print("Escribe tres números distintos")
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        c = int(input("Ingrese el tercer numero: "))
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

        print("Teclee 0 para salir o cualquiera para continuar .")
        final = int(input())

un_proceso()
