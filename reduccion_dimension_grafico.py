# -----------------------------------------------------------------------------
# SCRIPT DE VISUALIZACIÓN: CONCEPTO DE REDUCCIÓN DE LA DIMENSIÓN
# Autor: Gemini Code Assist, para Alejandro Quintero Ruiz
# Fecha: 2023-10-27
# Objetivo: Generar un gráfico vectorial de calidad editorial que ilustra
#           el concepto de reducción de la dimensión para una presentación.
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------------------------------------------------------

# 2. DEFINICIÓN DE DATOS/PARÁMETROS MATEMÁTICOS
# Generamos datos sintéticos que existen en 3D pero tienen una estructura
# intrínseca de menor dimensión (una curva tipo 'S').
# Esto simula datos complejos donde la información relevante puede ser capturada
# con menos características.
n_points = 25
t = np.linspace(0, 4 * np.pi, n_points)
x = np.cos(t)
y = np.sin(t)
z = t / (2 * np.pi)

# Proyectamos los datos 3D a un plano 2D. En un caso real, esto se haría
# con un algoritmo como PCA. Aquí, simplemente descartamos una dimensión (Y)
# para ilustrar el concepto de proyección.
x_2d = x
y_2d = z

# -----------------------------------------------------------------------------

# 3. FUNCIÓN O BLOQUE DE GENERACIÓN DEL GRÁFICO

# --- Configuración del Estilo del Gráfico ---
# Usamos un estilo limpio y profesional. La fuente 'sans-serif' es moderna y legible.
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'axes.labelcolor': '#333333',
    'xtick.color': '#333333',
    'ytick.color': '#333333',
    'axes.titlepad': 20,
    'figure.dpi': 300 # Alta resolución para exportación a PNG si se requiere
})

# --- Creación de la Figura y los Ejes (Subplots) ---
# Creamos una figura con una proporción 16:9, ideal para PowerPoint.
# Dividimos la figura en dos subplots para el antes y el después.
fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2)

# --- Paleta de Colores Armónica y Apta para Daltonismo (Viridis) ---
# El color de los puntos varía a lo largo de la curva para mostrar la estructura.
colors = plt.cm.viridis(np.linspace(0, 1, n_points))

# --- Gráfico 1: Espacio de Alta Dimensión (3D) ---
ax1.scatter(x, y, z, c=colors, s=60, depthshade=True, edgecolors='k', linewidth=0.5)
ax1.set_title('1. Espacio de Alta Dimensión\n(Datos Crudos)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Característica 1', fontsize=12)
ax1.set_ylabel('Característica 2', fontsize=12)
ax1.set_zlabel('Característica 3', fontsize=12)
ax1.view_init(elev=20., azim=-65) # Ajustamos el ángulo de vista para mejor perspectiva

# --- Gráfico 2: Espacio de Baja Dimensión (2D) ---
ax2.scatter(x_2d, y_2d, c=colors, s=60, edgecolors='k', linewidth=0.5)
ax2.set_title('2. Espacio de Baja Dimensión\n(Información Útil)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Componente Principal 1', fontsize=12)
ax2.set_ylabel('Componente Principal 2', fontsize=12)
ax2.set_aspect('equal', adjustable='box') # Mantenemos la proporción de los ejes

# --- Anotaciones y Conexiones ---
# Añadimos una flecha grande para representar el proceso de transformación.
fig.text(0.5, 0.5, '', ha='center', va='center') # Punto de anclaje central
arrow_props = dict(
    arrowstyle="<|-|>",
    mutation_scale=30,
    color='gray',
    lw=2,
    shrinkA=10, # Reduce el inicio de la flecha
    shrinkB=10  # Reduce el final de la flecha
)
# La anotación conecta los dos subplots
fig.add_artist(plt.annotate(
    '',
    xy=(0.55, 0.5), xycoords='figure fraction',
    xytext=(0.45, 0.5), textcoords='figure fraction',
    arrowprops=arrow_props
))
fig.text(0.5, 0.55, 'Reducción de la Dimensión\n(Proceso de Transformación)',
         ha='center', va='center', fontsize=14, color='gray', style='italic')

# --- Título General y Ajuste de Diseño ---
fig.suptitle(
    'El Problema de las Características: De Datos Crudos a Información Útil',
    fontsize=22,
    fontweight='bold',
    y=0.95
)
plt.tight_layout(rect=[0, 0.05, 1, 0.9]) # Ajusta el layout para que no se solapen los títulos

# -----------------------------------------------------------------------------

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# Añadimos la marca de agua de forma discreta en la parte inferior central.
fig.text(
    0.5, 0.01,
    '© Alejandro Quintero Ruiz. Generado con Python.',
    ha='center',
    va='bottom',
    fontsize=10,
    color='gray',
    alpha=0.8
)

# -----------------------------------------------------------------------------

# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# Guardamos la imagen en formato SVG (vectorial) y PNG (alta resolución).
# SVG es ideal para escalar sin pérdida de calidad en PowerPoint.
# PNG es una alternativa de alta calidad.
output_filename_svg = "reduccion_dimension_grafico.svg"
output_filename_png = "reduccion_dimension_grafico.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Opcional: Mostrar el gráfico en pantalla al ejecutar el script
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

# -----------------------------------------------------------------------------
