import utils as u

while True:
    u.imprimir_menu()
    opcion = u.ingresar_opcion()

    if opcion == 1:
        u.agregar_usuario()
    elif opcion == 2:
        u.listar_usuario()
    elif opcion == 3:
        print("Gracias por usar el sistema")
        break
    else:
        print("Error: opcion no valida")