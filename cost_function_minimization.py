# -*- coding: utf-8 -*-
"""
Script para la visualización de la minimización de una función de coste.

Este script genera un gráfico de contorno de alta calidad que ilustra el
concepto de descenso de gradiente sobre una superficie de pérdida. El gráfico
está diseñado para presentaciones (formato 16:9) y publicaciones científicas.

Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
"""

# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# =============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# =============================================================================

# Se define una función de coste convexa J(θ) con dos parámetros (theta_1, theta_2).
# Usaremos una función cuadrática simple que tiene un único mínimo global.
# J(θ) = a*(θ₁ - x₀)² + b*(θ₂ - y₀)²
def cost_function(theta1, theta2):
    """Función de coste J(θ₁, θ₂) a minimizar."""
    return 0.5 * (theta1 - 2)**2 + 2.5 * (theta2 - 1)**2

# Se define el gradiente de la función de coste, ∇J(θ).
# El gradiente es un vector de derivadas parciales: [∂J/∂θ₁, ∂J/∂θ₂].
def gradient(theta1, theta2):
    """Calcula el gradiente de la función de coste en el punto (θ₁, θ₂)."""
    grad_theta1 = theta1 - 2
    grad_theta2 = 5 * (theta2 - 1)
    return np.array([grad_theta1, grad_theta2])

# Parámetros para el algoritmo de descenso de gradiente
learning_rate = 0.15  # Tasa de aprendizaje (α)
num_iterations = 25   # Número de iteraciones

# Puntos de inicio para las trayectorias del descenso de gradiente
start_points = [np.array([-2.0, 3.5]), np.array([5.5, 4.0])]

# =============================================================================
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# =============================================================================

# --- Configuración del estilo del gráfico ---
plt.style.use('seaborn-v0_8-whitegrid') # Estilo profesional y limpio
mpl.rcParams['font.family'] = 'sans-serif' # Fuente clara y aceptada
mpl.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
mpl.rcParams['axes.labelweight'] = 'bold'
mpl.rcParams['axes.titleweight'] = 'bold'
mpl.rcParams['figure.dpi'] = 300 # Alta resolución por defecto

# --- Creación de la figura y los ejes ---
# Proporción 16:9 ideal para presentaciones en PowerPoint
fig, ax = plt.subplots(figsize=(12, 6.75))

# --- Creación de la malla de datos para el contorno ---
theta1_vals = np.linspace(-3, 7, 400)
theta2_vals = np.linspace(-1, 5, 400)
T1, T2 = np.meshgrid(theta1_vals, theta2_vals)
Z = cost_function(T1, T2)

# --- Dibujo del mapa de contorno relleno (heatmap) ---
# Se usa el colormap 'magma', que es perceptualmente uniforme y tiene
# negros/morados oscuros para los valores mínimos, como se solicitó.
contour = ax.contourf(T1, T2, Z, levels=50, cmap='magma')

# --- Cálculo y dibujo de las trayectorias de descenso de gradiente ---
for start_point in start_points:
    path = [start_point]
    current_point = start_point.copy()
    for _ in range(num_iterations):
        grad = gradient(current_point[0], current_point[1])
        current_point -= learning_rate * grad
        path.append(current_point.copy())
    path = np.array(path)
    
    # Dibuja la trayectoria
    ax.plot(path[:, 0], path[:, 1], 'o-', color='cyan', markersize=4, linewidth=1.5, label='Trayectoria de Optimización')
    # Marca el punto de inicio
    ax.plot(start_point[0], start_point[1], 'o', color='lime', markersize=8, markeredgecolor='black')

# --- Marcado del punto mínimo ---
# El mínimo de nuestra función está en (2, 1)
min_point = np.array([2.0, 1.0])
ax.plot(min_point[0], min_point[1], '*', color='red', markersize=15, markeredgecolor='white', label='Mínimo Global (∇J(θ)=0)')

# --- Ajustes estéticos, etiquetas y título ---
ax.set_xlabel('Parámetro θ₁ (Peso 1)', fontsize=14)
ax.set_ylabel('Parámetro θ₂ (Peso 2)', fontsize=14)
ax.set_title('Minimización de la Función de Coste mediante Descenso de Gradiente', fontsize=16, pad=20)

# --- Creación de la barra de color ---
cbar = fig.colorbar(contour)
cbar.set_label('Valor de la Función de Coste J(θ)', fontsize=14, rotation=270, labelpad=20)

# --- Leyenda ---
# Para evitar etiquetas duplicadas en la leyenda
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), fontsize=12, loc='upper left')

ax.set_aspect('equal', adjustable='box')

# =============================================================================
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# =============================================================================
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.98, 0.02, copyright_text,
         ha='right', va='bottom', fontsize=10, color='gray',
         bbox=dict(facecolor='white', alpha=0.6, edgecolor='none', boxstyle='round,pad=0.2'))

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajusta el layout para que no se corte nada

# =============================================================================
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# =============================================================================
# Se guardará en formato SVG (vectorial, escalable) y PNG (alta resolución).
output_filename_svg = "cost_function_minimization.svg"
output_filename_png = "cost_function_minimization.png"

try:
    plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
    plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")

# Muestra el gráfico en la consola/notebook (opcional)
plt.show()
