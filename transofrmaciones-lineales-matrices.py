import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec

# --- 1. Importación de Librerías ---
# numpy para operaciones matriciales y vectoriales
# matplotlib.pyplot para la creación de gráficos
# matplotlib.patches para elementos gráficos personalizados en la leyenda

# --- 2. Definición de Datos/Parámetros Matemáticos ---
# Definimos una matriz de transformación 2x2.
# Esta matriz realizará un cizallamiento y un escalado, lo que permite una visualización clara
# de cómo se deforma el espacio. Es una matriz no singular para una transformación bien definida.
A = np.array([[1.5, 0.5],
              [0.5, 1.5]])

# Vectores base canónicos originales en 2D
i_hat_orig = np.array([1, 0])
j_hat_orig = np.array([0, 1])

# Un vector arbitrario 'v' en el espacio original para demostrar la transformación
v_orig = np.array([0.7, 0.5])

# Calculamos los vectores transformados aplicando la matriz A
i_hat_trans = A @ i_hat_orig
j_hat_trans = A @ j_hat_orig
v_trans = A @ v_orig
 
# --- 3. Bloque de Generación del Gráfico ---
def setup_plot_style():
    """
    Configura el estilo global de Matplotlib para una estética de publicación Q1.
    """
    plt.style.use('seaborn-v0_8-whitegrid') # Un estilo con rejilla sutil y fondo blanco
    # Configuración de fuentes para publicación: tamaños más finos pero legibles.
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans', 'Liberation Sans'], # Prioridad de fuentes
        'font.size': 10,            # Tamaño de fuente base
        'axes.labelsize': 12,       # Tamaño de etiquetas de ejes
        'axes.titlesize': 10,       # Tamaño del título del gráfico (reducido otro 20%)
        'xtick.labelsize': 9,       # Tamaño de etiquetas de ticks X
        'ytick.labelsize': 9,       # Tamaño de etiquetas de ticks Y
        'legend.fontsize': 10,      # Tamaño de fuente de la leyenda
        'figure.titlesize': 18,     # Tamaño del título general de la figura
        'figure.dpi': 300           # Resolución para rasterizados (PNG), aunque SVG/PDF son vectoriales
    })

