"""
Actividad DUOC UC - Debugging con Python
Archivo principal: main.py CORREGIDO
"""

from funciones import (
    agregar_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante
)

estudiantes = []

def mostrar_menu():
    print("\n===== SISTEMA CRUD ESTUDIANTES DUOC UC =====")
    print("1. Agregar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Salir")

opcion = 0

while opcion != 6:
    mostrar_menu()

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: opción inválida. Ingrese solo números.")
        continue  # Regresa al inicio del ciclo sin evaluar los 'if'
        
    if opcion == 1:
        agregar_estudiante(estudiantes)

    elif opcion == 2:
        listar_estudiantes(estudiantes)

    elif opcion == 3:
        try:
            rut = input("Ingrese RUT del estudiante a buscar (solo números): ")
            buscar_estudiante(estudiantes, rut)
        except ValueError:
            print("Error: El RUT debe ser un dato numérico.")

    elif opcion == 4:
        try:
            rut = input("Ingrese RUT del estudiante a actualizar (solo números): ")
            actualizar_estudiante(estudiantes, rut)
        except ValueError:
            print("Error: El RUT debe ser un dato numérico.")

    elif opcion == 5:
        try:
            rut = input("Ingrese RUT del estudiante a eliminar (solo números): ")
            eliminar_estudiante(estudiantes, rut)
        except ValueError:
            print("Error: El RUT debe ser un dato numérico.")

    elif opcion == 6:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida. Ingrese un número del 1 al 6.")
