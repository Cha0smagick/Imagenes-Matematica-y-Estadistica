# -----------------------------------------------------------------------------
# SCRIPT PARA LA VISUALIZACIÓN DE LA FUNCIÓN DE COSTE: ENTROPÍA CRUZADA BINARIA
#
# Objetivo: Generar un gráfico de calidad editorial que ilustre el
#           comportamiento de la función de Entropía Cruzada Binaria (BCE).
# Autor:    Alejandro Quintero Ruiz (Generado con asistencia de Gemini Code Assist)
# Fecha:    2023-10-27
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# -----------------------------------------------------------------------------

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# Generamos un rango de probabilidades predichas, desde un valor muy pequeño
# (epsilon) hasta casi 1, para evitar errores de log(0).
epsilon = 1e-9
predicted_probabilities = np.linspace(epsilon, 1 - epsilon, 500)

# Calculamos el coste para los dos casos de la clasificación binaria:
# Caso 1: La etiqueta verdadera (y) es 1. Coste = -log(p)
cost_if_true_is_1 = -np.log(predicted_probabilities)

# Caso 2: La etiqueta verdadera (y) es 0. Coste = -log(1-p)
cost_if_true_is_0 = -np.log(1 - predicted_probabilities)

# -----------------------------------------------------------------------------

# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
def create_cross_entropy_plot():
    """
    Crea y personaliza el gráfico de la función de coste de Entropía Cruzada Binaria.
    """
    # --- Configuración Inicial y Estilo ---
    # Usamos un estilo limpio y profesional. 'seaborn-v0_8-whitegrid' es una base excelente.
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Creación de la figura y los ejes, con una relación de aspecto 16:9 para PowerPoint.
    fig, ax = plt.subplots(figsize=(12, 6.75))

    # Paleta de colores profesional y amigable con el daltonismo (Azul y Naranja).
    color_y1 = '#0072B2'  # Azul
    color_y0 = '#D55E00'  # Naranja Bermellón

    # --- Trazado de las Curvas ---
    ax.plot(predicted_probabilities, cost_if_true_is_1, label='Coste si la etiqueta real es 1', color=color_y1, linewidth=2.5)
    ax.plot(predicted_probabilities, cost_if_true_is_0, label='Coste si la etiqueta real es 0', color=color_y0, linewidth=2.5)

    # --- Ajustes Estéticos y Etiquetas ---
    # Título y subtítulo para dar contexto.
    fig.suptitle(
        'Función de Coste: Entropía Cruzada Binaria (BCE)',
        fontsize=18,
        fontweight='bold',
        fontfamily='sans-serif'
    )
    ax.set_title(
        'Visualización del coste según la probabilidad predicha por el modelo',
        fontsize=12,
        fontfamily='sans-serif',
        pad=10
    )

    # Etiquetas de los ejes con tipografía clara.
    ax.set_xlabel('Probabilidad Predicha por el Modelo (p)', fontsize=12, fontweight='bold', fontfamily='sans-serif')
    ax.set_ylabel('Coste (Pérdida)', fontsize=12, fontweight='bold', fontfamily='sans-serif')

    # Configuración de los límites y ticks de los ejes para mayor claridad.
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 6) # Limitamos el eje Y para una mejor visualización, aunque el coste tiende a infinito.
    ax.xaxis.set_major_locator(mticker.MultipleLocator(0.1))
    ax.tick_params(axis='both', which='major', labelsize=10)

    # --- Leyenda y Anotaciones ---
    # Colocamos la leyenda en una posición óptima.
    legend = ax.legend(loc='upper center', fontsize=11, frameon=True, shadow=True)
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_alpha(0.8)

    # Anotaciones clave para guiar al espectador.
    ax.annotate(
        'Predicción Correcta\nCoste Mínimo',
        xy=(0.95, 0.1), xytext=(0.7, 0.5),
        arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
        fontsize=11, ha='center', fontfamily='sans-serif'
    )
    ax.annotate(
        'Predicción Incorrecta\nCoste Máximo',
        xy=(0.05, 3), xytext=(0.3, 3.5),
        arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
        fontsize=11, ha='center', fontfamily='sans-serif'
    )

    # Ajuste final del layout para evitar solapamientos.
    fig.tight_layout(rect=[0, 0.05, 1, 0.95]) # Deja espacio en la parte inferior para el copyright.
    
    return fig, ax

# -----------------------------------------------------------------------------

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
def add_copyright(fig):
    """
    Añade una marca de agua de copyright a la figura.
    """
    fig.text(
        0.99, 0.01, # Posición en la esquina inferior derecha
        '© Alejandro Quintero Ruiz. Generado con Python.',
        ha='right',
        va='bottom',
        fontsize=9,
        color='gray',
        alpha=0.8
    )

# -----------------------------------------------------------------------------

# --- Ejecución Principal ---
if __name__ == '__main__':
    # Generamos el gráfico.
    main_figure, main_ax = create_cross_entropy_plot()

    # Añadimos el copyright.
    add_copyright(main_figure)

    # 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
    # Guardamos la imagen en formato SVG (vectorial, ideal para escalabilidad)
    # y PNG (alta resolución para compatibilidad).
    output_filename_svg = 'grafico_entropia_cruzada.svg'
    output_filename_png = 'grafico_entropia_cruzada.png'
    
    main_figure.savefig(output_filename_svg, format='svg', bbox_inches='tight')
    main_figure.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

    print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")
    
    # Mostramos el gráfico en pantalla (opcional).
    plt.show()

