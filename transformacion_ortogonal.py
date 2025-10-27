# -----------------------------------------------------------------------------
# SCRIPT PARA VISUALIZAR LA TRANSFORMACIÓN DE UNA MATRIZ ORTOGONAL
# Autor: Gemini Code Assist, para Alejandro Quintero Ruiz
# Objetivo: Generar un gráfico de calidad editorial que ilustra el efecto
#           geométrico de una matriz ortogonal (rotación) en el espacio 2D.
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

# -----------------------------------------------------------------------------

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS

# Ángulo de rotación en grados. Elegimos un ángulo que sea visualmente claro.
theta_degrees = 35
theta_radians = np.deg2rad(theta_degrees)

# Matriz de rotación 2D (un ejemplo de matriz ortogonal)
# A = [[cos(θ), -sin(θ)],
#      [sin(θ),  cos(θ)]]
rotation_matrix = np.array([
    [np.cos(theta_radians), -np.sin(theta_radians)],
    [np.sin(theta_radians),  np.cos(theta_radians)]
])

# Vectores base originales (e_1 y e_2, o i y j)
# Representan las columnas de la matriz identidad.
i_vec = np.array([1, 0])
j_vec = np.array([0, 1])

# Aplicamos la transformación ortogonal a los vectores base
# El resultado serán las nuevas columnas de la matriz de rotación.
i_vec_transformed = rotation_matrix.dot(i_vec)
j_vec_transformed = rotation_matrix.dot(j_vec)

# -----------------------------------------------------------------------------

# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO

def create_orthogonal_transformation_plot():
    """
    Genera y estiliza el gráfico que muestra la transformación ortogonal.
    """
    # --- Configuración del Estilo y Figura ---
    # Usamos un estilo limpio y profesional.
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Creación de la figura con una relación de aspecto 16:9 para PowerPoint.
    fig, ax = plt.subplots(figsize=(12, 6.75), dpi=150)
    
    # Paleta de colores profesional y amigable con el daltonismo
    # (Azul para original, Naranja para transformado, Gris para ejes)
    color_original = '#0072B2'  # Azul
    color_transformed = '#D55E00' # Naranja bermellón
    color_axes = '#606060'

    # --- Dibujo de los Ejes Coordenados ---
    ax.axhline(0, color=color_axes, linewidth=1.0, zorder=1)
    ax.axvline(0, color=color_axes, linewidth=1.0, zorder=1)

    # --- Dibujo de los Vectores Originales y Transformados ---
    # Origen para todos los vectores
    origin = [0], [0]

    # Vectores originales (i, j)
    ax.quiver(*origin, i_vec[0], i_vec[1], scale=1, scale_units='xy', angles='xy', color=color_original, zorder=3, width=0.008)
    ax.quiver(*origin, j_vec[0], j_vec[1], scale=1, scale_units='xy', angles='xy', color=color_original, zorder=3, width=0.008)

    # Vectores transformados (i', j')
    ax.quiver(*origin, i_vec_transformed[0], i_vec_transformed[1], scale=1, scale_units='xy', angles='xy', color=color_transformed, zorder=3, width=0.008)
    ax.quiver(*origin, j_vec_transformed[0], j_vec_transformed[1], scale=1, scale_units='xy', angles='xy', color=color_transformed, zorder=3, width=0.008)

    # --- Anotaciones y Etiquetas ---
    # Usamos una fuente sans-serif clara y legible como 'Arial' o 'Helvetica'.
    font_config = {'fontname': 'Arial', 'fontsize': 14}

    # Etiquetas para los vectores
    ax.text(i_vec[0] * 1.1, i_vec[1], "i = [1, 0]", color=color_original, ha='left', va='center', **font_config)
    ax.text(j_vec[0], j_vec[1] * 1.1, "j = [0, 1]", color=color_original, ha='center', va='bottom', **font_config)
    
    # Usamos i' y j' para los transformados. El apóstrofo es un carácter Unicode válido.
    ax.text(i_vec_transformed[0] * 1.1, i_vec_transformed[1] * 1.1, "i' = A * i", color=color_transformed, ha='left', va='bottom', **font_config)
    ax.text(j_vec_transformed[0] * 1.1, j_vec_transformed[1] * 1.1, "j' = A * j", color=color_transformed, ha='right', va='bottom', **font_config)

    # --- Elementos Geométricos Adicionales ---
    # Círculo unitario para mostrar que la norma (longitud) se conserva.
    unit_circle = plt.Circle((0, 0), 1, color='gray', linestyle='--', fill=False, linewidth=1.2, zorder=2)
    ax.add_artist(unit_circle)
    ax.text(1.02, 1.02, "Círculo unitario (norma=1)", color='gray', ha='left', va='bottom', style='italic', fontsize=11)

    # Arco para indicar el ángulo de rotación θ
    rotation_arc = Arc((0, 0), 0.5, 0.5, angle=0, theta1=0, theta2=theta_degrees, color='black', linestyle='-', linewidth=1.0)
    ax.add_patch(rotation_arc)
    ax.text(0.35, 0.1, "θ", fontsize=16, ha='center', va='center')

    # --- Ajustes Finales del Gráfico ---
    # Título y subtítulo
    plt.suptitle("Visualización de una Transformación Ortogonal (Rotación)", fontsize=20, y=0.98, fontname='Arial', weight='bold')
    plt.title("Una matriz ortogonal A preserva la longitud y los ángulos entre vectores.", fontsize=14, pad=20, fontname='Arial')

    # Configuración de los límites y aspecto
    lim = 1.4
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal', adjustable='box') # Esencial para que los ángulos se vean de 90°

    # Ocultar los bordes del gráfico para un look más limpio
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Ocultar ticks de los ejes
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Leyenda manual para mayor control y claridad
    ax.text(-lim + 0.1, lim - 0.1, "Original", color=color_original, ha='left', va='top', weight='bold', **font_config)
    ax.text(-lim + 0.1, lim - 0.25, "Transformado", color=color_transformed, ha='left', va='top', weight='bold', **font_config)

    return fig, ax

