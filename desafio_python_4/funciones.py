"""
Actividad DUOC UC - Debugging con Python
Archivo de funciones: funciones.py

Este archivo contiene las funciones del CRUD corregidas.
"""
def evaluar_rut_unico(rut, estudiantes):
    for estudiante in estudiantes:
        if estudiante["rut"] == rut:
            return False
    return True


def evaluar_rut(rut):
    # 1. Validamos el largo total de la cadena de texto (entre 7 y 9 caracteres)
    if not (7 <= len(rut) <= 9):
        print("Error: El RUT debe tener entre 7 y 9 caracteres en total.")
        return False
        
    # 2. Separamos cuerpo y dígito verificador para validar su contenido
    cuerpo = rut[:-1]
    dv = rut[-1].upper()
    
    if not cuerpo.isdigit():
        print("Error: El cuerpo del RUT debe contener solo números.")
        return False
        
    if dv not in "0123456789K":
        print("Error: El dígito verificador debe ser un número o la letra K.")
        return False
        
    return True # El RUT es válido en estructura


def agregar_estudiante(estudiantes):
    print("\n--- Agregar estudiante ---")
    while True:
        rut_input = input("Ingrese RUT de corrido (ej: 12345678K): ").strip()

        if evaluar_rut(rut_input):
            if evaluar_rut_unico(rut_input,estudiantes):
                rut = rut_input.upper()
                break
            else:
                print("Error: el Rut ya existe")

    nombre = input("Ingrese nombre: ")
    carrera = input("Ingrese carrera: ")
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            break
        except ValueError:
            print("Error: debe ingresar datos numéricos")
    
    estudiante = {
        "rut": rut,
        "nombre": nombre,
        "carrera": carrera,
        "edad": edad
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente")


def listar_estudiantes(estudiantes):
    print("\n--- Lista de estudiantes ---")
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        for i in range(len(estudiantes)):
            print(f"RUT: {estudiantes[i]['rut']}")
            print(f"Nombre: {estudiantes[i]['nombre']}")
            print(f"Carrera: {estudiantes[i]['carrera']}")
            print(f"Edad: {estudiantes[i]['edad']}")
            print("------------------------")


def buscar_estudiante(estudiantes, rut):
    print("\n--- Buscar estudiante ---")
    rut_buscado = str(rut).upper()
    for estudiante in estudiantes:
        if str(estudiante["rut"]).upper() == rut_buscado:
            print("Estudiante encontrado:")
            print(f"RUT: {estudiante['rut']}")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Carrera: {estudiante['carrera']}")
            print(f"Edad: {estudiante['edad']}")
            return 
            
    print("No se encontró el estudiante")


def actualizar_estudiante(estudiantes, rut):
    print("\n--- Actualizar estudiante ---")
    rut_buscado = str(rut).upper()
    for estudiante in estudiantes:
        if str(estudiante["rut"]).upper() == rut_buscado:
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_carrera = input("Ingrese nueva carrera: ")
            while True:
                try:
                    nueva_edad = int(input("Ingrese nueva edad: "))
                    break
                except ValueError:
                    print("Error: el dato debe ser numérico")

            estudiante["nombre"] = nuevo_nombre
            estudiante["carrera"] = nueva_carrera
            estudiante["edad"] = nueva_edad

            print("Estudiante actualizado correctamente")
            return

    print("No se encontró el estudiante")


def eliminar_estudiante(estudiantes, rut):
    print("\n--- Eliminar estudiante ---")
    rut_buscado = str(rut).upper()
    for estudiante in estudiantes:
        if str(estudiante["rut"]).upper() == rut_buscado:
            while True:
                confirmar = input("Confirmar eliminacion? (S/N)").strip().upper()
                if confirmar == "S":
                    estudiantes.remove(estudiante)
                    print("Estudiante eliminado correctamente")
                    return
                elif confirmar == "N":
                    print("Eliminacion cancelada")
                    break
                else:
                    print("Error: dato invalido (S/N)")


    print("No se encontró el estudiante") 
