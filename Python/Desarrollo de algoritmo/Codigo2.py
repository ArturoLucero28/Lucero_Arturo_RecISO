#Realizar un script en python que pida al usuario si quiere o no realizar el programa
#y si lo ejecuta pida un numero, con ese numero el programa le dirá si es divisible entre 2,
#y repetiremos el proceso hasta en 10 ocasiones
def un_proceso():

    pr = input("Desea ejecutar el programa (s/n): ")
    
    if pr.lower() == "s":
        c = 0
        while c < 10:
            a = int(input("Ingrese un número: "))
            c += 1
            r = a % 2
            if r == 0:
                print(f"{a} seleccionado")
            else:
                print(f"{a} No seleccionado")
            print(r)

    print("YA TERMINAMOS")

un_proceso()