# -----------------------------------------------------------------------------

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT

def add_copyright(fig):
    """
    Añade la marca de agua de copyright a la figura.
    """
    fig.text(0.98, 0.02, "© Alejandro Quintero Ruiz. Generado con Python.", 
             ha='right', va='bottom', fontsize=10, color='gray',
             fontname='Arial')

# -----------------------------------------------------------------------------

# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO

def save_plot(fig, filename_base):
    """
    Guarda la figura en formatos de alta calidad (SVG, PDF, PNG).
    """
    # Guardar en formato SVG (Vectorial, ideal para escalabilidad)
    svg_path = f"{filename_base}.svg"
    fig.savefig(svg_path, format='svg', bbox_inches='tight', pad_inches=0.1)
    print(f"Gráfico guardado en: {svg_path}")

    # Guardar en formato PDF (Vectorial, ideal para documentos)
    pdf_path = f"{filename_base}.pdf"
    fig.savefig(pdf_path, format='pdf', bbox_inches='tight', pad_inches=0.1)
    print(f"Gráfico guardado en: {pdf_path}")

    # Guardar en formato PNG (Ráster de alta resolución, 300 DPI)
    png_path = f"{filename_base}.png"
    fig.savefig(png_path, format='png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    print(f"Gráfico guardado en: {png_path}")

# -----------------------------------------------------------------------------

# --- Ejecución Principal del Script ---
if __name__ == "__main__":
    # Generar el gráfico
    main_fig, main_ax = create_orthogonal_transformation_plot()
    
    # Añadir el copyright
    add_copyright(main_fig)
    
    # Mostrar el gráfico (opcional, útil para debugging)
    plt.show()
    
    # Guardar el gráfico en múltiples formatos
    save_plot(main_fig, "transformacion_ortogonal")

