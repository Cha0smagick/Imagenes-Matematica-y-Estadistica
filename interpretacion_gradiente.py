# -*- coding: utf-8 -*-
"""
Script para generar una visualización de alta calidad de la
interpretación geométrica del gradiente de una función escalar.

Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
Fecha: 2023-10-27
"""

# =============================================================================
# 1. Importación de Librerías
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# =============================================================================
# 2. Definición de Datos y Parámetros Matemáticos
# =============================================================================

# Definimos una función escalar f(x, y) para visualizar.
# Usaremos una función cuadrática simple que genera elipses como curvas de nivel.
def f(x, y):
    return x**2 + 2 * y**2

# Creamos una malla de puntos (grid) para evaluar la función.
x = np.linspace(-2.5, 2.5, 400)
y = np.linspace(-2.5, 2.5, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Punto de interés P donde calcularemos el gradiente.
punto_p = np.array([-1.5, 1.0])

# Calculamos el gradiente de f(x, y): ∇f = [∂f/∂x, ∂f/∂y] = [2x, 4y]
gradiente_en_p = np.array([2 * punto_p[0], 4 * punto_p[1]])

# =============================================================================
# 3. Generación del Gráfico
# =============================================================================

# --- Configuración del Estilo del Gráfico ---
# Usamos un estilo profesional y limpio.
plt.style.use('seaborn-v0_8-whitegrid')

# Configuración de la tipografía para legibilidad y estética científica.
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial'] # Fuentes claras y universales
mpl.rcParams['font.size'] = 14
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['axes.titlesize'] = 18
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['legend.fontsize'] = 14

# --- Creación de la Figura y Ejes ---
# Proporción 16:9 ideal para presentaciones.
fig, ax = plt.subplots(figsize=(12, 6.75))

# --- Dibujo de las Curvas de Nivel (Contour Plot) ---
# Usamos un mapa de color amigable con el daltonismo (viridis).
niveles = np.arange(0, 12, 1.0)
contour = ax.contour(X, Y, Z, levels=niveles, cmap='viridis', linewidths=1.0)
ax.clabel(contour, inline=True, fontsize=10, fmt='%1.0f')

# Relleno de color para mejorar la visualización de crecimiento.
contourf = ax.contourf(X, Y, Z, levels=niveles, cmap='viridis', alpha=0.75)

# --- Dibujo del Punto P y los Vectores Gradiente ---
# Punto P
ax.plot(punto_p[0], punto_p[1], 'ko', markersize=10, label='Punto P')
ax.text(punto_p[0] - 0.3, punto_p[1] + 0.1, 'P', fontsize=16, fontweight='bold')

# Vector Gradiente (∇f) - Dirección de máximo crecimiento
ax.arrow(punto_p[0], punto_p[1], gradiente_en_p[0], gradiente_en_p[1],
         head_width=0.15, head_length=0.2, fc='red', ec='red', length_includes_head=True,
         linewidth=1.5, label='Gradiente (∇f)')

# Vector Gradiente Negativo (-∇f) - Dirección de máximo decrecimiento
ax.arrow(punto_p[0], punto_p[1], -gradiente_en_p[0], -gradiente_en_p[1],
         head_width=0.15, head_length=0.2, fc='blue', ec='blue', length_includes_head=True,
         linewidth=1.5, label='Gradiente Negativo (-∇f)')

# --- Ajustes Estéticos Finales ---
ax.set_title('Interpretación Geométrica del Gradiente', pad=20)
ax.set_xlabel('Eje x')
ax.set_ylabel('Eje y')
ax.set_aspect('equal', adjustable='box') # Asegura que la perpendicularidad sea visualmente correcta
ax.legend(loc='upper right')

# Ajustar límites para centrar la vista
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)

# =============================================================================
# 4. Adición del Copyright
# =============================================================================
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.98, 0.02, copyright_text,
         ha='right', va='bottom', fontsize=10, color='gray',
         bbox=dict(facecolor='white', alpha=0.5, edgecolor='none', pad=2))

# Ajustar el layout para que el copyright no se superponga con las etiquetas
fig.tight_layout(rect=[0, 0.03, 1, 0.97])

# =============================================================================
# 5. Guardado y Exportación del Archivo
# =============================================================================
# Guardar en formato vectorial SVG (ideal para escalabilidad y calidad)
output_filename_svg = "interpretacion_gradiente.svg"
fig.savefig(output_filename_svg, format='svg', bbox_inches='tight')

# Guardar en formato PNG de alta resolución (300 DPI) como alternativa
output_filename_png = "interpretacion_gradiente.png"
fig.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")
