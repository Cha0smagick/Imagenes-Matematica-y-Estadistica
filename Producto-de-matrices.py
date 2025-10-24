# 1. Importación de Librerías
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 2. Definición de Datos/Parámetros Matemáticos
# Dimensiones simbólicas para la visualización.
# Estos valores controlan la proporción de los rectángulos.
m = 4
n = 6
p = 3

# Paleta de colores (Viridis es amigable con el daltonismo)
color_A = '#440154' # Morado oscuro
color_B = '#21918c' # Verde azulado
color_D = '#fde725' # Amarillo
color_match = '#fca50a' # Naranja para resaltar la dimensión compatible

# Configuración de la fuente
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']


# 3. Función o Bloque de Generación del Gráfico
def generar_grafico_producto_matrices():
    """
    Genera y configura la visualización del producto de matrices.
    """
    # Crear una figura con una proporción 16:9, ideal para presentaciones.
    fig, ax = plt.subplots(figsize=(12.8, 7.2))

    # --- Dibujar las matrices como rectángulos ---
    # Matriz A (m x n)
    mat_A = patches.Rectangle((0, 1), n, m, linewidth=1.5, edgecolor='black', facecolor=color_A, alpha=0.7)
    ax.add_patch(mat_A)
    ax.text(n / 2, m + 1.5, 'Matriz A', ha='center', va='center', fontsize=18, fontweight='bold')
    ax.text(n / 2, 0.5, 'Dimensión: m × n', ha='center', va='center', fontsize=14)

    # Matriz B (n x p)
    mat_B = patches.Rectangle((n + 2, (m - n)/2 + 1), p, n, linewidth=1.5, edgecolor='black', facecolor=color_B, alpha=0.7)
    ax.add_patch(mat_B)
    ax.text(n + 2 + p / 2, (m - n)/2 + n + 0.5, 'Matriz B', ha='center', va='center', fontsize=18, fontweight='bold')
    ax.text(n + 2 + p / 2, (m - n)/2 + -0.0, 'Dimensión: n × p', ha='center', va='center', fontsize=14)

    # Matriz Resultante D = AB (m x p)
    mat_D = patches.Rectangle((n + p + 4, 1), p, m, linewidth=1.5, edgecolor='black', facecolor=color_D, alpha=0.8)
    ax.add_patch(mat_D)
    ax.text(n + p + 4 + p / 2, m + 1.5, 'Matriz D = AB', ha='center', va='center', fontsize=18, fontweight='bold')
    ax.text(n + p + 4 + p / 2, 0.5, 'Dimensión: m × p', ha='center', va='center', fontsize=14)

    # --- Anotaciones para explicar el proceso ---
    # Símbolos de multiplicación e igualdad
    ax.text(n + 1, m/2 + 1, '×', ha='center', va='center', fontsize=30)
    ax.text(n + p + 3, m/2 + 1, '=', ha='center', va='center', fontsize=30)

    # Resaltar la compatibilidad (n == n)
    # Anotación para las columnas de A
    ax.annotate(
        'Columnas = n', xy=(n, m + 1), xytext=(n / 2, m + 2.5),
        arrowprops=dict(facecolor=color_match, edgecolor=color_match, shrink=0.05, width=2, headwidth=8),
        ha='center', va='center', fontsize=14, color=color_match, fontweight='bold'
    )
    # Anotación para las filas de B
    ax.annotate(
        'Filas = n', xy=(n + 2, (m - n)/2 + 1 + n), xytext=(n + 2 + p/2, (m - n)/2 + n + 1.5),
        arrowprops=dict(facecolor=color_match, edgecolor=color_match, shrink=0.05, width=2, headwidth=8),
        ha='center', va='center', fontsize=14, color=color_match, fontweight='bold'
    )
    ax.text(
        n + 1, -1.5, 'Compatibilidad: Deben ser iguales',
        ha='center', va='center', fontsize=15, color=color_match, style='italic'
    )

    # Mostrar cómo se heredan las dimensiones externas (m y p)
    # Guía para la dimensión 'm'
    ax.plot([0, n + p + 4], [m + 1, m + 1], color=color_A, linestyle='--', linewidth=1.5)
    ax.plot([0, 0], [1, m + 1], color=color_A, linestyle='--', linewidth=1.5)
    ax.text(-0.5, (m+1)/2 + 1, 'm', ha='center', va='center', fontsize=16, color=color_A, fontweight='bold')

    # Guía para la dimensión 'p'
    ax.plot([n + 2, n + p + 4], [(m-n)/2 + 1, 1], color=color_B, linestyle='--', linewidth=1.5)
    ax.plot([n + 2 + p, n + 2 + p], [(m-n)/2 + 1, (m-n)/2 + 1 + n], color=color_B, linestyle='--', linewidth=1.5)
    ax.text(n + 2 + p/2, (m-n)/2, 'p', ha='center', va='center', fontsize=16, color=color_B, fontweight='bold')


    # --- Ajustes finales del gráfico ---
    # Título principal
    fig.suptitle(
        'Visualización del Producto de Matrices y sus Dimensiones',
        fontsize=22,
        fontweight='bold'
    )
    # Eliminar ejes y bordes para un look limpio
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1, n + p + 4 + p + 1)
    ax.set_ylim(-2.5, m + 4)
    ax.axis('off')

    return fig, ax

# 4. Bloque de Adición del Copyright
def anadir_copyright(fig):
    """
    Añade una marca de agua de copyright a la figura.
    """
    fig.text(
        0.98, 0.02,
        '© Alejandro Quintero Ruiz. Generado con Python.',
        ha='right',
        va='bottom',
        fontsize=10,
        color='gray',
        style='italic'
    )

# --- Ejecución Principal ---
if __name__ == "__main__":
    # Generar el gráfico
    figura, eje = generar_grafico_producto_matrices()

    # Añadir el copyright
    anadir_copyright(figura)

    # 5. Bloque de Guardado/Exportación del Archivo
    # Guardar en formato SVG para máxima calidad y escalabilidad.
    # También se guarda en PNG de alta resolución como alternativa.
    nombre_archivo_svg = "producto_matrices_visualizacion.svg"
    nombre_archivo_png = "producto_matrices_visualizacion.png"

    figura.savefig(nombre_archivo_svg, format='svg', bbox_inches='tight')
    figura.savefig(nombre_archivo_png, format='png', dpi=300, bbox_inches='tight')

    print(f"Gráfico guardado exitosamente como '{nombre_archivo_svg}' y '{nombre_archivo_png}'.")

    # Opcional: mostrar el gráfico en pantalla si se ejecuta interactivamente.
    # plt.show()

