# -*- coding: utf-8 -*-
"""
Script para la generación de un gráfico 3D de alta calidad representando
una función escalar de dos variables (f: R^2 -> R), comúnmente utilizada
como función de coste en problemas de optimización.

Este gráfico está diseñado para ser insertado en presentaciones (PowerPoint),
priorizando la legibilidad, el contraste y la estética profesional.

Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
"""

# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm # Colormaps

# =============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# =============================================================================

# Definimos la función de coste z = f(x, y).
# Esta función está diseñada para tener un mínimo global y uno local,
# simulando una superficie de error compleja como las de las redes neuronales.
def funcion_coste(x, y):
    """
    Define una superficie con dos mínimos (uno global y uno local).
    Es una suma de dos funciones gaussianas invertidas.
    """
    # Mínimo global (más profundo)
    p1 = -2.0 * np.exp(-((x - 0.5)**2 + (y - 0.5)**2) / 0.3)
    # Mínimo local (menos profundo)
    p2 = -1.5 * np.exp(-((x + 0.5)**2 + (y + 0.5)**2) / 0.5)
    # Ruido suave para añadir realismo
    ruido = 0.1 * np.cos(5 * x) * np.sin(5 * y)
    return p1 + p2 + ruido

# Creamos la malla de puntos (x, y) donde se evaluará la función.
x = np.linspace(-1.5, 1.5, 200)
y = np.linspace(-1.5, 1.5, 200)
X, Y = np.meshgrid(x, y)
Z = funcion_coste(X, Y)

# =============================================================================
# 3. GENERACIÓN DEL GRÁFICO
# =============================================================================

# --- Configuración Estética General ---
# Usamos un estilo que mejora la estética por defecto.
plt.style.use('seaborn-v0_8-whitegrid')

# Configuración de la fuente para un look profesional y legible.
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': 'Arial', # O 'Calibri', 'Helvetica', etc.
    'font.size': 12,
    'axes.labelweight': 'bold',
    'axes.titleweight': 'bold'
})

# --- Creación de la Figura y Ejes 3D ---
# Proporción 16:9 ideal para presentaciones.
fig = plt.figure(figsize=(12, 6.75))
ax = fig.add_subplot(111, projection='3d')

# --- Dibujo de la Superficie ---
# Se utiliza un colormap amigable con el daltonismo (viridis) y profesional.
surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis, rstride=5, cstride=5, 
                       alpha=0.9, antialiased=True, linewidth=0.1, edgecolor='black')

# --- Ajustes Estéticos y Etiquetas ---
# Título principal del gráfico.
fig.suptitle(
    'Visualización de una Función de Coste Escalar de Varias Variables',
    fontsize=16,
    y=0.95 # Ajuste de la posición vertical del título
)

# Etiquetas de los ejes, describiendo qué representa cada uno.
ax.set_xlabel('Variable 1 (x)', labelpad=10)
ax.set_ylabel('Variable 2 (y)', labelpad=10)
ax.set_zlabel('Coste / Error (z)', labelpad=10)

# Ajuste del ángulo de visión para una mejor perspectiva.
ax.view_init(elev=30, azim=-60)

# Añadir una barra de color para dar escala a los valores de Z.
cbar = fig.colorbar(surf, shrink=0.6, aspect=10, pad=0.1)
cbar.set_label('Valor de la Función de Coste')

# Optimizar el espaciado para que no se solapen los elementos.
fig.tight_layout(rect=[0, 0.05, 1, 0.95]) # Ajuste para dejar espacio al copyright y título

# =============================================================================
# 4. ADICIÓN DEL COPYRIGHT / MARCA DE AGUA
# =============================================================================
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.5, 0.02, copyright_text, ha='center', va='bottom', fontsize=9, color='gray')

# =============================================================================
# 5. GUARDADO / EXPORTACIÓN DEL ARCHIVO
# =============================================================================
# Guardamos la imagen en formato SVG (vectorial) para máxima calidad y escalabilidad.
# También se guarda una copia en PNG de alta resolución como alternativa.
output_filename_svg = "funcion_coste_multivariable.svg"
output_filename_png = "funcion_coste_multivariable.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

# Opcional: Mostrar el gráfico en una ventana.
# plt.show()

