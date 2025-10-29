# -*- coding: utf-8 -*-
"""
Script para generar un gráfico comparativo de variantes del Descenso del Gradiente.
Visualiza los caminos de optimización de GD, SGD y Adam en una superficie de pérdida.
"""

# ==============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

# ==============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ==============================================================================

# Definimos una función de pérdida con un mínimo global y uno local para ilustrar el concepto.
# Esta es una función comúnmente usada para visualización de optimización.
def loss_function(w1, w2):
    """Función de pérdida con dos mínimos."""
    return (
        0.5 * (w1**2 + 0.5 * w2**2 - 0.3 * w1 * w2)
        + 1.5 * np.sin(1.5 * w1)
        + 2 * np.cos(1.2 * w2)
        + 0.1 * w1
    )

# Generamos los datos para la superficie de contorno
w1_space = np.linspace(-5, 5, 400)
w2_space = np.linspace(-7, 7, 400)
W1, W2 = np.meshgrid(w1_space, w2_space)
Z = loss_function(W1, W2)

# Mínimos (aproximados para la visualización)
global_minimum = np.array([-1.15, 3.9])
local_minimum = np.array([2.9, -2.5])
start_point = np.array([-4.5, -6.0])

# Simulación de las trayectorias de optimización (conceptual)
# Estos no son resultados de una ejecución real, sino representaciones artísticas
# para ilustrar el comportamiento teórico de cada algoritmo.

# GD (Batch): Camino suave y directo hacia el mínimo más cercano.
path_gd = np.array([
    [-4.5, -6.0], [-3.2, -4.5], [-2.5, -3.8], [0.5, -3.0], [2.0, -2.6], [2.9, -2.5]
])

# SGD: Camino ruidoso que explora más y escapa del mínimo local.
path_sgd = np.array([
    [-4.5, -6.0], [-4.0, -4.0], [-2.5, -5.0], [-3.5, -3.0], [-1.5, -3.5],
    [-2.0, -1.5], [0.0, -1.0], [-1.0, 1.0], [-0.5, 3.0], [-1.5, 3.5], [-1.15, 3.9]
])

# Adam: Camino eficiente y adaptativo hacia el mínimo global.
path_adam = np.array([
    [-4.5, -6.0], [-3.0, -3.5], [-1.5, -1.0], [-1.0, 2.0], [-1.2, 3.5], [-1.15, 3.9]
])

# ==============================================================================
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ==============================================================================

# Configuración del estilo (profesional, limpio, moderno)
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': 'Arial', # Fuente clara y profesional
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 11,
    'figure.titlesize': 16,
    'axes.titleweight': 'bold',
    'axes.labelweight': 'bold'
})

# Paleta de colores armónica y amigable con el daltonismo
colors = {'gd': '#377eb8', 'sgd': '#ff7f00', 'adam': '#4daf4a'}

# Creación de la figura y los ejes (aspecto 16:9 para PowerPoint)
fig, ax = plt.subplots(figsize=(12, 6.75))

# Dibujar los contornos de la función de pérdida
contour = ax.contourf(W1, W2, Z, levels=20, cmap='viridis_r', alpha=0.85)
ax.contour(W1, W2, Z, levels=20, colors='white', linewidths=0.3, alpha=0.5)

# Dibujar las trayectorias
for path, label, color in [(path_gd, 'GD (Estándar)', colors['gd']),
                           (path_sgd, 'SGD (Estocástico)', colors['sgd']),
                           (path_adam, 'Adam (Adaptativo)', colors['adam'])]:
    ax.plot(path[:, 0], path[:, 1], marker='o', markersize=4, linestyle='-',
            linewidth=2.5, color=color, label=label,
            path_effects=[path_effects.withStroke(linewidth=4, foreground='white')])

# Marcar puntos de interés
ax.plot(*start_point, 'X', color='red', markersize=12, markeredgewidth=2.5, label='Inicio', zorder=10)
ax.text(global_minimum[0], global_minimum[1] + 0.4, 'Mínimo Global', ha='center', va='bottom', fontsize=11, fontweight='bold', color='#333333')
ax.text(local_minimum[0], local_minimum[1] - 0.4, 'Mínimo Local', ha='center', va='top', fontsize=11, fontweight='bold', color='#333333')

# Ajustes estéticos del gráfico
ax.set_xlabel('Parámetro 1 (w₁)')
ax.set_ylabel('Parámetro 2 (w₂)')
ax.set_title('Comparativa de Variantes del Descenso del Gradiente', pad=20)
ax.set_xlim(w1_space.min(), w1_space.max())
ax.set_ylim(w2_space.min(), w2_space.max())

# Creación de la leyenda
legend = ax.legend(loc='upper left', frameon=True, framealpha=0.9, facecolor='white', edgecolor='gray')
legend.set_title('Algoritmo', prop={'weight':'bold'})

# ==============================================================================
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ==============================================================================
fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.',
         ha='right', va='bottom', fontsize=8, color='gray', style='italic')

# ==============================================================================
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# ==============================================================================
output_filename_svg = 'comparativa_descenso_gradiente.svg'
output_filename_png = 'comparativa_descenso_gradiente.png'

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

plt.show()

print(f"Gráfico guardado como '{output_filename_svg}' y '{output_filename_png}'.")
