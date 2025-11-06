# ----------------------------------------------------------------------------
# SCRIPT PARA VISUALIZAR CONCEPTOS FUNDAMENTALES DE LA TEORÍA DE PROBABILIDAD
#
# Autor: Alejandro Quintero Ruiz (Generado con asistencia de Gemini Code Assist)
# Objetivo: Crear un gráfico de calidad editorial para explicar los
#           conceptos de Espacio Muestral, Evento y Suceso Elemental.
# ----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Rectangle

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS/ESTÉTICOS

# -- Parámetros del Gráfico --
FIG_WIDTH = 16
FIG_HEIGHT = 9
DPI_VALUE = 300
ASPECT_RATIO = FIG_WIDTH / FIG_HEIGHT
FONT_FAMILY = 'Arial' # Una fuente sans-serif clara y profesional
plt.style.use('seaborn-v0_8-whitegrid') # Estilo limpio y profesional

# -- Paleta de Colores (Amigable para Daltónicos - Paleta de Paul Tol) --
COLOR_ESPACIO_MUESTRAL = '#E8E8E8' # Gris claro para el fondo
COLOR_EVENTO = '#DDAA33' # Ocre/Amarillo
COLOR_PUNTOS = '#004488' # Azul oscuro
COLOR_TEXTO_PRINCIPAL = '#333333' # Gris oscuro para texto
COLOR_TEXTO_SECUNDARIO = '#555555'

# -- Parámetros de los Elementos Geométricos --
# Coordenadas y dimensiones para el Espacio Muestral (S)
espacio_muestral_coords = (0, 0)
espacio_muestral_width = 10
espacio_muestral_height = espacio_muestral_width / ASPECT_RATIO

# Coordenadas y dimensiones para el Evento (E)
evento_centro = (espacio_muestral_width * 0.65, espacio_muestral_height * 0.5)
evento_width = espacio_muestral_width * 0.4
evento_height = espacio_muestral_height * 0.6

# Generación de Sucesos Elementales (puntos aleatorios)
num_puntos = 200
np.random.seed(42) # Para reproducibilidad
puntos_x = np.random.uniform(espacio_muestral_coords[0], espacio_muestral_width, num_puntos)
puntos_y = np.random.uniform(espacio_muestral_coords[1], espacio_muestral_height, num_puntos)


# 3. FUNCIÓN O BLOQUE DE GENERACIÓN DEL GRÁFICO

def generar_grafico_probabilidad():
    """
    Genera y configura el gráfico de los conceptos de probabilidad.
    """
    # -- Creación de la figura y los ejes --
    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT), dpi=DPI_VALUE)
    ax.set_facecolor('white')

    # -- Dibujo del Espacio Muestral (S) --
    espacio_muestral = Rectangle(
        espacio_muestral_coords, espacio_muestral_width, espacio_muestral_height,
        facecolor=COLOR_ESPACIO_MUESTRAL, edgecolor=COLOR_TEXTO_PRINCIPAL,
        linewidth=1.5, label='Espacio Muestral (S)'
    )
    ax.add_patch(espacio_muestral)

    # -- Dibujo del Evento (E) --
    evento = Ellipse(
        xy=evento_centro, width=evento_width, height=evento_height,
        facecolor=COLOR_EVENTO, alpha=0.6, edgecolor=COLOR_TEXTO_PRINCIPAL,
        linewidth=1.5, label='Evento o Suceso (E)'
    )
    ax.add_patch(evento)

    # -- Dibujo de los Sucesos Elementales --
    ax.scatter(puntos_x, puntos_y, color=COLOR_PUNTOS, s=25, zorder=3,
               label='Suceso Elemental')

    # -- Ajustes Estéticos y de Ejes --
    ax.set_xlim(-0.5, espacio_muestral_width + 0.5)
    ax.set_ylim(-0.5, espacio_muestral_height + 0.5)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off') # Ocultamos los ejes para un look más de diagrama

    # -- Título y Subtítulo --
    fig.suptitle(
        'Fundamentales de la Teoría de Probabilidad',
        fontsize=24, fontweight='bold', color=COLOR_TEXTO_PRINCIPAL,
        ha='center', x=0.5, y=0.92, fontfamily=FONT_FAMILY
    )

    # -- Anotaciones y Etiquetas --
    # Etiqueta para Espacio Muestral (S)
    ax.text(0.5, espacio_muestral_height - 0.3, 'S: Espacio Muestral',
            fontsize=18, fontweight='bold', color=COLOR_TEXTO_PRINCIPAL,
            ha='left', va='center', fontfamily=FONT_FAMILY)

    # Etiqueta para Evento (E)
    ax.text(evento_centro[0], evento_centro[1] + evento_height * 0.6, 'E: Evento o Suceso',
            fontsize=16, color=COLOR_TEXTO_PRINCIPAL,
            ha='center', va='center', fontfamily=FONT_FAMILY)

    # Anotación para Suceso Elemental
    ax.annotate('Suceso Elemental\n(un resultado posible)',
                xy=(puntos_x[10], puntos_y[10]), xycoords='data',
                xytext=(puntos_x[10] - 2.5, puntos_y[10] + 1.5),
                fontsize=14, color=COLOR_TEXTO_SECUNDARIO,
                arrowprops=dict(arrowstyle="->", color=COLOR_TEXTO_SECUNDARIO),
                ha='center', fontfamily=FONT_FAMILY)

    # Anotaciones de las reglas de probabilidad
    ax.text(espacio_muestral_width * 0.98, 0.3,
            'Reglas: P(S) = 1  y  0 ≤ P(E) ≤ 1',
            fontsize=14, style='italic', color=COLOR_TEXTO_SECUNDARIO,
            ha='right', va='center', fontfamily=FONT_FAMILY)

    return fig, ax

# -- Generar el gráfico --
fig, ax = generar_grafico_probabilidad()


# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT

copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(
    0.98, 0.02,
    copyright_text,
    ha='right',
    va='bottom',
    fontsize=10,
    color=COLOR_TEXTO_SECUNDARIO,
    fontfamily=FONT_FAMILY
)


# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO

# Guardar en formato SVG (vectorial, ideal para PowerPoint y publicaciones)
output_filename_svg = "probabilidad_conceptos_fundamentales.svg"
fig.savefig(output_filename_svg, format='svg', bbox_inches='tight', pad_inches=0.2)

# Opcional: Guardar en formato PNG de alta resolución
output_filename_png = "probabilidad_conceptos_fundamentales.png"
fig.savefig(output_filename_png, format='png', dpi=DPI_VALUE, bbox_inches='tight', pad_inches=0.2)

# Opcional: Guardar en formato PDF (vectorial)
output_filename_pdf = "probabilidad_conceptos_fundamentales.pdf"
fig.savefig(output_filename_pdf, format='pdf', bbox_inches='tight', pad_inches=0.2)

plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}', '{output_filename_png}' y '{output_filename_pdf}'.")

