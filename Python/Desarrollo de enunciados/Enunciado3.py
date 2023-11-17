#Introducimos las ciudades en una lista
ciudades = {"Mérida","Montijo","Guadiana","Caceres","Puebla de la calzada","Lácara","Barbaño","Valdelacalzada","La Roca","Calamonte"}
ciudad = input("Introduce el nombre de la ciudad")
#para que de igual como lo ingresa el usurio hacemos lower
ciudad=ciudad.lower()
#verificamos
if ciudad in ciudades
    print("La ciudad está")
    else
    print("La ciudad no está")