import time

# Para Pedir al usuario el nombre del archivo a buscar
nombre_archivo = input("Ingrese el nombre del archivo a buscar: ")


inicio = time.time()

# Intentar abrir el archivo en modo lectura y escritura
try:
    with open(nombre_archivo, 'r+') as archivo:
        
        contenido = archivo.read()
        print("Contenido del archivo:", contenido)
        
        # Escribir en el archivo
        archivo.write("Nueva información")

except FileNotFoundError:
    print("El archivo especificado no fue encontrado.")

except PermissionError:
    print("No se tienen los permisos necesarios para acceder al archivo.")

except Exception as e:
    print("Ocurrió un error:", e)

fin = time.time()

# Calcular el tiempo transcurrido
tiempo_transcurrido = fin - inicio
print("Tiempo transcurrido: ", tiempo_transcurrido, "segundos")
