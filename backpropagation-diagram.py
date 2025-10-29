# -----------------------------------------------------------------------------
# SCRIPT PARA LA VISUALIZACIÓN DEL ALGORITMO DE RETROPROPAGACIÓN (BACKPROPAGATION)
#
# Autor: Alejandro Quintero Ruiz (Generado con asistencia de Gemini Code Assist)
# Objetivo: Crear un gráfico de calidad editorial para explicar el concepto
#           de retropropagación en redes neuronales.
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import matplotlib.pyplot as plt
import numpy as np

# 2. DEFINICIÓN DE DATOS/PARÁMETROS (Conceptuales para la estructura del gráfico)

# Coordenadas para las neuronas de cada capa
input_layer_coords = [(0, y) for y in np.linspace(0.8, -0.8, 3)]
hidden_layer_coords = [(2, y) for y in np.linspace(1, -1, 4)]
output_layer_coords = [(4, 0)]

# Paleta de colores profesional y amigable con el daltonismo
COLOR_FORWARD = '#0072B2'  # Azul
COLOR_BACKWARD = '#D55E00' # Naranja quemado
COLOR_NEURON = '#444444'
COLOR_TEXT = '#333333'
COLOR_ANNOTATION = '#555555'

# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO

def plot_backpropagation_diagram():
    """
    Genera y personaliza el diagrama del algoritmo de retropropagación.
    """
    # --- Configuración inicial del lienzo ---
    # Proporción 16:9 ideal para presentaciones (ej. PowerPoint)
    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # --- Ajustes estéticos del eje ---
    ax.set_xlim(-1.5, 5.5)
    ax.set_ylim(-2, 2)
    ax.axis('off') # Ocultamos los ejes para un look limpio

    # --- Dibujar neuronas ---
    for coords in [input_layer_coords, hidden_layer_coords, output_layer_coords]:
        for (x, y) in coords:
            neuron = plt.Circle((x, y), 0.2, facecolor='white', edgecolor=COLOR_NEURON, lw=1.5, zorder=4)
            ax.add_patch(neuron)

    # --- Dibujar conexiones y flechas (Paso hacia adelante - Forward Pass) ---
    # De capa de entrada a capa oculta
    for start in input_layer_coords:
        for end in hidden_layer_coords:
            ax.plot([start[0] + 0.2, end[0] - 0.2], [start[1], end[1]], color=COLOR_NEURON, alpha=0.3, zorder=1)

    # De capa oculta a capa de salida
    for start in hidden_layer_coords:
        ax.plot([start[0] + 0.2, output_layer_coords[0][0] - 0.2], [start[1], output_layer_coords[0][1]], color=COLOR_NEURON, alpha=0.3, zorder=1)

    # Flechas que indican el flujo hacia adelante
    ax.arrow(-1, 0, 0.6, 0, head_width=0.1, head_length=0.15, fc=COLOR_FORWARD, ec=COLOR_FORWARD, lw=1.5)
    ax.arrow(1, 1.5, 0.6, 0, head_width=0.1, head_length=0.15, fc=COLOR_FORWARD, ec=COLOR_FORWARD, lw=1.5)
    ax.arrow(3, 1.5, 0.6, 0, head_width=0.1, head_length=0.15, fc=COLOR_FORWARD, ec=COLOR_FORWARD, lw=1.5)

    # --- Anotaciones del paso hacia adelante ---
    ax.text(-1.2, 0.2, "Entrada (x)", ha='center', va='bottom', fontsize=12, color=COLOR_TEXT, fontfamily='sans-serif')
    ax.text(4.8, 0, "Salida (ŷ)", ha='center', va='center', fontsize=12, color=COLOR_TEXT, fontfamily='sans-serif')
    ax.text(5.2, 0.5, "Valor Real (y)", ha='center', va='center', fontsize=12, color=COLOR_TEXT, fontfamily='sans-serif')
    ax.plot([4.2, 4.8, 5.2, 4.8], [0, 0, 0.5, 0], color=COLOR_BACKWARD, ls='--', lw=1) # Comparación de error
    ax.text(5.2, 0.25, "Cálculo\ndel Error E(y, ŷ)", ha='center', va='center', fontsize=11, color=COLOR_BACKWARD, fontfamily='sans-serif')

    # --- Dibujar flechas (Paso hacia atrás - Backward Pass) ---
    # De capa de salida a capa oculta
    ax.arrow(output_layer_coords[0][0] - 0.3, -0.5, -1.4, 0, head_width=0.1, head_length=0.15, fc=COLOR_BACKWARD, ec=COLOR_BACKWARD, lw=2, zorder=5)
    # De capa oculta a capa de entrada
    ax.arrow(hidden_layer_coords[0][0] - 0.3, -1.5, -1.4, 0, head_width=0.1, head_length=0.15, fc=COLOR_BACKWARD, ec=COLOR_BACKWARD, lw=2, zorder=5)

    # --- Anotaciones del paso hacia atrás ---
    ax.text(3.2, -0.7, "Propagación del gradiente del error (∂E/∂w)", ha='center', va='top', fontsize=12, color=COLOR_BACKWARD, fontfamily='sans-serif', weight='bold')
    ax.text(1.2, -1.7, "Actualización de pesos y sesgos", ha='center', va='top', fontsize=12, color=COLOR_BACKWARD, fontfamily='sans-serif', weight='bold')

    # --- Etiquetas de las capas y título ---
    font_title = {'family': 'sans-serif', 'color': COLOR_TEXT, 'weight': 'bold', 'size': 18}
    font_label = {'family': 'sans-serif', 'color': COLOR_ANNOTATION, 'weight': 'normal', 'size': 14}

    ax.set_title("El Algoritmo de Retropropagación (Backpropagation)", fontdict=font_title, pad=35)
    ax.text(0, 1.8, "Capa de Entrada", ha='center', fontdict=font_label)
    ax.text(2, 1.8, "Capa Oculta", ha='center', fontdict=font_label)
    ax.text(4, 1.8, "Capa de Salida", ha='center', fontdict=font_label)

    # Anotación general del flujo
    ax.text(2, 2.2, "1. Paso hacia Adelante (Forward Pass) →", ha='center', va='center', fontsize=13, color=COLOR_FORWARD, bbox=dict(facecolor='white', edgecolor=COLOR_FORWARD, boxstyle='round,pad=0.3'))
    ax.text(2, -2.2, "← 2. Paso hacia Atrás (Backward Pass)", ha='center', va='center', fontsize=13, color=COLOR_BACKWARD, bbox=dict(facecolor='white', edgecolor=COLOR_BACKWARD, boxstyle='round,pad=0.3'))

    return fig, ax