def create_linear_transformation_plot(A, i_hat, j_hat, v, i_hat_t, j_hat_t, v_t):
    """
    Genera el gráfico de la transformación lineal.
    """
    setup_plot_style()
    
    # Paleta de colores amigable con el daltonismo (ColorBrewer 'Paired')
    colors = plt.cm.get_cmap('Paired', 6)

    # Configuración del tamaño de la figura para una relación de aspecto 16:9 (PowerPoint)
    fig_width = 10  # pulgadas
    fig_height = fig_width * (9/16)
    fig = plt.figure(figsize=(fig_width, fig_height))

    # Usar GridSpec para un control de layout robusto y evitar superposiciones.
    # Se reserva el 100% del espacio para el gráfico principal, la leyenda se manejará por separado.
    ax = fig.add_subplot(1, 1, 1)

    # Título principal del gráfico
    ax.set_title('\nTransformaciones Lineales:\nMatrices en Acción', pad=20, fontweight='bold')
    ax.set_aspect('equal', adjustable='box') # Asegura que las unidades en X e Y sean iguales

    # Ajuste dinámico de los límites de los ejes para que todos los vectores sean visibles
    all_points = np.vstack([i_hat, j_hat, v, i_hat_t, j_hat_t, v_t])
    max_coord = np.max(np.abs(all_points))
    limit = np.ceil(max_coord * 1.2) # Margen del 20%
    # Ajuste de Ylim para bajar el contenido del gráfico: se añade un 35% de espacio en la parte superior.
    top_padding = (limit * 2) * 0.35
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit + top_padding])

    # --- DIBUJAR ESPACIO ORIGINAL ---
    # Cuadrado unitario original (línea discontinua)
    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=colors(0), linestyle='--', alpha=0.6, linewidth=1.5)
    
    # Vector i_hat original (flecha)
    ax.arrow(0, 0, i_hat[0], i_hat[1], head_width=0.08, head_length=0.1, fc=colors(1), ec=colors(1), linewidth=2)
    ax.text(i_hat[0] + 0.1, i_hat[1] - 0.05, 'i', color=colors(1), fontsize=10, fontweight='bold')

    # Vector j_hat original (flecha)
    ax.arrow(0, 0, j_hat[0], j_hat[1], head_width=0.08, head_length=0.1, fc=colors(2), ec=colors(2), linewidth=2)
    ax.text(j_hat[0] - 0.1, j_hat[1] + 0.1, 'j', color=colors(2), fontsize=10, fontweight='bold')

    # Vector v original (flecha punteada)
    ax.arrow(0, 0, v[0], v[1], head_width=0.08, head_length=0.1, fc=colors(3), ec=colors(3), linewidth=2, linestyle=':')
    ax.text(v[0] + 0.1, v[1] + 0.1, 'v', color=colors(3), fontsize=10, fontweight='bold')

    # --- DIBUJAR ESPACIO TRANSFORMADO ---
    # Para dibujar la cuadrícula transformada, transformamos los vértices del cuadrado unitario.
    transformed_square_points = np.array([[0,0], i_hat, i_hat + j_hat, j_hat, [0,0]]).T
    transformed_square_points = A @ transformed_square_points
    ax.plot(transformed_square_points[0,:], transformed_square_points[1,:], color=colors(0), linestyle='-', alpha=0.8, linewidth=1.5)

    # Vector i_hat transformado (flecha sólida)
    ax.arrow(0, 0, i_hat_t[0], i_hat_t[1], head_width=0.08, head_length=0.1, fc=colors(1), ec=colors(1), linewidth=2, linestyle='-', alpha=0.8)
    ax.text(i_hat_t[0] + 0.1, i_hat_t[1] - 0.05, 'A i', color=colors(1), fontsize=10, fontweight='bold')

    # Vector j_hat transformado (flecha sólida)
    ax.arrow(0, 0, j_hat_t[0], j_hat_t[1], head_width=0.08, head_length=0.1, fc=colors(2), ec=colors(2), linewidth=2, linestyle='-', alpha=0.8)
    ax.text(j_hat_t[0] - 0.1, j_hat_t[1] + 0.1, 'A j', color=colors(2), fontsize=10, fontweight='bold')

    # Vector v transformado (flecha sólida)
    ax.arrow(0, 0, v_t[0], v_t[1], head_width=0.08, head_length=0.1, fc=colors(3), ec=colors(3), linewidth=2, linestyle='-', alpha=0.8)
    ax.text(v_t[0] + 0.1, v_t[1] + 0.1, 'A v', color=colors(3), fontsize=10, fontweight='bold')

    # --- FUNCIÓN AUXILIAR PARA ANOTACIONES ---
    def draw_and_adjust_annotations(ax, fig):
        """Dibuja las anotaciones y ajusta su posición para evitar superposiciones."""
        # 1. Dibuja los textos en sus posiciones iniciales deseadas.
        # Usamos coordenadas de la figura (0 a 1) para un posicionamiento preciso. y=0.88 las baja ligeramente.
        text_left = fig.text(0.01, 0.88, f'Matriz de Transformación A:\n[[{A[0,0]:.1f}, {A[0,1]:.1f}]\n [{A[1,0]:.1f}, {A[1,1]:.1f}]]',
                transform=fig.transFigure, fontsize=10, verticalalignment='top', horizontalalignment='left',
                bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='gray', lw=0.5, alpha=0.8))

        text_right = fig.text(0.99, 0.88, 'Propiedades Clave de Matrices:\n'
                           '1. Distributiva: A(B+D) = AB + AD\n'
                           '2. No Conmutativa: AB != BA (en general)\n',
                transform=fig.transFigure, fontsize=10, verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='gray', lw=0.5, alpha=0.8))

        # 2. Forzamos el renderizado del canvas para que los elementos tengan su tamaño y posición final.
        fig.canvas.draw()

        # 3. Obtenemos las "cajas delimitadoras" (bounding boxes) de los textos.
        bbox_left = text_left.get_window_extent()
        bbox_right = text_right.get_window_extent()

        # 4. Verificamos si se superponen y las ajustamos si es necesario.
        if bbox_left.overlaps(bbox_right):
            # Calculamos el solapamiento en píxeles
            overlap = bbox_left.x1 - bbox_right.x0
            # Calculamos cuánto mover cada caja (la mitad del solapamiento + un pequeño margen)
            # Lo convertimos a coordenadas de la figura (0 a 1)
            shift_amount = (overlap / 2 + 5) / fig.get_figwidth() / fig.dpi

            # Obtenemos las posiciones actuales y las movemos
            pos_left = text_left.get_position()
            text_left.set_position((pos_left[0] - shift_amount, pos_left[1]))

            pos_right = text_right.get_position()
            text_right.set_position((pos_right[0] + shift_amount, pos_right[1]))

    # --- ANOTACIONES Y LEYENDA ---
    draw_and_adjust_annotations(ax, fig)

    # Leyenda de la figura, colocada en la parte inferior central para evitar cualquier superposición.
    legend_handles = [ # Se eliminó la línea discontinua de la leyenda para mayor claridad
        mpatches.Patch(color=colors(0), linestyle='--', label='Espacio Original'),
        mpatches.Patch(color=colors(0), linestyle='-', label='Espacio Transformado'),
        mpatches.Patch(color=colors(1), label='Vectores base i, A i'),
        mpatches.Patch(color=colors(2), label='Vectores base j, A j'),
        mpatches.Patch(color=colors(3), label='Vectores v, A v')
    ]
    fig.legend(handles=legend_handles, loc='lower center', bbox_to_anchor=(0.5, 0.02), ncol=3, frameon=False)

    # --- LIMPIEZA FINAL DEL GRÁFICO ---
    # Eliminar ejes y ticks para un look minimalista y enfocado en la visualización.
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    ax.grid(True, linestyle=':', alpha=0.6, color='lightgray')

    return fig

