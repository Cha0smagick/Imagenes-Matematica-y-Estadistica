# -----------------------------------------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# -----------------------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime

# -----------------------------------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS DE ESTILO
# -----------------------------------------------------------------------------
# -- Parámetros de Estilo Gráfico --
# Paleta de colores profesional y amigable con el daltonismo (Azul-Naranja)
COLOR_FONDO = '#2B303A'  # Gris oscuro azulado
COLOR_TEXTO_PRINCIPAL = '#E6E6E6' # Blanco roto
COLOR_TEXTO_SECUNDARIO = '#C0C5CE' # Gris claro
COLOR_MATRIZ_A = '#0077B6' # Azul profesional
COLOR_MATRIZ_B = '#F77F00' # Naranja vibrante
COLOR_RESULTADO = '#0096C7' # Azul claro (derivado del A)
COLOR_ANOTACION = '#FCBF49' # Amarillo/Naranja claro

# Tipografía
FONT_PRINCIPAL = 'Arial' # Fuente sans-serif limpia y profesional
FONT_MONOESPACIADA = 'Courier New' # Para una alineación perfecta de elementos

# -- Parámetros de la Figura --
ASPECT_RATIO = 16 / 9
FIG_WIDTH = 12 # en pulgadas
FIG_HEIGHT = FIG_WIDTH / ASPECT_RATIO
DPI_EXPORT = 300

# -- Contenido --
COPYRIGHT_TEXT = f"© Alejandro Quintero Ruiz. Generado con Python."

# -----------------------------------------------------------------------------
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# -----------------------------------------------------------------------------
def generar_visualizacion_producto_escalar():
    """
    Genera y estiliza una visualización conceptual del producto escalar
    como un producto matricial.
    """
    # --- Creación de la Figura y Ejes ---
    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT), facecolor=COLOR_FONDO)
    ax.set_facecolor(COLOR_FONDO)

    # Ocultar ejes, espinas y ticks para un lienzo limpio
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis('off')

    # --- Título y Subtítulo ---
    fig.suptitle(
        "Relación entre Producto Escalar y Producto Matricial",
        x=0.5, y=0.88,
        fontsize=24,
        fontweight='bold',
        color=COLOR_TEXTO_PRINCIPAL,
        fontfamily=FONT_PRINCIPAL
    )
    ax.text(
        8.0, 8.0,
        "El producto escalar de dos vectores columna (v · w) se puede expresar como el producto matricial v\u1d40w",
        ha='center', va='center',
        fontsize=14,
        color=COLOR_TEXTO_SECUNDARIO,
        fontfamily=FONT_PRINCIPAL
    )

    # --- Representación Gráfica de la Operación: v^T w ---
    # Coordenadas base para el centrado vertical
    y_base = 4.5

    # Matriz v^T (1 x n)
    ax.add_patch(patches.Rectangle((1.5, y_base - 0.5), 4, 1, facecolor=COLOR_MATRIZ_A, alpha=0.8, ec=COLOR_TEXTO_PRINCIPAL, lw=0.5))
    ax.text(3.5, y_base, "[ v\u2081  v\u2082  ...  v\u2099 ]", ha='center', va='center', fontsize=16, color=COLOR_TEXTO_PRINCIPAL, fontfamily=FONT_MONOESPACIADA)
    ax.text(3.5, y_base - 1.0, "v\u1d40 (1 \u00D7 n)", ha='center', va='center', fontsize=12, color=COLOR_TEXTO_SECUNDARIO, fontfamily=FONT_PRINCIPAL)

    # Matriz w (n x 1)
    ax.add_patch(patches.Rectangle((6.5, y_base - 2), 1, 4, facecolor=COLOR_MATRIZ_B, alpha=0.8, ec=COLOR_TEXTO_PRINCIPAL, lw=0.5))
    ax.text(7.0, y_base + 1.5, "w\u2081", ha='center', va='center', fontsize=16, color=COLOR_TEXTO_PRINCIPAL, fontfamily=FONT_MONOESPACIADA)
    ax.text(7.0, y_base + 0.5, "w\u2082", ha='center', va='center', fontsize=16, color=COLOR_TEXTO_PRINCIPAL, fontfamily=FONT_MONOESPACIADA)
    ax.text(7.0, y_base - 0.5, "...", ha='center', va='center', fontsize=16, color=COLOR_TEXTO_PRINCIPAL, fontfamily=FONT_MONOESPACIADA)
    ax.text(7.0, y_base - 1.5, "w\u2099", ha='center', va='center', fontsize=16, color=COLOR_TEXTO_PRINCIPAL, fontfamily=FONT_MONOESPACIADA)
    ax.text(7.0, y_base - 2.5, "w (n \u00D7 1)", ha='center', va='center', fontsize=12, color=COLOR_TEXTO_SECUNDARIO, fontfamily=FONT_PRINCIPAL)

    # Símbolo de igualdad
    ax.text(8.5, y_base, "=", ha='center', va='center', fontsize=36, color=COLOR_TEXTO_PRINCIPAL, fontfamily=FONT_PRINCIPAL)

    # Matriz Resultado (1 x 1)
    ax.add_patch(patches.Rectangle((9.5, y_base - 0.5), 1, 1, facecolor=COLOR_RESULTADO, alpha=0.9, ec=COLOR_TEXTO_PRINCIPAL, lw=0.5))
    ax.text(10.0, y_base, "s", ha='center', va='center', fontsize=18, fontweight='bold', color=COLOR_TEXTO_PRINCIPAL, fontfamily=FONT_PRINCIPAL)
    ax.text(10.0, y_base - 1.0, "Resultado (1 \u00D7 1)", ha='center', va='center', fontsize=12, color=COLOR_TEXTO_SECUNDARIO, fontfamily=FONT_PRINCIPAL)

    # --- Anotación Explicativa ---
    anotacion = (
        "El producto de una matriz (1 \u00D7 n) y una (n \u00D7 1) da como resultado\n"
        "una matriz (1 \u00D7 1), que es un número real (un escalar)."
    )
    ax.text(
        13.0, 2.0, anotacion,
        ha='center', va='center',
        fontsize=12,
        color=COLOR_ANOTACION,
        fontfamily=FONT_PRINCIPAL,
        bbox=dict(boxstyle='round,pad=0.5', fc=COLOR_FONDO, ec=COLOR_ANOTACION, lw=1, alpha=0.7)
    )

    return fig, ax