# --- Ejecución del script ---
if __name__ == '__main__':
    # Generar el gráfico
    fig, ax = plot_backpropagation_diagram()

    # 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
    # Añadir marca de agua/copyright de forma discreta
    fig.text(0.98, 0.02, "© Alejandro Quintero Ruiz. Generado con Python.",
             ha='right', va='bottom', fontsize=10, color=COLOR_ANNOTATION,
             fontstyle='italic', family='sans-serif')

    # 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
    # Ajustar el layout para que no se corten los elementos
    fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # rect=[left, bottom, right, top]

    # Guardar en formato vectorial SVG (ideal para escalabilidad y calidad)
    output_filename_svg = "backpropagation_diagram.svg"
    fig.savefig(output_filename_svg, format='svg', dpi=300, bbox_inches='tight')

    # Opcional: Guardar en formato PDF y PNG de alta resolución
    output_filename_pdf = "backpropagation_diagram.pdf"
    fig.savefig(output_filename_pdf, format='pdf', dpi=300, bbox_inches='tight')

    output_filename_png = "backpropagation_diagram.png"
    fig.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

    print(f"Gráfico guardado exitosamente en los siguientes formatos:")
    print(f"- {output_filename_svg}")
    print(f"- {output_filename_pdf}")
    print(f"- {output_filename_png}")

    # Mostrar el gráfico (opcional)
    plt.show()
