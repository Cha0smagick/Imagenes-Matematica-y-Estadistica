# -*- coding: utf-8 -*-
"""
Script para generar un gráfico de alta calidad de la función de Rosenbrock,
ilustrando la optimización mediante Descenso de Gradiente (GD).

Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
Fecha: 2023-10-27
"""

# ==============================================================================
# 1. Importación de Librerías
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# ==============================================================================
# 2. Definición de Datos y Parámetros Matemáticos
# ==============================================================================

# --- Parámetros de la Función de Rosenbrock ---
# f(x, y) = (a - x)² + b(y - x²)²
A = 1.0
B = 100.0

# --- Definición de la función y su gradiente ---
def rosenbrock(x, y, a=A, b=B):
    """Calcula el valor de la función de Rosenbrock."""
    return (a - x)**2 + b * (y - x**2)**2

def rosenbrock_grad(x, y, a=A, b=B):
    """Calcula el gradiente de la función de Rosenbrock."""
    grad_x = -2 * (a - x) - 4 * b * x * (y - x**2)
    grad_y = 2 * b * (y - x**2)
    return np.array([grad_x, grad_y])

# --- Parámetros del Algoritmo de Descenso de Gradiente ---
punto_inicial = np.array([-1.5, 2.5])
tasa_aprendizaje = 0.0012
num_iteraciones = 1500

# --- Simulación del Descenso de Gradiente ---
trayectoria = [punto_inicial]
punto_actual = punto_inicial.copy()

for _ in range(num_iteraciones):
    gradiente = rosenbrock_grad(punto_actual[0], punto_actual[1])
    punto_actual = punto_actual - tasa_aprendizaje * gradiente
    trayectoria.append(punto_actual)

trayectoria = np.array(trayectoria)

# ==============================================================================
# 3. Generación del Gráfico
# ==============================================================================

# --- Configuración del estilo del gráfico ---
plt.style.use('seaborn-v0_8-whitegrid')
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']
mpl.rcParams['axes.labelweight'] = 'bold'
mpl.rcParams['axes.titleweight'] = 'bold'

# --- Creación de la figura y los ejes ---
# Aspect ratio 16:9 para presentaciones
fig, ax = plt.subplots(figsize=(12, 6.75))

# --- Creación de la malla para el gráfico de contorno ---
x_range = np.linspace(-2.0, 2.0, 400)
y_range = np.linspace(-1.0, 3.0, 400)
X, Y = np.meshgrid(x_range, y_range)
Z = rosenbrock(X, Y)

# --- Dibujo del gráfico de contorno ---
# Usamos niveles logarítmicos para visualizar mejor el valle
niveles = np.logspace(0, 3.5, 20)
contour = ax.contourf(X, Y, Z, levels=niveles, cmap='viridis', alpha=0.85)
contour_lines = ax.contour(X, Y, Z, levels=niveles, colors='white', linewidths=0.5, alpha=0.5)

# --- Dibujo de la trayectoria del Descenso de Gradiente ---
ax.plot(trayectoria[:, 0], trayectoria[:, 1], 'r-o', 
        markersize=3, linewidth=1.5, label='Trayectoria del Descenso de Gradiente',
        markevery=[0] + list(range(100, num_iteraciones, 200))) # Marcar solo algunos puntos

# --- Marcadores para puntos clave ---
ax.plot(punto_inicial[0], punto_inicial[1], 'go', markersize=10, label='Punto de Inicio', markeredgecolor='white', markeredgewidth=1.5)
ax.plot(A, A**2, 'm*', markersize=15, label=f'Mínimo Global ({A}, {A})', markeredgecolor='white', markeredgewidth=1.5)

# --- Títulos, etiquetas y leyenda ---
ax.set_title('Optimización de la Función de Rosenbrock con Descenso de Gradiente', fontsize=16, pad=20)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12, rotation=0, labelpad=15)
ax.legend(loc='upper left', fontsize=10, frameon=True, facecolor='white', framealpha=0.8)

# --- Ajustes estéticos ---
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal', adjustable='box')
cbar = fig.colorbar(contour, ax=ax)
cbar.set_label('Valor de f(x, y) - Escala Logarítmica', rotation=270, labelpad=20)

# ==============================================================================
# 4. Adición del Copyright
# ==============================================================================
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.5, 0.01, copyright_text, ha='center', va='bottom', fontsize=8, color='gray')

# ==============================================================================
# 5. Guardado y Exportación del Archivo
# ==============================================================================

# --- Ajustar el layout para que no se corten los elementos ---
fig.tight_layout(rect=[0, 0.03, 1, 0.97]) # Ajustar para dejar espacio al copyright

# --- Guardar en formato vectorial SVG y PNG de alta resolución ---
output_filename_svg = "rosenbrock_optimization_plot.svg"
output_filename_png = "rosenbrock_optimization_plot.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# --- Mostrar el gráfico (opcional) ---
plt.show()

print(f"Gráfico guardado como '{output_filename_svg}' y '{output_filename_png}'.")