# -----------------------------------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# -----------------------------------------------------------------------------
def anadir_copyright(fig):
    """Añade una marca de agua de copyright a la figura."""
    fig.text(
        0.98, 0.02,
        COPYRIGHT_TEXT,
        ha='right',
        va='bottom',
        fontsize=8,
        color=COLOR_TEXTO_SECUNDARIO,
        alpha=0.7,
        fontfamily=FONT_PRINCIPAL
    )

# -----------------------------------------------------------------------------
# 5. BLOQUE PRINCIPAL Y DE GUARDADO/EXPORTACIÓN
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # Generar el gráfico
    figura, ejes = generar_visualizacion_producto_escalar()

    # Añadir el copyright
    anadir_copyright(figura)

    # --- Guardar el archivo ---
    # Se guardará en dos formatos para máxima compatibilidad y calidad.
    # .svg: Formato vectorial, escalable infinitamente, ideal para edición y web.
    # .png: Formato rasterizado de alta resolución, ideal para inserción directa.
    nombre_archivo_base = "visualizacion_producto_escalar_matricial"
    
    # Guardar en formato SVG (Vectorial)
    ruta_svg = f"{nombre_archivo_base}.svg"
    figura.savefig(ruta_svg, format='svg', bbox_inches='tight', pad_inches=0.1)
    print(f"Gráfico guardado exitosamente en: {ruta_svg}")

    # Guardar en formato PNG (Alta resolución)
    ruta_png = f"{nombre_archivo_base}.png"
    figura.savefig(ruta_png, format='png', dpi=DPI_EXPORT, bbox_inches='tight', pad_inches=0.1)
    print(f"Gráfico guardado exitosamente en: {ruta_png}")

    # Opcional: Mostrar el gráfico en una ventana
    # plt.show()
