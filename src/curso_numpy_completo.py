# -*- coding: utf-8 -*-
"""
Proyecto: Sprint Data Science - Curso de NumPy Básico
Integrantes: Filiberto Roldán Acencio, Genaro Torres Urbano, Julián Hernández Romero, Juan Carlos Sosa Aguirre
Descripción: Script único con la implementación progresiva de los videos del curso de NumPy,
             incluyendo comentarios sobre la lógica matemática y de negocio.
"""

import numpy as np

print("=" * 60)
print(" CURSO DE NUMPY BÁSICO - IMPLEMENTACIÓN COMPLETA")
print("=" * 60)

# --- Video 1 al 5: Introducción y uso de listas con arrays ---
# Lógica: Convertir listas nativas a arrays de NumPy para almacenar datos en memoria contigua
lista_datos = [2, 4, 6, 8, 10]
vector = np.array(lista_datos)
print("\n[1] Introducción y Arrays desde Listas:")
print("Vector:", vector, "| Tipo de dato:", vector.dtype)

# --- Video 6 y 7: Funciones básicas y operaciones con arrays ---
# Lógica: Las operaciones se vectorizan a nivel de C, evitando bucles lentos 'for' en Python
vector_b = np.array([1, 3, 5, 7, 9])
suma_arrays = vector + vector_b
multiplicacion_escalar = vector * 3
print("\n[2] Operaciones Básicas Vectorizadas:")
print("Suma (vector + vector_b):", suma_arrays)
print("Multiplicación por escalar (* 3):", multiplicacion_escalar)

# --- Video 8: Uso de los números y rangos (arange / linspace) ---
# Lógica: Generación rápida de secuencias numéricas continuas para análisis
rango_numeros = np.arange(0, 10, 2)  # Del 0 al 10 con salto de 2
espacio_lineal = np.linspace(0, 1, 5)   # 5 números equidistantes entre 0 y 1
print("\n[3] Generación de Números y Rangos:")
print("Arange (0 a 10 con paso 2):", rango_numeros)
print("Linspace (0 a 1 en 5 partes):", espacio_lineal)

# --- Video 9: Implementación de ejes (axis) en matrices ---
# Lógica: axis=0 opera verticalmente (columnas) y axis=1 opera horizontalmente (filas)
matriz = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print("\n[4] Manejo de Ejes (Axis) en Matrices:")
print("Matriz original:\n", matriz)
print("Suma vertical (axis=0 - por columnas):", np.sum(matriz, axis=0))
print("Suma horizontal (axis=1 - por filas):", np.sum(matriz, axis=1))

# --- Video 10: Funciones estadísticas básicas ---
# Lógica: Cálculo rápido de métricas descriptivas para la toma de decisiones analíticas
print("\n[5] Funciones Estadísticas:")
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

print("\n[6] Álgebra Lineal con NumPy:")
print("Producto punto (dot) de matrices:\n", producto_dot)
print("Determinante de matriz_a:", round(determinante, 2))

print("=" * 60)
print(" ¡Ejecución finalizada con éxito!")
print("=" * 60)
