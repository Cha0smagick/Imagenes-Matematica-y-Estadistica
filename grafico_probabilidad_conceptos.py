# ----------------------------------------------------------------------------
# SCRIPT PARA VISUALIZACIÓN DE OPERACIONES DE EVENTOS Y PROPIEDADES DE PROBABILIDAD
#
# Objetivo: Generar un gráfico de calidad editorial para ilustrar conceptos
#           fundamentales de la teoría de la probabilidad.
# Autor:    Alejandro Quintero Ruiz (Generado a través de Asistente de IA)
# Fecha:    2023-10-27
# ----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS DE ESTILO
# -------------------------------------------------
# Configuración general de estilo para los gráficos
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans' # Fuente sans-serif clara y profesional
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['figure.titlesize'] = 16
plt.rcParams['figure.titleweight'] = 'bold'

# Paleta de colores (considerando daltonismo)
COLOR_E = '#0072B2'  # Azul
COLOR_F = '#D55E00'  # Naranja Bermellón
ALPHA_FILL = 0.4     # Transparencia para las áreas
ALPHA_EDGE = 0.9     # Transparencia para los bordes

# Parámetros geométricos para los círculos
C1_CENTER = (-0.25, 0)
C2_CENTER = (0.25, 0)
RADIUS = 0.4

# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# -------------------------------------
def crear_grafico_probabilidad():
    """
    Crea y configura la figura con 4 subplots para ilustrar los conceptos
    de unión, intersección, eventos excluyentes y el axioma de la unión.
    """
    # Crear figura y ejes con una proporción 16:9 para presentaciones
    fig, axs = plt.subplots(2, 2, figsize=(12, 6.75), constrained_layout=True)
    fig.suptitle('Operaciones entre Eventos y Propiedades de la Probabilidad')

    # --- Subplot 1: Unión (E ∪ F) ---
    ax1 = axs[0, 0]
    ax1.set_title('Unión (E ∪ F)')
    
    # Círculos
    circ_e1 = patches.Circle(C1_CENTER, RADIUS, ec=COLOR_E, fc=COLOR_E, alpha=ALPHA_FILL, lw=2)
    circ_f1 = patches.Circle(C2_CENTER, RADIUS, ec=COLOR_F, fc=COLOR_F, alpha=ALPHA_FILL, lw=2)
    ax1.add_patch(circ_e1)
    ax1.add_patch(circ_f1)
    
    # Etiquetas de los conjuntos
    ax1.text(C1_CENTER[0] - RADIUS, C1_CENTER[1] + RADIUS, 'E', fontsize=14, fontweight='bold', ha='center')
    ax1.text(C2_CENTER[0] + RADIUS, C2_CENTER[1] + RADIUS, 'F', fontsize=14, fontweight='bold', ha='center')
    ax1.text(0, -0.6, 'Incluye todo en E o en F', ha='center')

    # --- Subplot 2: Intersección (E ∩ F) ---
    ax2 = axs[0, 1]
    ax2.set_title('Intersección (E ∩ F)')

    # Círculos base (solo bordes)
    circ_e2_base = patches.Circle(C1_CENTER, RADIUS, ec=COLOR_E, fc='none', lw=2, alpha=ALPHA_EDGE)
    circ_f2_base = patches.Circle(C2_CENTER, RADIUS, ec=COLOR_F, fc='none', lw=2, alpha=ALPHA_EDGE)
    ax2.add_patch(circ_e2_base)
    ax2.add_patch(circ_f2_base)

    # Área de intersección
    # (Se crea un área compleja usando la intersección de dos círculos)
    path_e = patches.Circle(C1_CENTER, RADIUS).get_path()
    path_f = patches.Circle(C2_CENTER, RADIUS).get_path()
    inter_path = patches.Path.make_compound_path(path_e, path_f)
    patch_inter = patches.PathPatch(inter_path, facecolor='purple', alpha=ALPHA_FILL)
    ax2.add_patch(patch_inter)
    
    # Etiquetas
    ax2.text(C1_CENTER[0] - RADIUS, C1_CENTER[1] + RADIUS, 'E', fontsize=14, fontweight='bold', ha='center')
    ax2.text(C2_CENTER[0] + RADIUS, C2_CENTER[1] + RADIUS, 'F', fontsize=14, fontweight='bold', ha='center')
    ax2.text(0, -0.6, 'Incluye solo lo común a E y F', ha='center')

    # --- Subplot 3: Eventos Mutuamente Excluyentes ---
    ax3 = axs[1, 0]
    ax3.set_title('Eventos Mutuamente Excluyentes')
    
    # Círculos separados
    circ_e3 = patches.Circle((-0.5, 0), RADIUS, ec=COLOR_E, fc=COLOR_E, alpha=ALPHA_FILL, lw=2)
    circ_f3 = patches.Circle((0.5, 0), RADIUS, ec=COLOR_F, fc=COLOR_F, alpha=ALPHA_FILL, lw=2)
    ax3.add_patch(circ_e3)
    ax3.add_patch(circ_f3)
    
    # Etiquetas
    ax3.text(-0.5, 0, 'E', fontsize=14, fontweight='bold', ha='center', va='center', color='white')
    ax3.text(0.5, 0, 'F', fontsize=14, fontweight='bold', ha='center', va='center', color='white')
    ax3.text(0, -0.6, 'Intersección vacía: E ∩ F = ∅', ha='center')

    # --- Subplot 4: Axioma de la Unión ---
    ax4 = axs[1, 1]
    ax4.set_title('Axioma de la Unión (para eventos excluyentes)')
    
    # Círculos separados (igual que en ax3)
    circ_e4 = patches.Circle((-0.5, 0), RADIUS, ec=COLOR_E, fc=COLOR_E, alpha=ALPHA_FILL, lw=2)
    circ_f4 = patches.Circle((0.5, 0), RADIUS, ec=COLOR_F, fc=COLOR_F, alpha=ALPHA_FILL, lw=2)
    ax4.add_patch(circ_e4)
    ax4.add_patch(circ_f4)
    
    # Etiquetas y fórmula
    ax4.text(-0.5, 0, 'E₁', fontsize=14, fontweight='bold', ha='center', va='center', color='white')
    ax4.text(0.5, 0, 'E₂', fontsize=14, fontweight='bold', ha='center', va='center', color='white')
    ax4.text(0, -0.65, 'Si E₁ ∩ E₂ = ∅, entonces\nP(E₁ ∪ E₂) = P(E₁) + P(E₂)', ha='center', va='top', fontsize=12)

    # Ajustes finales para todos los subplots
    for ax in axs.flat:
        ax.set_xlim(-1, 1)
        ax.set_ylim(-0.8, 0.8)
        ax.set_aspect('equal', adjustable='box')
        ax.axis('off') # Ocultar ejes para un look limpio

    return fig

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ----------------------------------
def agregar_copyright(fig):
    """Añade una marca de agua de copyright a la figura."""
    fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.',
             ha='right', va='bottom', fontsize=8, color='gray',
             fontstyle='italic')

# --- Ejecución Principal ---
if __name__ == '__main__':
    # Generar el gráfico
    figura_probabilidad = crear_grafico_probabilidad()

    # Añadir el copyright
    agregar_copyright(figura_probabilidad)

    # 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
    # ---------------------------------------------
    # Guardar en formato SVG (vectorial, ideal para PowerPoint y escalado)
    # y PNG de alta resolución como alternativa.
    nombre_archivo_svg = 'grafico_probabilidad_conceptos.svg'
    nombre_archivo_png = 'grafico_probabilidad_conceptos.png'
    
    try:
        figura_probabilidad.savefig(nombre_archivo_svg, format='svg', bbox_inches='tight')
        figura_probabilidad.savefig(nombre_archivo_png, format='png', dpi=300, bbox_inches='tight')
        print(f"Gráfico guardado exitosamente como '{nombre_archivo_svg}' y '{nombre_archivo_png}'.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

    # Opcional: mostrar el gráfico en pantalla
    plt.show()
