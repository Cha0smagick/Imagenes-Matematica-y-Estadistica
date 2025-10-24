import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np # Aunque no se usa directamente para operaciones matriciales aquí, es una buena práctica incluirlo para tareas numéricas.

# --- 1. Importación de Librerías ---
# matplotlib.pyplot para la creación de gráficos.
# matplotlib.patches para formas geométricas como rectángulos.
# numpy para posibles operaciones numéricas (aunque en este script conceptual no se usa directamente para matrices).

# --- 2. Definición de Datos/Parámetros Matemáticos ---
# Para este gráfico conceptual, usaremos representaciones simbólicas de los elementos de la matriz.
# Definimos las dimensiones de las matrices de ejemplo para una ilustración clara.
# Matriz A: m x n
# Matriz B: n x p
# Matriz D (resultado): m x p
m, n, p = 2, 3, 2 # Ejemplo: A (2x3), B (3x2), D (2x2)

# Elementos conceptuales de las matrices A, B y D.
matrix_A_elements = [
    ["A_11", "A_12", "A_13"],
    ["A_21", "A_22", "A_23"]
]

matrix_B_elements = [
    ["B_11", "B_12"],
    ["B_21", "B_22"],
    ["B_31", "B_32"]
]

matrix_D_elements = [
    ["D_11", "D_12"],
    ["D_21", "D_22"]
]

# Índices para resaltar: la primera fila de A, la primera columna de B,
# y el elemento resultante D_11 (índices 0-based).
highlight_row_A = 0
highlight_col_B = 0
highlight_element_D_row = 0
highlight_element_D_col = 0

