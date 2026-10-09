# -*- coding: utf-8 -*-
"""
Script Maestro de Automatización
Creador: Filiberto Roldán Acencio
Descripción: Crea carpetas, instala dependencias faltantes, genera el script 
completo de NumPy con comentarios y ejecuta la práctica en un solo paso.
"""

import os
import sys
import subprocess

print("="*60)
print(" INICIANDO AUTOMATIZACIÓN TOTAL DEL PROYECTO")
print("="*60)

# 1. Crear la estructura de carpetas obligatorias
carpetas = ['src', 'notebooks', 'data']
for carpeta in carpetas:
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"[CARPETA CREADA] /{carpeta}")
    else:
        print(f"[OK] La carpeta /{carpeta} ya existe.")

# 2. Instalar dependencias automáticamente
dependencias = ['numpy', 'pandas', 'matplotlib', 'scikit-learn']
print("\n[INSTALACIÓN] Verificando e instalando librerías requeridas...")
for dep in dependencias:
    try:
        __import__(dep)
        print(f"  - {dep} ya está instalada.")
    except ImportError:
        print(f"  - Instalando {dep}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", dep])

# 3. Crear el archivo de requerimientos y gitignore
with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write("numpy>=1.22.0\npandas>=1.4.0\nscikit-learn>=1.0.0\nmatplotlib>=3.5.0\n")

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write("venv/\n.ipynb_checkpoints/\ndata/\n.DS_Store\n")

print("[ARCHIVOS BASE] requirements.txt y .gitignore creados correctamente.")

# 4. Crear el código fuente de NumPy dentro de la carpeta src/
codigo_numpy = """# -*- coding: utf-8 -*-
\"\"\"
Proyecto: Sprint Data Science - Curso de NumPy Básico
Integrantes: Filiberto Roldán Acencio, Genaro Torres Urbano, Julián Hernández Romero, Juan Carlos Sosa Aguirre
Descripción: Script único con la implementación progresiva de los videos del curso de NumPy,
             incluyendo comentarios sobre la lógica matemática y de negocio.
\"\"\"

import numpy as np

print("=" * 60)
print(" CURSO DE NUMPY BÁSICO - IMPLEMENTACIÓN COMPLETA")
print("=" * 60)

# --- Video 1 al 5: Introducción y uso de listas con arrays ---
# Lógica: Convertir listas nativas a arrays de NumPy para almacenar datos en memoria contigua
lista_datos = [2, 4, 6, 8, 10]
vector = np.array(lista_datos)
print("\\n[1] Introducción y Arrays desde Listas:")
print("Vector:", vector, "| Tipo de dato:", vector.dtype)

# --- Video 6 y 7: Funciones básicas y operaciones con arrays ---
# Lógica: Las operaciones se vectorizan a nivel de C, evitando bucles lentos 'for' en Python
vector_b = np.array([1, 3, 5, 7, 9])
suma_arrays = vector + vector_b
multiplicacion_escalar = vector * 3
print("\\n[2] Operaciones Básicas Vectorizadas:")
print("Suma (vector + vector_b):", suma_arrays)
print("Multiplicación por escalar (* 3):", multiplicacion_escalar)

# --- Video 8: Uso de los números y rangos (arange / linspace) ---
# Lógica: Generación rápida de secuencias numéricas continuas para análisis
rango_numeros = np.arange(0, 10, 2)  # Del 0 al 10 con salto de 2
espacio_lineal = np.linspace(0, 1, 5)   # 5 números equidistantes entre 0 y 1
print("\\n[3] Generación de Números y Rangos:")
print("Arange (0 a 10 con paso 2):", rango_numeros)
print("Linspace (0 a 1 en 5 partes):", espacio_lineal)

# --- Video 9: Implementación de ejes (axis) en matrices ---
# Lógica: axis=0 opera verticalmente (columnas) y axis=1 opera horizontalmente (filas)
matriz = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print("\\n[4] Manejo de Ejes (Axis) en Matrices:")
print("Matriz original:\\n", matriz)
print("Suma vertical (axis=0 - por columnas):", np.sum(matriz, axis=0))
print("Suma horizontal (axis=1 - por filas):", np.sum(matriz, axis=1))

# --- Video 10: Funciones estadísticas básicas ---
# Lógica: Cálculo rápido de métricas descriptivas para la toma de decisiones analíticas
print("\\n[5] Funciones Estadísticas:")
print("Valor máximo global:", np.max(matriz))
print("Valor mínimo global:", np.min(matriz))
print("Media (promedio) general:", np.mean(matriz))
print("Desviación estándar:", np.std(matriz))

# --- Video 11 en adelante: Álgebra lineal básica ---
# Lógica: Multiplicación de matrices y cálculo de determinantes para modelos matemáticos
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])
producto_dot = np.dot(matriz_a, matriz_b)
determinante = np.linalg.det(matriz_a)

print("\\n[6] Álgebra Lineal con NumPy:")
print("Producto punto (dot) de matrices:\\n", producto_dot)
print("Determinante de matriz_a:", round(determinante, 2))

print("=" * 60)
print(" ¡Ejecución finalizada con éxito!")
print("=" * 60)
"""

ruta_archivo = os.path.join("src", "curso_numpy_completo.py")
with open(ruta_archivo, "w", encoding="utf-8") as f:
    f.write(codigo_numpy)

print(f"\n[ÉXITO] Archivo creado en: {ruta_archivo}")
print("="*60)
print("Ejecutando el script de NumPy automáticamente:\n")

# 5. Ejecutar automáticamente el script generado
os.system(f"{sys.executable} {ruta_archivo}")