'''
import tkinter as tk
from tkinter import filedialog
import tabula
import pandas as pd


def extraer_tablas_tabula(ruta_pdf):
    tablas = tabula.read_pdf(ruta_pdf, pages='all')
    return tablas


def guardar_en_excel(tablas, ruta_excel):
    with pd.ExcelWriter(ruta_excel) as writer:
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
    print("No se seleccionó ningún archivo PDF.")
'''
import tkinter as tk
from tkinter import filedialog
import pdfplumber
import tabula
import json

def choose_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            print(f"Contenido de la página {page.page_number}:")
            print(page.extract_text())
            print("\n")

def extract_tables(file_path):
    tables_data = []
    tables = tabula.read_pdf(file_path, pages='all', output_format='json')
    for table_num, table in enumerate(tables):
        print(f"Tabla {table_num + 1}:")
        print(table)
    return tables_data

pdf_file_path = choose_pdf_file()
print("Palabras encontradas en el PDF:")
read_pdf(pdf_file_path)
print("Tablas encontradas en el PDF:")
tables_data = extract_tables(pdf_file_path)
