# 1. Importación de Librerías
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# --- Configuración Inicial para Estilo Profesional ---
# Usar un estilo base que sea limpio y profesional.
plt.style.use('seaborn-v0_8-whitegrid')
# Configuración de la fuente para legibilidad (buscando una fuente sans-serif común)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica'] # Fallback fonts
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['figure.titlesize'] = 18


# 2. Definición de Datos/Parámetros Matemáticos
# Definimos una matriz A de 2x2.
# Esta matriz ha sido elegida porque tiene autovalores y autovectores "limpios".
# Sus autovalores son m1=3 y m2=1.
# Sus autovectores correspondientes son [1, 1] y [-1, 1].
A = np.array([[2, 1],
              [1, 2]])

# Definimos un autovector 'x' de la matriz A.
# Corresponde al autovalor m=3.
x = np.array([1, 1])

# Definimos un vector 'y' que NO es un autovector de A.
y = np.array([1, 0])

# Aplicamos la transformación lineal de la matriz A a ambos vectores.
Ax = A @ x  # Resultado de A * x
Ay = A @ y  # Resultado de A * y

# El autovalor asociado a x es 3.
m = 3


# 3. Función o Bloque de Generación del Gráfico
def generar_grafico_autovectores():
    """
    Genera y configura el gráfico que visualiza el concepto de autovectores.
    """
    # Crear la figura y los ejes con una proporción de 16:9 para PowerPoint.
    fig, ax = plt.subplots(figsize=(12, 6.75))

    # --- Paleta de Colores Armónica y Apta para Daltonismo ---
    color_autovector = '#1f77b4'  # Azul
    color_transformado = '#ff7f0e' # Naranja
    color_no_autovector = '#2ca02c' # Verde
    color_ayuda = 'gray'

    # --- Dibujar Vectores ---
    # Origen para todos los vectores
    origen = [0, 0]

    # Vector original 'x' (autovector)
    ax.quiver(*origen, *x, angles='xy', scale_units='xy', scale=1, color=color_autovector, width=0.01, label=r'Autovector $\vec{x}$')
    
    # Vector transformado 'Ax'
    ax.quiver(*origen, *Ax, angles='xy', scale_units='xy', scale=1, color=color_transformado, width=0.015, label=r'Transformado $A\vec{x} = m\vec{x}$')

    # Vector 'y' (no autovector)
    ax.quiver(*origen, *y, angles='xy', scale_units='xy', scale=1, color=color_no_autovector, width=0.01, label=r'Vector $\vec{y}$ (no autovector)')
    
    # Vector transformado 'Ay'
    ax.quiver(*origen, *Ay, angles='xy', scale_units='xy', scale=1, color=color_no_autovector, alpha=0.5, width=0.01, label=r'Transformado $A\vec{y}$')

    # --- Líneas de Ayuda Visual ---
    # Línea punteada para mostrar la colinealidad de x y Ax
    ax.plot([0, Ax[0]], [0, Ax[1]], color=color_ayuda, linestyle='--', zorder=0)

    # --- Anotaciones y Etiquetas ---
    # Anotar los vectores para mayor claridad
    ax.text(x[0] * 0.5, x[1] * 1.2, r'$\vec{x}$', color=color_autovector, size=16, ha='center')
    ax.text(Ax[0] * 0.9, Ax[1] * 0.9, r'$A\vec{x}$', color=color_transformado, size=16, ha='center')
    ax.text(y[0] * 1.1, y[1] * 1.1, r'$\vec{y}$', color=color_no_autovector, size=16, ha='center')
    ax.text(Ay[0] * 1.05, Ay[1] * 0.8, r'$A\vec{y}$', color=color_no_autovector, alpha=0.7, size=16, ha='center')
    
    # Anotación explicativa principal
    ax.text(0.5, 2.5, f'El vector transformado $A\\vec{{x}}$ es colineal con $\\vec{{x}}$\n$A\\vec{{x}} = {m}\\vec{{x}}$',
            size=13, ha='left', va='center', bbox=dict(boxstyle="round,pad=0.5", fc='aliceblue', ec='lightsteelblue', lw=1))

    # --- Ajustes Estéticos del Gráfico ---
    # Título y subtítulo
    fig.suptitle('Visualización de Autovectores y Autovalores', weight='bold')
    ax.set_title('El autovector mantiene su dirección tras una transformación lineal', style='italic', fontsize=14)

    # Límites y aspecto
    lim_max = max(np.max(np.abs(Ax)), np.max(np.abs(Ay))) + 1
    ax.set_xlim(-lim_max, lim_max)
    ax.set_ylim(-1, lim_max)
    ax.set_aspect('equal', adjustable='box') # Ejes a la misma escala para una correcta visualización de ángulos

    # Etiquetas de los ejes
    ax.set_xlabel('Componente X')
    ax.set_ylabel('Componente Y')

    # Leyenda
    ax.legend(loc='upper left', frameon=True, shadow=True)

    # Ocultar el borde superior y derecho para un look más moderno
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    return fig, ax

# Generar el gráfico
fig, ax = generar_grafico_autovectores()


# 4. Bloque de Adición del Copyright
# Añadir la marca de agua/copyright de forma discreta
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.98, 0.02, copyright_text, ha='right', va='bottom', fontsize=10, color='gray', style='italic')


# 5. Bloque de Guardado/Exportación del Archivo
# Guardar la figura en formato vectorial SVG (escalable y de alta calidad)
# y en PNG con alta resolución (300 DPI).
output_filename_svg = "visualizacion_autovector.svg"
output_filename_pdf = "visualizacion_autovector.pdf"
output_filename_png = "visualizacion_autovector.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight', pad_inches=0.1)
plt.savefig(output_filename_pdf, format='pdf', bbox_inches='tight', pad_inches=0.1)
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight', pad_inches=0.1)

# Mostrar el gráfico (opcional, útil si se ejecuta interactivamente)
plt.show()

print(f"Gráfico guardado exitosamente en los siguientes formatos:")
print(f"- {output_filename_svg} (Vectorial, recomendado para PowerPoint)")
print(f"- {output_filename_pdf} (Vectorial, recomendado para publicaciones)")
print(f"- {output_filename_png} (Alta resolución, 300 DPI)")
