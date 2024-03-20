import os
import time 

def buscar_archivo():
    nombre_archivo = input("Bienvenido, Ingrese el nombre dpypel archivo que desea buscar: ")
    if os.path.exists(nombre_archivo):
        print(f"El archivo {nombre_archivo} existe.")
        with open(nombre_archivo, 'r') as file:
            contenido = file.read()
            print("Contenido del archivo:")
            print(contenido)
        return nombre_archivo
    else:
        print(f"El archivo {nombre_archivo} no existe.")
        return None

def editar_archivo(nombre_archivo):
    if nombre_archivo is None:
        return

    opcion = input("Desea editar el archivo? (si/no): ")
    if opcion.lower() == 'si':
        with open(nombre_archivo, 'a') as file:
            nueva_linea = input("Ingrese el contenido que desea agregar al archivo: ")
            file.write("\n" + nueva_linea)

def guardar_archivo(nombre_archivo):
    if nombre_archivo is None:
        return

    opcion = input("Desea guardar el archivo? (si/no): ")
    if opcion.lower() == 'si':
        print(f"El archivo {nombre_archivo} ha sido guardado exitosamente.")

#Utilizamos time para calcular el tiempo en que sedemore en correr el archivo
def calcular_tiempo_ejecucion():
    inicio = time.time()
    nombre_archivo = buscar_archivo()
    editar_archivo(nombre_archivo)
    guardar_archivo(nombre_archivo)
    fin = time.time()
    tiempo_total = fin - inicio
    print(f"El Tiempo total de ejecución: {tiempo_total} segundos.")

if __name__ == "__main__":
    calcular_tiempo_ejecucion()

'''
Read ("r") (Leer)
Append ("a") (Agregar)
Write ("w") (Escribir)
Create ("x") (Crear)
'''