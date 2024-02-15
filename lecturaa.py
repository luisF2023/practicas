#lectura
o = open("C:\\Users\\luisf\\OneDrive\\Desktop\\practicas.py\\archivo_escritura.txt","r")

try:
    for linea in o:
        print(linea)
finally:
    o.close()