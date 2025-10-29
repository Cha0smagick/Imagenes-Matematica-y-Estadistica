# ----------------------------------------------------------------------------
# SCRIPT PARA VISUALIZAR EL GRADIENTE EN LA OPTIMIZACIÓN
# Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
# Fecha: 2023-10-27
# ----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS

# Definimos la función de coste J(θ) y su derivada (gradiente en 1D)
# Usamos una parábola para una visualización clara de un mínimo.
# J(θ) = (θ - 2)^2 + 1
def J(theta):
    return (theta - 2)**2 + 1

# La derivada de J(θ) es J'(θ) = 2 * (θ - 2)
def dJ(theta):
    return 2 * (theta - 2)

# Rango de valores para el parámetro θ
theta_vals = np.linspace(-1, 5, 400)
# Calculamos los valores de la función de coste
cost_vals = J(theta_vals)

# Punto específico donde evaluaremos el gradiente
theta_point = 4.0
cost_point = J(theta_point)
gradient_at_point = dJ(theta_point)

# 3. GENERACIÓN DEL GRÁFICO

# --- Configuración de Estilo Profesional ---
# Usamos un estilo que emula a 'fivethirtyeight' pero con personalizaciones
style.use('fivethirtyeight')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans'] # Fuente clara y ampliamente disponible
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['axes.labelcolor'] = '#333333'
plt.rcParams['xtick.color'] = '#333333'
plt.rcParams['ytick.color'] = '#333333'
plt.rcParams['text.color'] = '#333333'
plt.rcParams['figure.dpi'] = 150 # Buena resolución para vistas previas

# --- Creación de la Figura y Ejes (Aspecto 16:9) ---
fig, ax = plt.subplots(figsize=(12, 6.75))

# --- Dibujo de la Función de Coste ---
ax.plot(theta_vals, cost_vals, color='#007ACC', linewidth=2.5, label='Función de Coste J(θ)')

# --- Dibujo del Punto de Evaluación ---
ax.scatter(theta_point, cost_point, color='#D62728', s=100, zorder=5, label='Punto de Evaluación')

# --- Visualización de los Vectores de Gradiente ---
vector_len = 0.8 # Longitud visual de los vectores en el gráfico
# Vector de Gradiente (Máximo Ascenso)
ax.arrow(theta_point, cost_point, vector_len, gradient_at_point * vector_len,
         head_width=0.15, head_length=0.2, fc='#2CA02C', ec='#2CA02C',
         linewidth=1.8, zorder=4)
# Vector de Gradiente Negativo (Máximo Descenso)
ax.arrow(theta_point, cost_point, -vector_len, -gradient_at_point * vector_len,
         head_width=0.15, head_length=0.2, fc='#FF7F0E', ec='#FF7F0E',
         linewidth=1.8, zorder=4)

# --- Anotaciones y Etiquetas ---
# Título y subtítulo para dar contexto
fig.suptitle('El Rol del Gradiente en la Optimización', fontsize=20, fontweight='bold', ha='center')
ax.set_title('La dirección de máximo descenso (-∇J(θ)) guía la minimización de la función de coste.', fontsize=14, pad=20)

# Etiquetas de los ejes
ax.set_xlabel('θ (Parámetros del Modelo)', fontsize=14, fontweight='bold')
ax.set_ylabel('J(θ) (Función de Coste)', fontsize=14, fontweight='bold')

# Anotaciones para los vectores
ax.text(theta_point + vector_len, cost_point + gradient_at_point * vector_len,
        '  ∇J(θ)\nMáximo Crecimiento',
        fontsize=12, color='#2CA02C', verticalalignment='center', fontweight='medium')

ax.text(theta_point - vector_len - 0.1, cost_point - gradient_at_point * vector_len,
        '-∇J(θ)\nMáximo Descenso  ',
        fontsize=12, color='#FF7F0E', verticalalignment='center', horizontalalignment='right', fontweight='medium')

# --- Ajustes Finales de Estilo ---
ax.grid(True, which='major', linestyle='--', linewidth=0.5)
ax.legend(loc='upper left', fontsize=12)
ax.set_ylim(bottom=0) # Asegurar que el eje Y comience en 0
fig.tight_layout(rect=[0, 0.05, 1, 0.95]) # Ajustar layout para dar espacio al título y copyright

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.5, 0.01, copyright_text, ha='center', va='bottom', fontsize=10, color='gray')

# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# Se guardará en formato SVG (vectorial, escalable) y PNG (alta resolución)
output_filename_svg = "gradiente_optimizacion.svg"
output_filename_png = "gradiente_optimizacion.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico (opcional, útil en entornos interactivos)
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

