# 1. Importación de Librerías
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patheffects import withStroke

# -----------------------------------------------------------------------------

# 2. Definición de Datos/Parámetros
# Este gráfico es conceptual, por lo que los "datos" son en realidad parámetros de estilo y posición.

# --- Configuración General de Estilo ---
BG_COLOR = "#f0f0f0"  # Color de fondo para la visualización (no para el guardado)
FONT_FAMILY = "Arial"
TITLE_FONT_SIZE = 22
SUBTITLE_FONT_SIZE = 18
LABEL_FONT_SIZE = 14
MATRIX_LABEL_FONT_SIZE = 20
COPYRIGHT_FONT_SIZE = 10
PRIMARY_TEXT_COLOR = "#333333"
SECONDARY_TEXT_COLOR = "#555555"

# --- Paleta de Colores (Amigable para Daltónicos) ---
COLOR_A = "#003f5c"
COLOR_B = "#7a5195"
COLOR_D = "#ef5675"
COLOR_RESULT = "#ffa600"

# --- Parámetros de la Figura ---
FIG_WIDTH = 16
FIG_HEIGHT = 9
DPI = 300

# -----------------------------------------------------------------------------

def create_matrix_box(ax, center_x, center_y, width, height, color, label, dim_label=""):
    """
    Función auxiliar para dibujar una matriz como una caja con sombra y etiquetas.
    """
    # Sombra
    shadow = patches.Rectangle(
        (center_x - width / 2 + 0.03, center_y - height / 2 - 0.03),
        width, height,
        transform=ax.transData,
        facecolor="black",
        alpha=0.2,
        zorder=1
    )
    ax.add_patch(shadow)

    # Caja principal
    rect = patches.Rectangle(
        (center_x - width / 2, center_y - height / 2),
        width, height,
        transform=ax.transData,
        facecolor=color,
        edgecolor="black",
        linewidth=1.5,
        zorder=2
    )
    ax.add_patch(rect)

    # Etiqueta de la matriz (ej. 'A')
    ax.text(
        center_x, center_y, label,
        ha='center', va='center',
        fontsize=MATRIX_LABEL_FONT_SIZE,
        fontweight='bold',
        color='white',
        fontfamily=FONT_FAMILY,
        path_effects=[withStroke(linewidth=2, foreground='black')],
        zorder=3
    )
    
    # Etiqueta de dimensión (ej. 'm x n')
    if dim_label:
        ax.text(
            center_x, center_y - height / 2 - 0.05, dim_label,
            ha='center', va='top',
            fontsize=LABEL_FONT_SIZE,
            color=PRIMARY_TEXT_COLOR,
            fontfamily=FONT_FAMILY,
            zorder=3
        )