# --- 3. Función o Bloque de Generación del Gráfico ---
def generate_matrix_multiplication_plot():
    # Configuración de la figura y los ejes para una presentación en PowerPoint (relación de aspecto 16:9).
    fig, ax = plt.subplots(figsize=(16, 9)) # 16 pulgadas de ancho, 9 pulgadas de alto
    ax.set_aspect('equal') # Mantiene la proporción de los elementos visuales.
    ax.set_xlim(-0.5, 10.5) # Ajusta los límites X del gráfico.
    ax.set_ylim(-0.5, 6.5) # Ajusta los límites Y del gráfico.
    ax.axis('off') # Oculta los ejes para un diseño limpio y sin distracciones.

    # Definición de una paleta de colores armónica y legible.
    matrix_text_color = 'black'
    highlight_color_A = '#ADD8E6' # Azul claro (para la fila de A)
    highlight_color_B = '#90EE90' # Verde claro (para la columna de B)
    result_color = '#4682B4' # Azul acero (para el elemento resultante D_ij)
    formula_color = '#333333' # Gris oscuro para las fórmulas y explicaciones.
    arrow_color = 'gray' # Color de las flechas.

    # Configuración de fuentes claras y científicamente aceptadas (sans-serif).
    font_name = 'DejaVu Sans' # Una fuente sans-serif común y legible en Matplotlib.
    matrix_element_fontsize = 14
    formula_fontsize = 16
    title_fontsize = 20
    label_fontsize = 16
    copyright_fontsize = 10

    # Función auxiliar para dibujar una matriz con sus elementos y opcionalmente resaltar una celda.
    def draw_matrix(ax, elements, start_x, start_y, cell_width=0.8, cell_height=0.8,
                    highlight_row=None, highlight_col=None, highlight_color=None,
                    element_color=matrix_text_color, border_color=matrix_text_color):
        rows = len(elements)
        cols = len(elements[0])

        # Dibuja los corchetes de la matriz.
        # Se ajusta el tamaño de los corchetes para que sean proporcionales a la matriz.
        ax.text(start_x - 0.2, start_y + (rows * cell_height / 2) - 0.1, '[',
                fontsize=matrix_element_fontsize * 3, ha='center', va='center', color=border_color, fontfamily=font_name)
        ax.text(start_x + cols * cell_width + 0.2, start_y + (rows * cell_height / 2) - 0.1, ']',
                fontsize=matrix_element_fontsize * 3, ha='center', va='center', color=border_color, fontfamily=font_name)

        # Dibuja cada elemento de la matriz.
        for r_idx, row in enumerate(elements):
            for c_idx, element in enumerate(row):
                x = start_x + c_idx * cell_width + cell_width / 2
                # Invertir el eje Y para que la primera fila (r_idx=0) esté arriba.
                y = start_y + (rows - 1 - r_idx) * cell_height + cell_height / 2

                # Dibuja un fondo de resaltado para la celda si se especifica.
                if highlight_color and ((highlight_row is not None and r_idx == highlight_row and c_idx == highlight_col) or
                                        (highlight_row is None and highlight_col is not None and c_idx == highlight_col) or
                                        (highlight_col is None and highlight_row is not None and r_idx == highlight_row)):
                    rect = patches.Rectangle((x - cell_width/2, y - cell_height/2), cell_width, cell_height,
                                             facecolor=highlight_color, edgecolor='none', alpha=0.6, zorder=1) # zorder para que esté detrás del texto
                    ax.add_patch(rect)

                ax.text(x, y, element, ha='center', va='center', fontsize=matrix_element_fontsize, color=element_color,
                        fontfamily=font_name, zorder=2) # zorder para que el texto esté encima del resaltado
        return start_x, start_y, cols * cell_width, rows * cell_height # Retorna información del bounding box de la matriz

    # --- Dibujar Matriz A ---
    A_x, A_y = 0.5, 3.5
    draw_matrix(ax, matrix_A_elements, A_x, A_y)
    ax.text(A_x + (len(matrix_A_elements[0]) * 0.8 / 2), A_y + len(matrix_A_elements) * 0.8 + 0.3, "Matriz A",
            ha='center', va='bottom', fontsize=label_fontsize, color=formula_color, fontfamily=font_name)

    # --- Dibujar Signo de Multiplicación ---
    ax.text(A_x + len(matrix_A_elements[0]) * 0.8 + 0.7, A_y + (len(matrix_A_elements) * 0.8 / 2), 'x',
            fontsize=title_fontsize, ha='center', va='center', color=formula_color, fontfamily=font_name)

    # --- Dibujar Matriz B ---
    B_x = A_x + len(matrix_A_elements[0]) * 0.8 + 1.5
    B_y = 3.5
    draw_matrix(ax, matrix_B_elements, B_x, B_y)
    ax.text(B_x + (len(matrix_B_elements[0]) * 0.8 / 2), B_y + len(matrix_B_elements) * 0.8 + 0.3, "Matriz B",
            ha='center', va='bottom', fontsize=label_fontsize, color=formula_color, fontfamily=font_name)

    # --- Dibujar Signo de Igual ---
    ax.text(B_x + len(matrix_B_elements[0]) * 0.8 + 0.7, B_y + (len(matrix_B_elements) * 0.8 / 2), '=',
            fontsize=title_fontsize, ha='center', va='center', color=formula_color, fontfamily=font_name)

    # --- Dibujar Matriz D (Resultado) ---
    D_x = B_x + len(matrix_B_elements[0]) * 0.8 + 1.5
    D_y = 3.5
    # Resaltar el elemento específico D_ij que se está calculando.
    draw_matrix(ax, matrix_D_elements, D_x, D_y,
                highlight_row=highlight_element_D_row, highlight_col=highlight_element_D_col,
                highlight_color=result_color)
    ax.text(D_x + (len(matrix_D_elements[0]) * 0.8 / 2), D_y + len(matrix_D_elements) * 0.8 + 0.3, "Matriz D",
            ha='center', va='bottom', fontsize=label_fontsize, color=formula_color, fontfamily=font_name)

    # --- Resaltar la fila y columna específicas para el cálculo ---
    # Resaltar la fila en A.
    A_row_rect = patches.Rectangle((A_x - 0.2, A_y + (len(matrix_A_elements) - 1 - highlight_row_A) * 0.8 - 0.2),
                                   len(matrix_A_elements[0]) * 0.8 + 0.4, 0.8 + 0.4,
                                   facecolor=highlight_color_A, edgecolor='none', alpha=0.4, zorder=0) # zorder bajo para el fondo
    ax.add_patch(A_row_rect)

    # Resaltar la columna en B.
    B_col_rect = patches.Rectangle((B_x + highlight_col_B * 0.8 - 0.2, B_y - 0.2),
                                   0.8 + 0.4, len(matrix_B_elements) * 0.8 + 0.4,
                                   facecolor=highlight_color_B, edgecolor='none', alpha=0.4, zorder=0) # zorder bajo para el fondo
    ax.add_patch(B_col_rect)

    # --- Añadir flechas para indicar el flujo del cálculo ---
    # Flecha desde la fila de A hacia el elemento de D.
    ax.annotate('', xy=(D_x + highlight_element_D_col * 0.8 + 0.4, D_y + (len(matrix_D_elements) - 1 - highlight_element_D_row) * 0.8 + 0.4),
                xytext=(A_x + len(matrix_A_elements[0]) * 0.8 + 0.5, A_y + (len(matrix_A_elements) - 1 - highlight_row_A) * 0.8 + 0.4),
                arrowprops=dict(facecolor=arrow_color, shrink=0.05, width=1.5, headwidth=8, headlength=8),
                zorder=3) # zorder alto para que las flechas estén encima

    # Flecha desde la columna de B hacia el elemento de D.
    ax.annotate('', xy=(D_x + highlight_element_D_col * 0.8 + 0.4, D_y + (len(matrix_D_elements) - 1 - highlight_element_D_row) * 0.8 + 0.4),
                xytext=(B_x + highlight_col_B * 0.8 + 0.4, B_y + len(matrix_B_elements) * 0.8 + 0.5),
                arrowprops=dict(facecolor=arrow_color, shrink=0.05, width=1.5, headwidth=8, headlength=8),
                zorder=3) # zorder alto para que las flechas estén encima

    # --- Fórmula del Componente d_i,j (sin LaTeX) ---
    formula_text = (
        "Fórmula del Componente d_i,j:\n"
        "d_i,j = (i-ésima fila de A) · (j-ésima columna de B)\n"
        "d_i,j = A_i1 * B_1j + A_i2 * B_2j + ... + A_in * B_nj\n"
        "d_i,j = sum(k=1 to n) (A_ik * B_kj)"
    )
    ax.text(D_x + len(matrix_D_elements[0]) * 0.8 + 1.5, D_y + (len(matrix_D_elements) * 0.8 / 2),
            formula_text, ha='left', va='center', fontsize=formula_fontsize, color=formula_color,
            fontfamily=font_name, linespacing=1.5)

    # --- Título del Gráfico ---
    ax.set_title("Producto de Matrices: Producto Fila-Columna",
                 fontsize=title_fontsize, color=formula_color, pad=20, fontfamily=font_name)

    # --- Texto explicativo general ---
    explanation_text = (
        "Cada elemento d_i,j de la matriz resultante D se obtiene como el producto escalar\n"
        "de la i-ésima fila de A y la j-ésima columna de B."
    )
    ax.text(A_x, A_y - 1.5, explanation_text, ha='left', va='top', fontsize=label_fontsize,
            color=formula_color, fontfamily=font_name, linespacing=1.3)

    # --- 4. Bloque de Adición del Copyright ---
    # Marca de agua visible pero discreta en la parte inferior derecha.
    fig.text(0.98, 0.02, "© Alejandro Quintero Ruiz. Generado con Python.",
             ha='right', va='bottom', fontsize=copyright_fontsize, color='gray', fontfamily=font_name)

    # --- 5. Bloque de Guardado/Exportación del Archivo ---
    # Guardar la imagen en formatos vectoriales y de alta resolución.
    output_filename_svg = "producto_matrices_fila_columna.svg"
    output_filename_pdf = "producto_matrices_fila_columna.pdf"
    output_filename_png = "producto_matrices_fila_columna.png"

    plt.savefig(output_filename_svg, format='svg', bbox_inches='tight', dpi=300)
    plt.savefig(output_filename_pdf, format='pdf', bbox_inches='tight', dpi=300)
    plt.savefig(output_filename_png, format='png', bbox_inches='tight', dpi=300)

    print(f"Gráfico guardado como: {output_filename_svg}, {output_filename_pdf}, y {output_filename_png}")
    plt.close(fig) # Cierra la figura para liberar memoria.

# Ejecutar la función para generar el gráfico
if __name__ == "__main__":
    generate_matrix_multiplication_plot()
