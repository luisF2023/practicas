"""
import tkinter as tk
from tkinter import filedialog
import tabula
import pandas as pd


def extraer_tablas_tabula(ruta_pdf):
    tablas = tabula.read_pdf(ruta_pdf, pages='all')
    return tablas


def guardar_en_excel(tablas, ruta_excel):
    with pd.ExcelWriter(ruta_excel, engine='openpyxl') as writer:
        writer.book.create_sheet("Sheet1")  
        for i, tabla in enumerate(tablas):



            tabla.to_excel(writer, sheet_name=f'Tabla {i+1}')


root = tk.Tk()
root.withdraw()

ruta_pdf = filedialog.askopenfilename(title="Selecciona un archivo PDF", filetypes=[("Archivos PDF", "*.pdf")])

if ruta_pdf:
    tablas_tabula = extraer_tablas_tabula(ruta_pdf)
    nombre_archivo_excel = f"{ruta_pdf[:-4]}.xlsx"

    guardar_en_excel(tablas_tabula, nombre_archivo_excel)

    print(f"Tablas extraídas y guardadas en {nombre_archivo_excel}")
else:
    print("No se pudo extraer ninguna tabla del archivo,selecciona otro archivo PDF.")
"""

import tkinter as tk
from tkinter import filedialog
import json
import tabula
import os
import pandas as pd

def extraer_tablas_tabula(ruta_pdf):
    tablas = tabula.read_pdf(ruta_pdf, pages='all', multiple_tables=True)
    return tablas

def guardar_en_json(tablas, ruta_json):
    data = []
    for tabla in tablas:
        if isinstance(tabla, pd.DataFrame):
            data.append(tabla.to_dict(orient='records'))
    with open(ruta_json, 'w') as file:
        json.dump(data, file)

root = tk.Tk()
root.withdraw()

ruta_pdf = filedialog.askopenfilename(title="Selecciona un archivo PDF", filetypes=[("Archivos PDF", "*.pdf")])

if ruta_pdf:
    tablas = extraer_tablas_tabula(ruta_pdf)
    if tablas:
        ruta_json = os.path.splitext(ruta_pdf)[0] + ".json"
        guardar_en_json(tablas, ruta_json)
        print(f"Tablas extraídas y guardadas de formato Json en {ruta_json}")
    else:
        print("No se pudo extraer ninguna tabla del archivo,selecciona otro archivo PDF.")
else:
    print("No se seleccionó ningún archivo PDF Vuelve a intentarlo nuevamente.")
