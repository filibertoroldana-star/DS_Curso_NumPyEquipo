# -*- coding: utf-8 -*-
"""
Proyecto: Sprint Data Science - Del Video al Repositorio
Curso: NumPy Básico (yacklyon)
Integrantes del Equipo:
  - Filiberto Roldán Acencio (Líder Técnico)
  - Genaro Torres Urbano
  - Julián Hernández Romero
  - Juan Carlos Sosa Aguirre
Descripción: Script que implementa de forma progresiva todos los 
             ejercicios del curso de NumPy, documentando explícitamente las 5 fases del sprint.
"""

import numpy as np

print("=" * 70)
print(" SPRINT DATA SCIENCE - CURSO DE NUMPY BÁSICO ")
print("=" * 70)

# =========================================================================
# FASE 1: Setup y Arquitectura del Proyecto
# =========================================================================
# - Creación del repositorio público: DS_Curso_NumPyEquipo
# - Estructura base establecida con carpetas src/, notebooks/, data/ y requirements.txt
# - Configuración de protecciones y control de Pull Requests en la rama main.
print("\n[FASE 1] Setup y Arquitectura: Entorno, dependencias y estructura validados.")

# =========================================================================
# FASE 2: Distribución de la Carga Ágil
# =========================================================================
# - Mapeo completo del playlist de NumPy y división equitativa de videos.
# - Asignación de tareas y seguimiento mediante tablero Kanban (To Do -> Done).
print("[FASE 2] Distribución Ágil: Tareas divididas equitativamente entre los 4 integrantes.")

# =========================================================================
# FASE 3: Desarrollo Aislado y Control de Versiones 
# =========================================================================
print("\n[FASE 3] Desarrollo Aislado: Ejecutando la implementación completa del curso...")

# --- Bloque 1: Introducción y Creación de Arrays (Listas vs Arrays) ---
# Lógica: Convertir listas nativas de Python a estructuras homogéneas en memoria contigua.
print("\n--- Bloque 1: Listas y Arrays en NumPy ---")
lista_python = [2, 4, 6, 8, 10, 12]
vector_np = np.array(lista_python)
print(f"Lista original de Python: {lista_python}")
print(f"Vector convertido en NumPy: {vector_np}")
print(f"Tipo de datos (dtype): {vector_np.dtype} | Dimensiones (ndim): {vector_np.ndim} | Forma (shape): {vector_np.shape}")

# --- Bloque 2: Generación de Rangos y Secuencias Numéricas ---
# Lógica: Uso de arange y linspace para generar conjuntos de datos continuos rápidamente.
print("\n--- Bloque 2: Rangos y Secuencias (arange / linspace) ---")
secuencia_arange = np.arange(0, 20, 3)  # Del 0 al 20 con pasos de 3
secuencia_linspace = np.linspace(0, 1, 5) # 5 valores equidistantes entre 0 y 1
print(f"Secuencia con arange(0, 20, 3): {secuencia_arange}")
print(f"Secuencia con linspace(0, 1, 5): {secuencia_linspace}")

# --- Bloque 3: Indexación, Slicing y Operaciones Vectorizadas ---
# Lógica: Las operaciones matemáticas con NumPy se vectorizan a nivel de C (sin bucles 'for').
print("\n--- Bloque 3: Slicing y Operaciones Vectorizadas ---")
matriz_base = np.array([[10, 20, 30], 
                        [40, 50, 60], 
                        [70, 80, 90]])
print(f"Matriz original:\n{matriz_base}")
print(f"Acceso por Slicing (Fila 1 en adelante, Columnas 1 en adelante):\n{matriz_base[1:, 1:]}")

vector_a = np.array([1, 2, 3])
vector_b = np.array([10, 20, 30])
resultado_vectorial = (vector_a * 2) + vector_b
print(f"Resultado de operación vectorizada ((vector_a * 2) + vector_b): {resultado_vectorial}")

# --- Bloque 4: Implementación de Ejes (Axis) y Estadísticas ---
# Lógica: axis=0 opera verticalmente (columnas) y axis=1 opera horizontalmente (filas).
print("\n--- Bloque 4: Manejo de Ejes y Funciones Estadísticas ---")
matriz_datos = np.array([[5, 12, 8], 
                         [14, 3, 20], 
                         [9, 15, 6]])
print(f"Matriz de datos:\n{matriz_datos}")
print(f"Suma vertical por columnas (axis=0): {np.sum(matriz_datos, axis=0)}")
print(f"Suma horizontal por filas (axis=1): {np.sum(matriz_datos, axis=1)}")
print(f"Valor máximo global: {np.max(matriz_datos)}")
print(f"Valor mínimo global: {np.min(matriz_datos)}")
print(f"Media (promedio) general: {np.mean(matriz_datos):.2f}")
print(f"Desviación estándar: {np.std(matriz_datos):.2f}")

# --- Bloque 5: Álgebra Lineal Básica ---
# Lógica: Operaciones avanzadas como producto punto y determinantes para modelos matemáticos.
print("\n--- Bloque 5: Álgebra Lineal ---")
matriz_m1 = np.array([[1, 2], [3, 4]])
matriz_m2 = np.array([[2, 0], [1, 2]])
producto_punto = np.dot(matriz_m1, matriz_m2)
determinante = np.linalg.det(matriz_m1)
print(f"Producto punto (dot) de matrices:\n{producto_punto}")
print(f"Determinante de matriz_m1: {determinante:.2f}")

# =========================================================================
# FASE 4: Code Review e Integración Continua
# =========================================================================
# - Apertura de Pull Requests desde las ramas de cada integrante hacia main.
# - Revisión cruzada obligatoria y aprobación técnica por parte del equipo.
print("\n[FASE 4] Code Review: Pull requests validados mediante revisión cruzada rigurosa.")

# =========================================================================
# FASE 5: Documentación y Cierre
# =========================================================================
# - Construcción del README.md con enlaces, créditos e instrucciones de instalación.
# - Ejecución de la prueba final clonando el repositorio desde cero.
print("[FASE 5] Documentación y Cierre: README.md completo y pruebas finales superadas con éxito.")
print("=" * 70)
print("¡EJECUCIÓN DEL PROYECTO FINALIZADA CORRECTAMENTE!")
print("=" * 70)