def validar_texto(texto):
    while True:
        variable =input(texto)
        if variable != "":
            return variable.strip()
        else:
            print("Error: el texto no puede estar vacio")

def imprimir_menu():
    print("Menu\n\
1. Agregar usuario \n2. Listar usuarios \n3.Salir")
    

def ingresar_opcion():
    opcion = 0
    while True:
        try:
            opcion = int(input("ingrese una opcion: "))
            break
        except:
            print("la opcion debe ser un numero")
    return opcion


def agregar_usuario():
    nombre = validar_texto("ingrese un nombre: ")
    correo = validar_texto("ingrese un correo: ")
    usuario = {"nombre_usuario": nombre, "correo_usuario": correo}
    return usuario

