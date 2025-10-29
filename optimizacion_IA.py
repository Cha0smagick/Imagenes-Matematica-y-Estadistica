# -*- coding: utf-8 -*-
"""
Script para generar un gráfico de calidad editorial sobre el concepto de
optimización en Inteligencia Artificial.

Este script visualiza una función de pérdida no convexa, destacando los
mínimos locales y globales, y el proceso de descenso de gradiente.

Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
Fecha: 2023-10-27
"""

# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# =============================================================================

# Definimos la función de pérdida J(θ) (una función no convexa)
# J(θ) = 0.1θ^4 + 0.2θ^3 - 1.5θ^2 - 1.8θ + 5
def loss_function(theta):
    return 0.1*theta**4 + 0.2*theta**3 - 1.5*theta**2 - 1.8*theta + 5

# Definimos la derivada de la función de pérdida (gradiente)
# J'(θ) = 0.4θ^3 + 0.6θ^2 - 3.0θ - 1.8
def gradient(theta):
    return 0.4*theta**3 + 0.6*theta**2 - 3.0*theta - 1.8

# Rango de valores para el parámetro θ
theta_values = np.linspace(-4.5, 3.5, 400)
# Calculamos los valores de la función de pérdida para cada θ
loss_values = loss_function(theta_values)

# Puntos de interés para las anotaciones
global_min_theta = 2.55
local_min_theta = -2.8
gradient_point_theta = -1.0

# =============================================================================
# 3. GENERACIÓN DEL GRÁFICO
# =============================================================================

# --- Configuración de Estilo Profesional ---
plt.style.use('seaborn-v0_8-whitegrid') # Estilo base limpio
sns.set_palette("colorblind") # Paleta de colores amigable para daltónicos
plt.rcParams['font.family'] = 'Arial' # Tipografía profesional
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.titleweight'] = 'bold'

# --- Creación de la Figura y Ejes (Aspecto 16:9) ---
fig, ax = plt.subplots(figsize=(12, 6.75))

# --- Dibujo de la Función de Pérdida ---
ax.plot(theta_values, loss_values, label="Función de Pérdida J(θ)", linewidth=2.5)

# --- Anotaciones y Puntos Clave ---
# Mínimo Global
ax.plot(global_min_theta, loss_function(global_min_theta), 'o', markersize=10, color=sns.color_palette()[2])
ax.annotate('Mínimo Global\n(Objetivo de la Optimización)', 
            xy=(global_min_theta, loss_function(global_min_theta)),
            xytext=(global_min_theta - 0.2, loss_function(global_min_theta) + 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
            ha='right', va='bottom', fontsize=12, fontweight='bold')

# Mínimo Local
ax.plot(local_min_theta, loss_function(local_min_theta), 'o', markersize=10, color=sns.color_palette()[3])
ax.annotate('Mínimo Local', xy=(local_min_theta, loss_function(local_min_theta)),
            xytext=(-4.2, loss_function(local_min_theta) + 2),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
            ha='left', va='center', fontsize=12)

# Punto y Tangente para ilustrar el Gradiente
x0 = gradient_point_theta
y0 = loss_function(x0)
slope = gradient(x0)
tangent_x = np.linspace(x0 - 0.8, x0 + 0.8, 10)
tangent_y = y0 + slope * (tangent_x - x0)
ax.plot(tangent_x, tangent_y, '--', color='gray', linewidth=2, label='Gradiente (Derivada)')
ax.annotate('Descenso de Gradiente', xy=(x0 + 0.5, y0 + slope * 0.5),
            xytext=(x0 + 1.0, y0 + 4),
            arrowprops=dict(facecolor=sns.color_palette()[1], shrink=0.05, width=1.5, headwidth=10, connectionstyle="arc3,rad=-0.2"),
            ha='center', va='center', fontsize=12, color=sns.color_palette()[1], fontweight='bold')

# --- Ajustes Finales del Gráfico ---
ax.set_title("La Optimización como Proceso de Minimización de Pérdida en IA")
ax.set_xlabel("Parámetro del Modelo (θ)")
ax.set_ylabel("Función de Pérdida J(θ)")
ax.legend(fontsize=12, loc='upper left')
ax.set_ylim(bottom=-1) # Ajuste para dar espacio visual
sns.despine() # Elimina los bordes superior y derecho para un look más limpio

# =============================================================================
# 4. ADICIÓN DEL COPYRIGHT
# =============================================================================
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.98, 0.02, copyright_text, ha='right', va='bottom', fontsize=10, color='gray')

# =============================================================================
# 5. GUARDADO Y EXPORTACIÓN DEL ARCHIVO
# =============================================================================
output_filename = "optimizacion_en_ia.svg"
plt.savefig(output_filename, format='svg', dpi=300, bbox_inches='tight')

print(f"Gráfico guardado exitosamente como '{output_filename}'")
