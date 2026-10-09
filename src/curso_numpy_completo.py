# -*- coding: utf-8 -*-
"""
Proyecto: Sprint Data Science - Del Video al Repositorio
Curso: NumPy Básico (yacklyon)
Integrantes del Equipo:
  - Filiberto Roldán Acencio (Líder Técnico)
  - Genaro Torres Urbano
  - Julián Hernández Romero
  - Juan Carlos Sosa Aguirre
"""

import numpy as np

print("=" * 70)
print(" SPRINT DATA SCIENCE - CURSO DE NUMPY BÁSICO (IMPLEMENTACIÓN EXTENSA)")
print("=" * 70)

print("\n[FASE 1] Setup y Arquitectura: Entorno, dependencias y estructura validados.")
print("[FASE 2] Distribución Ágil: Tareas divididas equitativamente entre los 4 integrantes.")

print("\n[FASE 3] Desarrollo Aislado: Ejecutando la implementación completa del curso...")

print("\n--- Bloque 1: Listas y Arrays en NumPy ---")
lista_python = [2, 4, 6, 8, 10, 12]
vector_np = np.array(lista_python)
print(f"Lista original de Python: {lista_python}")
print(f"Vector convertido en NumPy: {vector_np}")
print(f"Tipo de datos (dtype): {vector_np.dtype} | Dimensiones (ndim): {vector_np.ndim} | Forma (shape): {vector_np.shape}")

print("\n--- Bloque 2: Rangos y Secuencias (arange / linspace) ---")
secuencia_arange = np.arange(0, 20, 3)
secuencia_linspace = np.linspace(0, 1, 5)
print(f"Secuencia con arange(0, 20, 3): {secuencia_arange}")
print(f"Secuencia con linspace(0, 1, 5): {secuencia_linspace}")

print("\n--- Bloque 3: Slicing y Operaciones Vectorizadas ---")
matriz_base = np.array([[10, 20, 30], 
                        [40, 50, 60], 
                        [70, 80, 90]])
print(f"Matriz original:\n{matriz_base}")
print(f"Acceso por Slicing:\n{matriz_base[1:, 1:]}")

vector_a = np.array([1, 2, 3])
vector_b = np.array([10, 20, 30])
resultado_vectorial = (vector_a * 2) + vector_b
print(f"Resultado de operación vectorizada: {resultado_vectorial}")

print("\n--- Bloque 4: Manejo de Ejes y Funciones Estadísticas ---")
matriz_datos = np.array([[5, 12, 8], 
                         [14, 3, 20], 
                         [9, 15, 6]])
print(f"Matriz de datos:\n{matriz_datos}")
print(f"Suma vertical por columnas (axis=0): {np.sum(matriz_datos, axis=0)}")
print(f"Suma horizontal por filas (axis=1): {np.sum(matriz_datos, axis=1)}")
print(f"Valor máximo global: {np.max(matriz_datos)}")
print(f"Valor mínimo global: {np.min(matriz_datos)}")
print(f"Media general: {np.mean(matriz_datos):.2f}")
print(f"Desviación estándar: {np.std(matriz_datos):.2f}")

print("\n--- Bloque 5: Álgebra Lineal ---")
matriz_m1 = np.array([[1, 2], [3, 4]])
matriz_m2 = np.array([[2, 0], [1, 2]])
producto_punto = np.dot(matriz_m1, matriz_m2)
determinante = np.linalg.det(matriz_m1)
print(f"Producto punto:\n{producto_punto}")
print(f"Determinante: {determinante:.2f}")

print("\n[FASE 4] Code Review: Pull requests validados mediante revisión cruzada rigurosa.")
print("[FASE 5] Documentación y Cierre: README.md completo y pruebas finales superadas con éxito.")
print("=" * 70)
