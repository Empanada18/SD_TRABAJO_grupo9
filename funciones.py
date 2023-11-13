from data import data  # Importa la estructura de datos desde data.py
import datetime as dt

DNI = 'DNI'
USUARIO = 'USUARIO'
RESERVA = 'RESERVA'
PUERTA = 'PUERTA'
TIME = 'TIME'
DIA = 'DIA'  

def search(dni):
    for entry in data:
        if entry[DNI] == dni:
            return True
    return False 

def dni_read(dni):
    for entry in data:
        if entry[DNI] == dni:
            puerta = entry[PUERTA]
            reserva = entry[RESERVA]
            return [puerta, reserva]

from datetime import datetime

def disponibilidad_now():
    hora_actual = datetime.now()
    dia_actual = hora_actual.strftime('%d/%m/%Y')
    hora_actual_str = hora_actual.strftime('%H:%M:%S')  # Formato de hora completo

    def verificar_disponibilidad(entry):
        dia_registro = entry['DIA']
        hora_registro = entry['TIME'].split(':')[0]  # Obtener solo la hora del registro

        if dia_registro == dia_actual and hora_registro == hora_actual_str.split(':')[0]:
            return True  # Coincide el día y la hora

    coincidencias = [verificar_disponibilidad(entry) for entry in data if verificar_disponibilidad(entry) is not None]

    if any(coincidencias):
        return [0, None]  # Hay coincidencias, no se puede hacer una reserva
    else:
        return [1, None]  # No hay coincidencias, se puede hacer una reserva

def reserva_now():
    DNI = input('Ingrese DNI nuevamente: ')
    USUARIO = input('Ingrese su nombre y apellido: ')

    hora_actual = dt.datetime.now()
    dia_actual = hora_actual.strftime('%d/%m/%Y')
    hora_actual = hora_actual.strftime('%H:%M:%S')

    disponibilidad = disponibilidad_now()  # Obtener disponibilidad actual

    if disponibilidad[0] == 1:
        puerta = 1  # Si hay disponibilidad, asigna la primera puerta
    else:
        puerta = 2  # Si no hay disponibilidad, asigna la segunda puerta

    new_entry = {
        'DNI': DNI,
        'USUARIO': USUARIO,
        'PUERTA': puerta,
        'TIME': hora_actual,
        'DIA': dia_actual
    }
    data.append(new_entry)

    print(f"Adelante, tiene la cancha {puerta} disponible.")

import serial

# Configura el puerto serial
ser = serial.Serial('COMX', 9600)  # Reemplaza 'COMX' con el nombre de tu puerto COM

def send(signal):
    try:
        ser.open()
        print("Puerto serial abierto")

        ser.write(signal.encode('utf-8'))
        print(f"Señal '{signal}' enviada al Arduino")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        ser.close()
        print("Puerto serial cerrado")