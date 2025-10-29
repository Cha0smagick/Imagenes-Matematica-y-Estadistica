# -*- coding: utf-8 -*-
"""
Script para generar un gráfico de calidad editorial que ilustra el problema
de los mínimos locales en optimización, como en el Descenso del Gradiente.

Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
"""

# ==============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# ==============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ==============================================================================

# Definimos la función no convexa.
# Una parábola (0.1*x^2) con una sinusoide (cos(x)) superpuesta.
def non_convex_function(x):
    """Función no convexa de ejemplo para la visualización."""
    return 0.1 * x**2 + np.cos(x)

# Generamos los datos para el eje X
x_data = np.linspace(-10, 10, 500)
# Calculamos los valores correspondientes del eje Y
y_data = non_convex_function(x_data)

# Coordenadas de puntos de interés (calculados analíticamente o por inspección)
# Mínimo Local
x_local_min = 3.05
y_local_min = non_convex_function(x_local_min)

# Mínimo Global
x_global_min = -3.05
y_global_min = non_convex_function(x_global_min)

# Punto de inicio para el descenso del gradiente (hipotético)
x_start = 8.0
y_start = non_convex_function(x_start)

# ==============================================================================
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ==============================================================================

def create_plot():
    """
    Crea y personaliza el gráfico de la función no convexa.
    """
    # --- Configuración de Estilo y Figura ---
    plt.style.use('seaborn-v0_8-whitegrid')
    mpl.rcParams['font.family'] = 'Arial' # Fuente profesional y legible
    mpl.rcParams['axes.labelweight'] = 'bold'
    mpl.rcParams['axes.titleweight'] = 'bold'

    # Crear la figura con una proporción 16:9 para PowerPoint
    fig, ax = plt.subplots(figsize=(12, 6.75))

    # --- Trazado de la Función y Puntos de Interés ---
    # Curva principal
    ax.plot(x_data, y_data, label='Función de Pérdida No Convexa $f(x)$', color='#440154', linewidth=2.5)

    # Puntos de interés
    ax.plot(x_global_min, y_global_min, 'o', color='#21918c', markersize=12, label='Mínimo Global')
    ax.plot(x_local_min, y_local_min, 'o', color='#fde725', markersize=12, label='Mínimo Local')
    ax.plot(x_start, y_start, 'o', color='#443a83', markersize=12, label='Punto de Inicio')

    # --- Anotaciones y Elementos Explicativos ---
    # Flechas y texto para anotar los puntos
    ax.annotate('Mínimo Global\n(Solución Óptima)', xy=(x_global_min, y_global_min), xytext=(-8, -1.5),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
                fontsize=12, ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1, alpha=0.8))

    ax.annotate('Mínimo Local\n(El algoritmo se detiene aquí)', xy=(x_local_min, y_local_min), xytext=(6, 0),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
                fontsize=12, ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1, alpha=0.8))

    # Línea tangente para mostrar gradiente = 0
    tangent_x = np.linspace(x_local_min - 1.5, x_local_min + 1.5, 10)
    tangent_y = np.full_like(tangent_x, y_local_min)
    ax.plot(tangent_x, tangent_y, '--', color='red', linewidth=2, label='Gradiente = 0')

    # --- Títulos, Etiquetas y Leyenda ---
    ax.set_title('El Problema de los Mínimos Locales en el Descenso del Gradiente', fontsize=18, pad=20)
    ax.set_xlabel('Parámetro del Modelo (ej. peso $w$)', fontsize=14)
    ax.set_ylabel('Valor de la Función de Pérdida', fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    # Colocar la leyenda de forma elegante
    ax.legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.5, -0.15),
              fancybox=True, shadow=True, ncol=4)

    # Ajustar el layout para que todo encaje
    plt.tight_layout(rect=[0, 0.1, 1, 0.95]) # Dejar espacio para copyright y leyenda

    # ==========================================================================
    # 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
    # ==========================================================================
    fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.',
             ha='right', va='bottom', fontsize=10, color='gray', style='italic')

    # ==========================================================================
    # 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
    # ==========================================================================
    plt.savefig("problema_minimos_locales.svg", format='svg', bbox_inches='tight')
    plt.savefig("problema_minimos_locales.png", format='png', dpi=300, bbox_inches='tight')
    
    plt.show()

if __name__ == '__main__':
    create_plot()
