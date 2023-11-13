import funciones

#numero_puertas = 2
#estado_puertas = 0: cerrado y 1: abierto

def access():
    while True:
        dni = input('Ingrese DNI: ') # Esto puede ser reemplazado por un sensor

        if not funciones.search(dni):
            print("Usted no se encuentra registrado. Ingrese un DNI válido.")
        else:
            reserva = funciones.dni_read(dni)

            if reserva == [0, 0] or reserva == [1, 0]:
                print("No tiene una reserva. ¿Desea realizar?")
                accion = input('Ingrese "s" para sí o "n" para no: ')
                if accion == 's':
                    print(".")
                    disponible = funciones.disponibilidad_now()
                    if disponible[0] == 1:
                        print("--")
                        funciones.reserva_now()
                        funciones.send("s")
                    else:
                        print("-")
                        print('Lo siento, no hay canchas disponibles en este momento')
                elif accion == 'n':
                    print("Esta bien, gracias")
                else:
                    print("ingrese un caracter correcto")
                    access()
            else:
                print(f"Adelante, ingrese por la puerta {reserva[0]}")
                funciones.send("s")
            break  # Salir del bucle