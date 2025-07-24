Clientes = {}

id = int(input("Introduce el código del cliente: "))
Clientes[id] = {}
Clientes[id]["name"] = input("Introduce el nombre del cliente: ")

Clientes[id]["destinos"] = {}

while True:
    totaldestinos = int(input("Ingrese cuantos destinos visitara el cliente"))
    i = 1
    if totaldestinos > 0 and totaldestinos < 6:
        d = input(f"Introduzca el destino # {i}: ")
        i += 1
        Clientes[id]["destinos"] = {
            "viajes": d,
        }
    else:
        print("El cliente debe de tener al menos un destino y menos de 5 destinos distintos")

