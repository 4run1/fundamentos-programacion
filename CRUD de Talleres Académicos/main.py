from funciones import (
    agregar_videojuego,
    listar_videojuegos,
    buscar_videojuego,
    actualizar_videojuego,
    eliminar_videojuego
)

videojuegos = []
opcion = 0

while opcion != 6:
    print("\n===== SISTEMA CRUD VIDEOJUEGOS DUOC =====")
    print("1. Agregar videojuego")
    print("2. Listar videojuegos")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar una opción numérica.")
        continue

    if opcion == 1:
        agregar_videojuego(videojuegos)

    elif opcion == 2:
        listar_videojuegos(videojuegos)

    elif opcion == 3:
        buscar_videojuego(videojuegos)

    elif opcion == 4:
        actualizar_videojuego(videojuegos)

    elif opcion == 5:
        eliminar_videojuego(videojuegos)

    elif opcion == 6:
        print("Gracias por utilizar el sistema.")

    else:
        print("Opción inválida.")