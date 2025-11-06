# -*- coding: utf-8 -*-
"""
Script para generar un gráfico de calidad editorial que ilustra el papel de la
probabilidad en la Inteligencia Artificial, mostrando la relación entre una
distribución subyacente, los datos de entrenamiento observados y el ruido.

Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
"""

# ==============================================================================
# 1. Importación de Librerías
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ==============================================================================
# 2. Definición de Datos y Parámetros Matemáticos
# ==============================================================================

# Parámetros para la "distribución desconocida" (usaremos una función seno como base)
np.random.seed(42) # Para reproducibilidad
x_true = np.linspace(0, 10, 200)
y_true = np.sin(x_true * 1.2) * 2.5 + 3

# Generación de "datos de entrenamiento" como realizaciones ruidosas
num_samples = 40
x_observed = np.linspace(0.5, 9.5, num_samples)
noise = np.random.normal(0, 0.6, num_samples) # Ruido Gaussiano
y_observed = np.sin(x_observed * 1.2) * 2.5 + 3 + noise

# ==============================================================================
# 3. Función de Generación del Gráfico
# ==============================================================================

def generar_grafico_probabilidad_ia():
    """
    Crea, estiliza y anota el gráfico conceptual.
    """
    # --- Configuración de Estilo Profesional ---
    plt.style.use('seaborn-v0_8-whitegrid') # Estilo base limpio y profesional
    
    # Paleta de colores armónica y amigable con el daltonismo
    color_true_signal = '#0072B2' # Azul
    color_observed_data = '#D55E00' # Bermellón
    color_annotations = '#333333' # Gris oscuro para texto
    
    # Configuración de la figura y los ejes (aspecto 16:9 para PowerPoint)
    fig, ax = plt.subplots(figsize=(12, 6.75))

    # --- Dibujo de los Elementos del Gráfico ---
    # Curva de la distribución verdadera
    ax.plot(x_true, y_true, color=color_true_signal, linewidth=2.5, linestyle='--', 
            label='Distribución Subyacente (Señal Pura)')

    # Puntos de los datos de entrenamiento observados
    ax.scatter(x_observed, y_observed, color=color_observed_data, s=60, 
               edgecolor='white', linewidth=1, zorder=5, 
               label='Datos de Entrenamiento (Observaciones con Ruido)')

    # --- Ajustes Estéticos y Etiquetas ---
    # Título y subtítulo
    fig.suptitle(
        "La Probabilidad en el Contexto de la IA", 
        fontsize=20, weight='bold', ha='center', x=0.5, y=0.96,
        fontname='Arial'
    )
    ax.set_title(
        "Visualización de datos de entrenamiento como realizaciones de una distribución desconocida",
        fontsize=14, pad=15, color=color_annotations,
        fontname='Arial'
    )
    
    # Etiquetas de los ejes
    ax.set_xlabel("Característica de Entrada (ej. tiempo, tamaño, etc.)", fontsize=12, fontname='Arial')
    ax.set_ylabel("Valor Medido u Observado", fontsize=12, fontname='Arial')

    # Leyenda
    ax.legend(loc='upper right', fontsize=11, frameon=True, fancybox=True, shadow=True)

    # --- Anotaciones para Claridad Conceptual ---
    # Anotación para señalar el "Ruido"
    idx_anotacion = 25 # Elegir un punto para la anotación
    x_point, y_point = x_observed[idx_anotacion], y_observed[idx_anotacion]
    y_true_point = np.sin(x_point * 1.2) * 2.5 + 3
    
    ax.annotate('Ruido', 
                xy=(x_point, (y_point + y_true_point) / 2), 
                xytext=(x_point + 1, y_point - 0.5),
                fontsize=12, color=color_annotations,
                arrowprops=dict(arrowstyle="<->", color=color_annotations, lw=1.5))

    # Ajustar límites y ticks para mayor claridad
    ax.set_xlim(0, 10)
    ax.tick_params(axis='both', which='major', labelsize=11)
    
    return fig, ax

# Generar el gráfico
fig, ax = generar_grafico_probabilidad_ia()

# ==============================================================================
# 4. Bloque de Adición del Copyright
# ==============================================================================
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.98, 0.02, copyright_text, ha='right', va='bottom', fontsize=9, 
         color='#555555', style='italic', fontname='Arial')

# ==============================================================================
# 5. Bloque de Guardado/Exportación del Archivo
# ==============================================================================
output_filename_svg = "probabilidad_en_ia.svg"
fig.savefig(output_filename_svg, format='svg', dpi=300, bbox_inches='tight')

print(f"Gráfico guardado exitosamente como '{output_filename_svg}'")

plt.show() # Opcional: muestra el gráfico en pantalla