# --- 4. Bloque de Adición del Copyright ---
def add_copyright(fig):
    """
    Añade el texto de copyright a la figura en la parte inferior derecha.
    """
    fig.text(0.99, 0.01, '© Alejandro Quintero Ruiz. Generado con Python.',
             ha='right', va='bottom', fontsize=8, color='gray', alpha=0.7,
             transform=fig.transFigure)

# --- 5. Bloque de Guardado/Exportación del Archivo ---
def save_plot(fig, filename="transformaciones_lineales_matrices_accion"):
    """
    Guarda la figura en múltiples formatos de alta fidelidad.
    """
    # Guardar como SVG (formato vectorial escalable, ideal para presentaciones y publicaciones)
    fig.savefig(f'{filename}.svg', format='svg', bbox_inches='tight', pad_inches=0.1)
    print(f"Gráfico guardado como {filename}.svg")

    # Guardar como PDF (formato vectorial, también excelente para impresión y documentos)
    fig.savefig(f'{filename}.pdf', format='pdf', bbox_inches='tight', pad_inches=0.1)
    print(f"Gráfico guardado como {filename}.pdf")

    # Guardar como PNG de alta resolución (300 DPI, para uso rasterizado de alta calidad)
    fig.savefig(f'{filename}.png', format='png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    print(f"Gráfico guardado como {filename}.png")

# --- Ejecución del script ---
if __name__ == "__main__":
    # Generar el gráfico
    figure = create_linear_transformation_plot(A, i_hat_orig, j_hat_orig, v_orig,
                                             i_hat_trans, j_hat_trans, v_trans)
    
    # Añadir el copyright
    add_copyright(figure)
    
    # Ajustar el layout para asegurar que todo encaje sin superposiciones
    figure.tight_layout(rect=[0, 0.03, 1, 0.85]) # rect=[left, bottom, right, top] -> deja espacio arriba y abajo
    
    # Guardar el gráfico en los formatos especificados
    save_plot(figure)
    
    # Mostrar el gráfico (opcional, útil para visualización inmediata si se ejecuta interactivamente)
    plt.show()
