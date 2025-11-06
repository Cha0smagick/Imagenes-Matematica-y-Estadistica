# -----------------------------------------------------------------------------
# SCRIPT PARA LA VISUALIZACIÓN DE LA DISTRIBUCIÓN NORMAL (GAUSSIANA)
#
# Objetivo: Generar un gráfico de calidad editorial que ilustra la
#           distribución normal y el efecto de sus parámetros (media y
#           desviación estándar).
#
# Autor:    Alejandro Quintero Ruiz (Generado con asistencia de IA)
# Fecha:    2023-10-27
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# -----------------------------------------------------------------------------
# Parámetros para diferentes distribuciones normales a graficar.
# Se incluye la distribución estándar N(0, 1) como referencia principal.
params = [
    {'mu': 0, 'sigma': 1, 'label': 'Estándar: N(0, 1)', 'linestyle': '-', 'color': '#0072B2'},
    {'mu': 0, 'sigma': 2, 'label': 'Mayor dispersión: N(0, 4)', 'linestyle': '--', 'color': '#D55E00'},
    {'mu': 0, 'sigma': 0.5, 'label': 'Menor dispersión: N(0, 0.25)', 'linestyle': ':', 'color': '#009E73'},
    {'mu': -2, 'sigma': 1, 'label': 'Media desplazada: N(-2, 1)', 'linestyle': '-.', 'color': '#CC79A7'}
]

# Rango de valores en el eje x para la visualización.
# Se elige un rango amplio para que todas las curvas se vean completas.
x = np.linspace(-8, 8, 1000)

# 3. GENERACIÓN DEL GRÁFICO
# -----------------------------------------------------------------------------

# --- Configuración de Estilo Profesional ---
# Se utiliza el estilo de Seaborn para una base estética limpia y moderna.
sns.set_theme(style="whitegrid")

# Configuración de la fuente para legibilidad (compatible con la mayoría de sistemas).
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans', 'Bitstream Vera Sans', 'sans-serif']
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'

# Creación de la figura y los ejes con una proporción 16:9 ideal para presentaciones.
fig, ax = plt.subplots(figsize=(12, 6.75))

# --- Iteración y Dibujo de las Curvas ---
# Se grafica la función de densidad de probabilidad (PDF) para cada conjunto de parámetros.
for p in params:
    # Se calcula la PDF usando la librería SciPy para mayor precisión y simplicidad.
    pdf = norm.pdf(x, p['mu'], p['sigma'])
    ax.plot(x, pdf,
            label=p['label'],
            linestyle=p['linestyle'],
            color=p['color'],
            linewidth=2.5) # Grosor de línea para buena visibilidad.

# --- Ajustes Estéticos y Etiquetas ---
# Título principal del gráfico.
ax.set_title('Distribución Normal o Gaussiana (N)', fontsize=18, pad=20)

# Etiquetas de los ejes, usando Unicode para los símbolos matemáticos.
ax.set_xlabel('Valor (x)', fontsize=14)
ax.set_ylabel('Densidad de Probabilidad f(x)', fontsize=14)

# Leyenda para identificar cada curva.
# 'loc' y 'bbox_to_anchor' la posicionan fuera del área de trazado para no obstruir los datos.
ax.legend(title='Parámetros (μ, σ²)', fontsize=11, title_fontsize=12,
          loc='upper left', bbox_to_anchor=(1.02, 1))

# Ajuste de los límites del eje y para dar "aire" al gráfico.
ax.set_ylim(bottom=0)
ax.set_xlim(x.min(), x.max())

# Mejora de la visibilidad de los ticks (marcas en los ejes).
ax.tick_params(axis='both', which='major', labelsize=12)

# Eliminación de los bordes superior y derecho para un look más limpio (estilo "Tufte").
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ajuste del layout para asegurar que todos los elementos (leyenda, títulos) quepan bien.
plt.tight_layout(rect=[0, 0.05, 0.85, 0.95]) # Se deja espacio abajo y a la derecha.

# 4. ADICIÓN DEL COPYRIGHT / MARCA DE AGUA
# -----------------------------------------------------------------------------
# Se añade el texto en la parte inferior central de la figura.
# 'fig.transFigure' asegura que las coordenadas son relativas a la figura completa.
fig.text(0.5, 0.01, '© Alejandro Quintero Ruiz. Generado con Python.',
         ha='center', va='bottom', fontsize=10, color='gray')

# 5. GUARDADO Y EXPORTACIÓN DEL ARCHIVO
# -----------------------------------------------------------------------------
# Se guarda la imagen en formato SVG (vectorial, escalable y de alta calidad).
# El formato PDF también es una excelente alternativa.
# Para PNG, se recomienda un DPI alto, ej: dpi=300.
output_filename_svg = 'distribucion_normal_gaussiana.svg'
output_filename_pdf = 'distribucion_normal_gaussiana.pdf'

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_pdf, format='pdf', bbox_inches='tight')

# Opcional: Guardar en formato PNG de alta resolución.
# plt.savefig('distribucion_normal_gaussiana.png', format='png', dpi=300, bbox_inches='tight')

# Opcional: Mostrar el gráfico en una ventana emergente al ejecutar el script.
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_pdf}'.")

