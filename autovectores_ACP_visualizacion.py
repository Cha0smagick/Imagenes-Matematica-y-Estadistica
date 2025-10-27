# ----------------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime

# ----------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ----------------------------------------------------
# Configuración para la generación de datos sintéticos
np.random.seed(42)
num_puntos = 300
media = [0, 0]
# Matriz de covarianza para generar datos con correlación
# Esto asegura que los datos no sean esféricos y tengan direcciones de varianza claras
cov_generacion = [[1, 0.8], 
                  [0.8, 1]]

# Generación de los datos
datos = np.random.multivariate_normal(media, cov_generacion, num_puntos)

# Cálculo de la matriz de covarianza S a partir de los datos generados
# ddof=1 para una estimación insesgada de la covarianza de la muestra
S = np.cov(datos, rowvar=False, ddof=1)

# Cálculo de autovalores (λ) y autovectores (w) de la matriz de covarianza S
autovalores, autovectores = np.linalg.eig(S)

# Ordenar autovectores y autovalores de mayor a menor
# Esto es crucial en PCA, ya que nos interesa el componente de mayor varianza
idx_ordenados = np.argsort(autovalores)[::-1]
autovalores = autovalores[idx_ordenados]
autovectores = autovectores[:, idx_ordenados]

# Asignar los componentes principales (autovectores) y sus autovalores
w1, w2 = autovectores[:, 0], autovectores[:, 1]
lambda1, lambda2 = autovalores[0], autovalores[1]

# Aplicar la transformación S al primer autovector w1
# Esto nos dará el vector Sw1 para visualizar la relación Sw = λw
Sw1 = S @ w1

# ----------------------------------------------------
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ----------------------------------------------------
def generar_grafico_pca():
    """
    Genera y estiliza el gráfico que visualiza la relación entre datos,
    matriz de covarianza y sus autovectores/autovalores.
    """
    # --- Configuración Estética ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(16, 9)) # Aspect ratio 16:9 para PowerPoint
    
    # Paleta de colores profesional y amigable con daltonismo
    color_datos = '#a9a9a9'      # Gris oscuro para los datos de fondo
    color_w1 = '#e67e22'         # Naranja para el 1er autovector
    color_w2 = '#27ae60'         # Verde para el 2do autovector
    color_Sw1 = '#c0392b'        # Rojo para el vector transformado
    color_texto = '#34495e'      # Gris azulado oscuro para texto

    # --- Dibujo de Elementos ---
    # Nube de puntos
    ax.scatter(datos[:, 0], datos[:, 1], alpha=0.6, c=color_datos, label='Datos Sintéticos')

    # Dibujar autovectores (w1 y w2) como flechas desde el origen
    # Se escalan por el autovalor para que su longitud represente la varianza
    escala_visual = 2 
    ax.arrow(0, 0, w1[0] * np.sqrt(lambda1) * escala_visual, w1[1] * np.sqrt(lambda1) * escala_visual,
             head_width=0.1, head_length=0.15, fc=color_w1, ec=color_w1, lw=2.5,
             label=r'$w_1$ (1er Autovector)')
    
    ax.arrow(0, 0, w2[0] * np.sqrt(lambda2) * escala_visual, w2[1] * np.sqrt(lambda2) * escala_visual,
             head_width=0.1, head_length=0.15, fc=color_w2, ec=color_w2, lw=2.5,
             label=r'$w_2$ (2do Autovector)')

    # Dibujar el vector transformado Sw1
    ax.arrow(0, 0, Sw1[0], Sw1[1],
             head_width=0.1, head_length=0.15, fc=color_Sw1, ec=color_Sw1, lw=2.5,
             label=r'$S \cdot w_1 = \lambda_1 w_1$ (Vector Transformado)')

    # --- Títulos, Etiquetas y Leyendas ---
    font_props = {'family': 'sans-serif', 'color': color_texto, 'weight': 'normal', 'size': 14}
    
    ax.set_title('Visualización de Autovectores y Autovalores en PCA', 
                 fontsize=20, weight='bold', color=color_texto, pad=20)
    ax.set_xlabel('Variable 1', fontdict=font_props)
    ax.set_ylabel('Variable 2', fontdict=font_props)
    
    # Configurar leyenda
    legend = ax.legend(loc='upper left', frameon=True, framealpha=0.9, facecolor='white',
                       prop={'size': 12})
    for text in legend.get_texts():
        text.set_color(color_texto)

    # --- Anotaciones para Claridad ---
    # Anotar los vectores directamente en el gráfico
    ax.text(w1[0] * np.sqrt(lambda1) * escala_visual * 0.5, 
            w1[1] * np.sqrt(lambda1) * escala_visual * 0.5 + 0.2, 
            r'$w_1$', color=color_w1, fontsize=16, weight='bold')
    
    ax.text(Sw1[0] * 0.7, Sw1[1] * 0.7 - 0.3, 
            r'$S \cdot w_1$', color=color_Sw1, fontsize=16, weight='bold')

    # --- Ajustes Finales ---
    ax.set_aspect('equal', adjustable='box') # Ejes a la misma escala para ver la ortogonalidad
    ax.axhline(0, color='grey', lw=0.5)
    ax.axvline(0, color='grey', lw=0.5)
    
    # Ajustar límites para centrar el gráfico
    lim_max = np.max(np.abs(datos)) * 1.1
    ax.set_xlim(-lim_max, lim_max)
    ax.set_ylim(-lim_max, lim_max)
    
    # Mejorar la legibilidad de los ticks
    plt.xticks(fontsize=12, color=color_texto)
    plt.yticks(fontsize=12, color=color_texto)
    
    return fig, ax

# Generar el gráfico
fig, ax = generar_grafico_pca()

# ----------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ----------------------------------------------------
copyright_texto = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.98, 0.02, copyright_texto, 
         ha='right', va='bottom', 
         fontsize=10, color='grey',
         transform=fig.transFigure)

# ----------------------------------------------------
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# ----------------------------------------------------
# Usar bbox_inches='tight' para asegurar que todo (títulos, etiquetas) se guarde
# dpi=300 es un buen estándar para publicaciones y presentaciones
nombre_archivo_svg = "visualizacion_pca_autovectores.svg"
nombre_archivo_png = "visualizacion_pca_autovectores.png"

plt.savefig(nombre_archivo_svg, format='svg', bbox_inches='tight')
plt.savefig(nombre_archivo_png, format='png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico (opcional)
plt.show()

print(f"Gráfico guardado como '{nombre_archivo_svg}' y '{nombre_archivo_png}'.")
print(f"Primer autovalor (λ1): {lambda1:.4f}")
print(f"El vector Sw1 es {lambda1:.4f} veces el vector w1.")
