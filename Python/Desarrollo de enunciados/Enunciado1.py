def enunciado1():
    #Creamos una variable en modo lista
    notas = []
    print("Ingresa las calificaciones de los 5 modulos:")
    #un bucle de rango 5 al pedirnos 5 modulos
    for i in range(5):
        modulo = float(input(f"Ingresa una nota: "))
        notas.append(modulo)
        i= i +1
    #Buscamos el mayor,menos y suma de la lista
    mayor = max(notas)
    menor = min(notas)
    suma = sum(notas)
    #Y para la media la conseguimos haciendo la suma de todos diviendolo entre todos los modulos
    media = suma / 5

    print(f"Calificacion mayor: {mayor}")
    print(f"Calificacion menor: {menor}")
    print(f"Media de calificaciones: {media}")

enunciado1()

