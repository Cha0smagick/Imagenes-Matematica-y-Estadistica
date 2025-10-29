# =============================================================================
# SCRIPT PARA LA VISUALIZACIÓN DE UNA FUNCIÓN DE COSTE J(θ)
#
# Objetivo: Generar un gráfico de calidad editorial para ilustrar el
#           concepto de minimización de una función de coste en Machine Learning.
# Autor:    Alejandro Quintero Ruiz (Generado con asistencia de Gemini Code Assist)
# =============================================================================

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# =============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# =============================================================================

# Definimos el rango de valores para el parámetro θ.
# Usamos np.linspace para crear puntos equidistantes.
theta = np.linspace(-4.5, 4.5, 400)

# Definimos la función de coste J(θ). Usamos una parábola simple (J(θ) = θ^2)
# como un ejemplo canónico de una función de coste convexa.
def funcion_coste(theta):
    """Calcula el valor de la función de coste J(θ) = θ^2."""
    return theta**2

# Calculamos los valores de J(θ) para cada valor de θ.
coste = funcion_coste(theta)

# =============================================================================
# 3. GENERACIÓN DEL GRÁFICO
# =============================================================================

# --- Configuración del Estilo y Estética ---

# Usamos un estilo que emula a la revista 'Science' y 'Nature' para un look limpio.
plt.style.use('seaborn-v0_8-talk')

# Configuración de la figura con una proporción 16:9, ideal para PowerPoint.
fig, ax = plt.subplots(figsize=(12, 6.75))

# Paleta de colores profesional y amigable con daltonismo.
color_curva = '#0072B2'      # Azul
color_punto_inicial = '#D55E00' # Naranja rojizo
color_minimo = '#009E73'     # Verde
color_anotacion = '#56B4E9'  # Azul claro
color_texto_secundario = '#333333'

# --- Trazado de la Curva Principal ---
ax.plot(theta, coste, color=color_curva, linewidth=3, label='Función de Coste J(θ)')

# --- Anotaciones y Puntos de Interés ---

# Punto 1: Estado actual del modelo (no optimizado)
theta_inicial = -3.5
coste_inicial = funcion_coste(theta_inicial)
ax.plot(theta_inicial, coste_inicial, 'o', color=color_punto_inicial, markersize=12, zorder=5)
ax.text(theta_inicial, coste_inicial + 2, 'Estado Actual del Modelo',
        horizontalalignment='center', fontsize=14, color=color_punto_inicial, weight='bold')

# Líneas discontinuas para mostrar las coordenadas del punto inicial
ax.plot([theta_inicial, theta_inicial], [0, coste_inicial], color=color_punto_inicial, linestyle='--', linewidth=1.5, alpha=0.7)
ax.plot([-4.5, theta_inicial], [coste_inicial, coste_inicial], color=color_punto_inicial, linestyle='--', linewidth=1.5, alpha=0.7)


# Punto 2: Mínimo global (objetivo del entrenamiento)
theta_minimo = 0
coste_minimo = funcion_coste(theta_minimo)
ax.plot(theta_minimo, coste_minimo, '*', color=color_minimo, markersize=20, zorder=5, markeredgecolor='white')
ax.text(theta_minimo, coste_minimo - 2.5, 'Mínimo Global\n(Objetivo del Entrenamiento)',
        horizontalalignment='center', fontsize=14, color=color_minimo, weight='bold')

# Anotación del proceso de minimización (flecha)
ax.annotate('Proceso de Minimización (Entrenamiento)',
            xy=(theta_minimo + 0.5, funcion_coste(0.5)),
            xytext=(theta_inicial + 1, funcion_coste(theta_inicial-1)),
            arrowprops=dict(facecolor=color_anotacion, shrink=0.05, width=2, headwidth=10, connectionstyle="arc3,rad=-0.2"),
            fontsize=14, color=color_texto_secundario,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.8))

# --- Configuración de Títulos, Etiquetas y Ejes ---

# Título principal claro y conciso.
fig.suptitle('Visualización de una Función de Coste Convexa', fontsize=20, weight='bold')

# Subtítulo explicativo.
ax.set_title('El entrenamiento busca el parámetro θ que minimiza el coste J(θ)', fontsize=16, pad=20)

# Etiquetas de los ejes con caracteres Unicode para θ.
ax.set_xlabel('Parámetro del Modelo (θ)', fontsize=16, labelpad=10)
ax.set_ylabel('Coste / Pérdida J(θ)', fontsize=16, labelpad=10)

# Ajuste de los límites y ticks de los ejes para un encuadre limpio.
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-5, 25)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position(('outward', 10))
ax.spines['bottom'].set_position(('outward', 10))
ax.tick_params(axis='both', which='major', labelsize=12)

# =============================================================================
# 4. ADICIÓN DEL COPYRIGHT
# =============================================================================

# Añadir marca de agua/copyright en la parte inferior central.
# Usamos fig.text para coordenadas relativas a la figura completa.
fig.text(0.5, 0.01, '© Alejandro Quintero Ruiz. Generado con Python.',
         ha='center', va='bottom', fontsize=10, color='gray', alpha=0.8)

# =============================================================================
# 5. GUARDADO Y EXPORTACIÓN DEL ARCHIVO
# =============================================================================

# Ajustar el layout para evitar que los elementos se solapen.
fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # rect deja espacio para suptitle y copyright

# Guardar la figura en formato SVG (vectorial, escalable) y PNG (alta resolución).
# SVG es ideal para publicaciones y PowerPoint, ya que no pierde calidad al escalar.
output_filename_svg = 'funcion_de_coste.svg'
output_filename_png = 'funcion_de_coste.png'

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico en pantalla (opcional).
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

