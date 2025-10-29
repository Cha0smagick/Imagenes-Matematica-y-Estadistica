# d:\0. Universidad Iberoamericana\10. fundamentos estadisticicos y matematicos para la IA\Graficas\script-graficas.py
"""
Script para generar un gráfico de calidad editorial que visualiza el concepto
del Error Cuadrático Medio (MSE) para una presentación en PowerPoint.

El gráfico consta de dos paneles:
1. Izquierda: Un ejemplo de regresión con puntos de datos, una línea de predicción
   y las líneas de error visuales.
2. Derecha: La función de coste parabólica del MSE, que muestra cómo se penalizan
   los errores.
"""

# ==============================================================================
# 1. Importación de Librerías
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ==============================================================================
# 2. Definición de Datos y Parámetros Matemáticos
# ==============================================================================
# Parámetros para un estilo profesional y limpio
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': 'Arial', # Fuente clara y profesional
    'font.size': 14,
    'axes.labelsize': 16,
    'axes.titlesize': 18,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 14,
    'figure.titlesize': 20,
    'axes.titleweight': 'bold',
    'axes.labelweight': 'bold',
    'figure.titleweight': 'bold'
})

# Datos simulados para el panel de regresión
np.random.seed(42) # Para reproducibilidad
x_real = np.linspace(0, 10, 15)
y_real = 2 * x_real + 1 + np.random.normal(0, 2.5, x_real.shape[0])

# Parámetros del modelo de predicción (línea de regresión)
phi_slope = 2.1
phi_intercept = 0.5
y_pred = phi_slope * x_real + phi_intercept

# Calcular los errores
errors = y_pred - y_real

# Datos para la función de coste (parábola)
error_range = np.linspace(-max(abs(errors))*1.1, max(abs(errors))*1.1, 400)
cost = error_range**2

# Paleta de colores armónica y amigable con el daltonismo
color_data = '#0072B2'      # Azul
color_model = '#D55E00'     # Naranja rojizo
color_error = '#009E73'     # Verde
color_highlight = '#CC79A7' # Rosa

# ==============================================================================
# 3. Función de Generación del Gráfico
# ==============================================================================
def generar_grafico_mse():
    """
    Crea y configura la figura con los dos paneles que ilustran el MSE.
    """
    # Crear una figura con una relación de aspecto 16:9 para PowerPoint
    fig = plt.figure(figsize=(16, 9))
    
    # Configurar una rejilla para los dos subplots
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1], wspace=0.3)
    
    # --- Panel Izquierdo: Contexto de Regresión ---
    ax1 = fig.add_subplot(gs[0])
    
    # Dibujar los errores primero para que queden detrás
    ax1.vlines(x_real, y_pred, y_real, color=color_error, linestyle='--', label='Error (Predicción - Real)', zorder=2)
    
    # Puntos de datos reales
    ax1.scatter(x_real, y_real, color=color_data, s=80, label='Datos Reales (yi)', zorder=3, alpha=0.8)
    
    # Línea del modelo de predicción
    ax1.plot(x_real, y_pred, color=color_model, linewidth=3, label='Predicción del Modelo f(xi, φ)', zorder=4)
    
    # Estética del panel izquierdo
    ax1.set_title('A. Contexto: Errores en un Modelo de Regresión')
    ax1.set_xlabel('Variable de Entrada (xi)')
    ax1.set_ylabel('Variable de Salida (y)')
    ax1.legend(loc='upper left')
    ax1.grid(True, which='both', linestyle='-', linewidth=0.5)
    
    # --- Panel Derecho: Función de Coste MSE ---
    ax2 = fig.add_subplot(gs[1])
    
    # Dibujar la parábola del coste
    ax2.plot(error_range, cost, color=color_model, linewidth=3, label='Coste = Error²', zorder=2)
    
    # Mapear los errores del panel izquierdo a la curva de coste
    ax2.scatter(errors, errors**2, color=color_error, s=80, zorder=3, label='Coste de Errores Individuales')
    
    # Estética del panel derecho
    ax2.set_title('B. Función de Coste: Error Cuadrático Medio')
    ax2.set_xlabel('Error (Predicción - Real)')
    ax2.set_ylabel('Coste (Error²)')
    ax2.legend(loc='upper center')
    ax2.grid(True, which='both', linestyle='-', linewidth=0.5)
    
    # Anotación clave: Penalización de errores grandes
    max_error_idx = np.argmax(np.abs(errors))
    error_val = errors[max_error_idx]
    cost_val = error_val**2
    ax2.annotate(
        'Errores grandes son\nfuertemente penalizados',
        xy=(error_val, cost_val),
        xytext=(error_val * 0.5, cost_val + 30),
        arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
        fontsize=12,
        fontweight='bold',
        ha='center',
        bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="k", lw=1, alpha=0.7)
    )
    
    # Título general de la figura
    fig.suptitle('Visualización del Error Cuadrático Medio (MSE)', fontsize=22, y=0.98)
    
    return fig

# Generar la figura
figura_mse = generar_grafico_mse()

# ==============================================================================
# 4. Bloque de Adición del Copyright
# ==============================================================================
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
figura_mse.text(
    0.98, 0.02, copyright_text,
    ha='right', va='bottom', fontsize=10, color='gray', style='italic'
)

# Ajustar el layout para evitar solapamientos y asegurar que todo sea visible
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# ==============================================================================
# 5. Bloque de Guardado/Exportación del Archivo
# ==============================================================================
# Guardar en formato SVG (vectorial, ideal para escalabilidad)
output_filename_svg = "grafico_mse_alta_calidad.svg"
figura_mse.savefig(output_filename_svg, format='svg', bbox_inches='tight', dpi=300)

# Guardar también en formato PNG de alta resolución como alternativa
output_filename_png = "grafico_mse_alta_calidad.png"
figura_mse.savefig(output_filename_png, format='png', bbox_inches='tight', dpi=300)

# Mostrar el gráfico (opcional, útil durante el desarrollo)
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