def main():
    """
    Función principal para generar y guardar el gráfico.
    """
    # 3. Función o Bloque de Generación del Gráfico
    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT), facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    # --- Configuración de los ejes y el título principal ---
    ax.set_xlim(0, FIG_WIDTH)
    ax.set_ylim(0, FIG_HEIGHT)
    ax.axis('off') # Ocultar ejes para un look de diagrama

    fig.suptitle(
        "Propiedades del Producto de Matrices",
        fontsize=TITLE_FONT_SIZE,
        fontweight='bold',
        color=PRIMARY_TEXT_COLOR,
        fontfamily=FONT_FAMILY,
        y=0.96
    )

    # --- SECCIÓN 1: Propiedad Distributiva: A(B+D) = AB + AD ---
    y_dist = 5.5
    ax.text(FIG_WIDTH / 2, y_dist + 1.8, "Propiedad Distributiva: A(B + D) = AB + AD",
            ha='center', va='center', fontsize=SUBTITLE_FONT_SIZE, fontweight='bold',
            color=PRIMARY_TEXT_COLOR, fontfamily=FONT_FAMILY)

    # Lado izquierdo: A(B+D)
    create_matrix_box(ax, 2, y_dist, 1.5, 2, COLOR_A, "A")
    ax.text(3.1, y_dist, "x", ha='center', va='center', fontsize=24)
    create_matrix_box(ax, 4.5, y_dist + 0.5, 2, 1, COLOR_B, "B")
    ax.text(4.5, y_dist, "+", ha='center', va='center', fontsize=24)
    create_matrix_box(ax, 4.5, y_dist - 0.5, 2, 1, COLOR_D, "D")
    
    # Símbolo de igualdad
    ax.text(FIG_WIDTH / 2, y_dist, "=", ha='center', va='center', fontsize=40, fontweight='bold')

    # Lado derecho: AB + AD
    create_matrix_box(ax, 9.5, y_dist, 1.5, 2, COLOR_A, "A")
    create_matrix_box(ax, 11.2, y_dist, 2, 2, COLOR_B, "B")
    ax.text(12.6, y_dist, "+", ha='center', va='center', fontsize=24)
    create_matrix_box(ax, 14, y_dist, 1.5, 2, COLOR_A, "A")
    create_matrix_box(ax, 15.7, y_dist, 2, 2, COLOR_D, "D")


    # --- SECCIÓN 2: Propiedad No Conmutativa: AB ≠ BA ---
    y_noncom = 2.5
    ax.text(FIG_WIDTH / 2, y_noncom + 1.2, "Propiedad No Conmutativa: AB ≠ BA",
            ha='center', va='center', fontsize=SUBTITLE_FONT_SIZE, fontweight='bold',
            color=PRIMARY_TEXT_COLOR, fontfamily=FONT_FAMILY)

    # Lado izquierdo: AB
    create_matrix_box(ax, 2, y_noncom, 1.5, 1, COLOR_A, "A", dim_label="(2x3)")
    ax.text(3.1, y_noncom, "x", ha='center', va='center', fontsize=24)
    create_matrix_box(ax, 4.2, y_noncom, 1, 1.5, COLOR_B, "B", dim_label="(3x2)")
    ax.text(5.3, y_noncom, "→", ha='center', va='center', fontsize=30)
    create_matrix_box(ax, 6.5, y_noncom, 1, 1, COLOR_RESULT, "AB", dim_label="(2x2)")

    # Símbolo de no igualdad
    ax.text(FIG_WIDTH / 2, y_noncom, "≠", ha='center', va='center', fontsize=40, fontweight='bold')

    # Lado derecho: BA
    create_matrix_box(ax, 9.8, y_noncom, 1, 1.5, COLOR_B, "B", dim_label="(3x2)")
    ax.text(10.9, y_noncom, "x", ha='center', va='center', fontsize=24)
    create_matrix_box(ax, 12, y_noncom, 1.5, 1, COLOR_A, "A", dim_label="(2x3)")
    ax.text(13.1, y_noncom, "→", ha='center', va='center', fontsize=30)
    create_matrix_box(ax, 14.5, y_noncom, 1.5, 1.5, COLOR_RESULT, "BA", dim_label="(3x3)")

    # 4. Bloque de Adición del Copyright
    copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
    ax.text(
        FIG_WIDTH / 2, 0.1, copyright_text,
        ha='center', va='bottom',
        fontsize=COPYRIGHT_FONT_SIZE,
        color=SECONDARY_TEXT_COLOR,
        fontfamily=FONT_FAMILY
    )

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajustar para que todo encaje

    # 5. Bloque de Guardado/Exportación del Archivo
    # Guardar en formato vectorial SVG (ideal para escalabilidad)
    plt.savefig("propiedades_matrices.svg", format="svg", transparent=True)
    
    # Guardar en formato PNG de alta resolución (para compatibilidad)
    plt.savefig("propiedades_matrices.png", format="png", dpi=DPI, transparent=True)

    print("Gráficos 'propiedades_matrices.svg' y 'propiedades_matrices.png' generados exitosamente.")
    
    # Opcional: mostrar el gráfico en una ventana
    plt.show()


if __name__ == "__main__":
    main()

