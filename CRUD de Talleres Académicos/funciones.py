def agregar_videojuego(videojuegos):
    print("\n--- Agregar videojuego ---")
    try:
        id_juego = int(input("Ingrese ID del videojuego: "))
    except ValueError:
        print("El ID debe ser numérico.")
        return
    # Validar que el ID no se repita
    for juego in videojuegos:
        if juego["id"] == id_juego:
            print("Ya existe un videojuego con ese ID.")
            return
    nombre = input("Ingrese nombre del videojuego: ").strip()
    genero = input("Ingrese género del videojuego: ").strip()
    if nombre == "" or genero == "":
        print("El nombre y el género no pueden quedar vacíos.")
        return
    try:
        precio = int(input("Ingrese precio del videojuego: "))
    except ValueError:
        print("El precio debe ser numérico.")
        return

    if precio <= 0:
        print("El precio debe ser mayor a cero.")
        return

    videojuego = {
    "id": id_juego,
    "nombre": nombre,
    "genero": genero,
    "precio": precio
    }
    videojuegos.append(videojuego)
    print("Videojuego agregado correctamente.")

def listar_videojuegos(videojuegos):
    print("\n--- Lista de videojuegos ---")
    if len(videojuegos) == 0:
        print("No hay videojuegos registrados.")
        return

    for juego in videojuegos:
        print(f"ID: {juego['id']}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Género: {juego['genero']}")
        print(f"Precio: ${juego['precio']}")
        print("----------------------------")

def buscar_videojuego(videojuegos):
    print("\n--- Buscar videojuego ---")

    try:
        id_buscar = int(input("Ingrese ID a buscar: "))
    except ValueError:
        print("El ID debe ser numérico.")
        return

    for juego in videojuegos:
        if juego["id"] == id_buscar:
            print("Videojuego encontrado:")
            print(f"Nombre: {juego['nombre']}")
            print(f"Género: {juego['genero']}")
            print(f"Precio: ${juego['precio']}")
            return

    print("No se encontró un videojuego con ese ID.")


def actualizar_videojuego(videojuegos):
    print("\n--- Actualizar videojuego ---")

    try:
        id_buscar = int(input("Ingrese ID a actualizar: "))
    except ValueError:
        print("El ID debe ser numérico.")
        return

    for juego in videojuegos:
        if juego["id"] == id_buscar:
            nuevo_nombre = input("Ingrese nuevo nombre: ").strip()
            nuevo_genero = input("Ingrese nuevo género: ").strip()

            if nuevo_nombre == "" or nuevo_genero == "":
                print("Los datos no pueden quedar vacíos.")
                return

            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
            except ValueError:
                print("El precio debe ser numérico.")
                return

            if nuevo_precio <= 0:
                print("El precio debe ser mayor a cero.")
                return

            juego["nombre"] = nuevo_nombre
            juego["genero"] = nuevo_genero
            juego["precio"] = nuevo_precio

            print("Videojuego actualizado correctamente.")
            return

    print("No se encontró un videojuego con ese ID.")

def eliminar_videojuego(videojuegos):
    print("\n--- Eliminar videojuego ---")
    try:
        id_buscar = int(input("Ingrese ID a eliminar: "))
    except ValueError:
        print("El ID debe ser numérico.")
        return
    for juego in videojuegos:
        if juego["id"] == id_buscar:
            videojuegos.remove(juego)
            print("Videojuego eliminado correctamente.")
        return
    print("No se encontró un videojuego con ese ID.")
