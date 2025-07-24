try:
    Clientes = {}

    totalclientes = int(input("Ingrese el total de Clientes a Registrar:  "))
    q = 1
    for i in range(totalclientes):
        print(f"\nCliente # {q}")
        id = int(input("Introduce el código del cliente:  "))
        Clientes[id] = {}
        Clientes[id]["name"] = input("Introduce el nombre del cliente:  ")

        Clientes[id]["destinos"] = {}

        while True:
            totaldestinos = int(input("Ingrese cuantos destinos visitara el cliente:   "))
            i = 1
            if totaldestinos > 0 and totaldestinos < 6:
                for destino in range(totaldestinos):
                    d = input(f"Introduzca el destino # {i}:   ")
                    i += 1
                    Clientes[id]["destinos"][totaldestinos] = {
                        "viajes": d,
                    }
                break

            else:
                print("El cliente debe de tener al menos un destino y menos de 5 destinos distintos   ")
        q = +1

    c = 1
    for id, dato in Clientes.items():
        print(f"\nCliente # {c}")
        print(f"ID: {id}")
        print(f"Nombre: {dato["name"]}")
        print(f"Destinos:   ")
        c += 1
        a = 1
        for totaldestinos, data in dato["destinos"].items():
            print(f"Destino #{a}: {data["viajes"]}")
            a = +1

    total = 0
    for id, data in Clientes.items():
        for totaldestinos, data in data["destinos"].items():
            total += totaldestinos

    print(f"Total de destinos: {total}")
    #print(f"\nTotal de viajes (destinos) de todos los clientes: {totaltrips(totalclientes)}")

except:
    print("Hubo un Error")
