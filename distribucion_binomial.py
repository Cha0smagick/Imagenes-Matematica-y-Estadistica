# =============================================================================
# SCRIPT PARA LA VISUALIZACIÓN DE LA DISTRIBUCIÓN BINOMIAL
#
# Objetivo: Generar un gráfico de calidad editorial que ilustre la Función
#           de Masa de Probabilidad (PMF) de la Distribución Binomial para
#           diferentes conjuntos de parámetros (n, p).
#
# Autor:    Alejandro Quintero Ruiz (Generado con asistencia de IA)
# Fecha:    2023-10-27
# =============================================================================

# -----------------------------------------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
import math

# -----------------------------------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# -----------------------------------------------------------------------------
# Se definen tres conjuntos de parámetros (n, p) para ilustrar el comportamiento
# de la distribución binomial.
params = [
    {'n': 20, 'p': 0.5, 'label': 'n=20, p=0.5 (Simétrica)', 'color_idx': 0},
    {'n': 20, 'p': 0.2, 'label': 'n=20, p=0.2 (Sesgada)', 'color_idx': 1},
    {'n': 40, 'p': 0.5, 'label': 'n=40, p=0.5 (Mayor dispersión)', 'color_idx': 2}
]

# Rango de éxitos (k) a evaluar. Se toma el máximo 'n' para el eje x.
max_n = max(p['n'] for p in params)
k_values = np.arange(0, max_n + 1)

# -----------------------------------------------------------------------------
# 3. FUNCIÓN O BLOQUE DE GENERACIÓN DEL GRÁFICO
# -----------------------------------------------------------------------------

# --- Configuración de Estilo Profesional ---
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'Arial' # Fuente limpia y profesional
plt.rcParams['axes.labelsize'] = 14    # Tamaño de etiquetas de ejes
plt.rcParams['xtick.labelsize'] = 12   # Tamaño de ticks en x
plt.rcParams['ytick.labelsize'] = 12   # Tamaño de ticks en y
plt.rcParams['legend.fontsize'] = 12   # Tamaño de la leyenda
plt.rcParams['figure.titlesize'] = 16  # Tamaño del título

# --- Creación de la Figura y Ejes ---
# Aspect ratio 16:9 ideal para presentaciones (ej. PowerPoint)
fig, ax = plt.subplots(figsize=(12, 6.75))

# Paleta de colores amigable con el daltonismo
palette = sns.color_palette("viridis", n_colors=len(params))

# --- Iteración y Ploteo de cada Distribución ---
for param in params:
    n = param['n']
    p = param['p']
    
    # Cálculo de la PMF (Probability Mass Function)
    probabilidades = binom.pmf(k_values, n, p)
    
    # Se plotea como una línea con marcadores para mayor claridad
    ax.plot(k_values, probabilidades, 
            marker='o', linestyle='-', 
            label=param['label'], 
            color=palette[param['color_idx']],
            alpha=0.8, markersize=5)
            
    # --- Anotación de la Media (Valor Esperado) ---
    media = n * p
    ax.axvline(x=media, color=palette[param['color_idx']], linestyle='--', linewidth=1.5, alpha=0.7)
    
    # Se añade texto para indicar la media, ajustando su posición para evitar solapamientos
    ax.text(media + 0.5, 0.01, f'E[X]={media:.1f}', 
            color=palette[param['color_idx']], 
            fontsize=11, 
            fontweight='bold',
            rotation=90)

# --- Ajustes Finales del Gráfico (Títulos, Etiquetas, Leyenda) ---
ax.set_title('Visualización de la Distribución Binomial para Diferentes Parámetros', 
             fontweight='bold', pad=20)
ax.set_xlabel('Número de Éxitos (k)')
ax.set_ylabel('Probabilidad P(X=k)')
ax.legend(title='Parámetros (n, p)', frameon=True, facecolor='white', framealpha=0.8)

# Ajustar límites para una mejor visualización
ax.set_xlim(left=-1, right=max_n + 1)
ax.set_ylim(bottom=0)

# Mejorar la apariencia de los bordes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# -----------------------------------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# -----------------------------------------------------------------------------
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.5, 0.01, copyright_text, 
         ha='center', va='bottom', 
         fontsize=10, color='gray', alpha=0.8)

# Ajustar el layout para que el copyright y los títulos no se solapen
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # rect=[left, bottom, right, top]

# -----------------------------------------------------------------------------
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# -----------------------------------------------------------------------------
# Guardar en formato vectorial (SVG) para máxima calidad y escalabilidad
output_filename_svg = "distribucion_binomial_alta_calidad.svg"
fig.savefig(output_filename_svg, format='svg', bbox_inches='tight')

# Guardar en formato PNG con alta resolución (300 DPI) para compatibilidad
output_filename_png = "distribucion_binomial_alta_calidad.png"
fig.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# --- Mostrar el gráfico (opcional) ---
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

