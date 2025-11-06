# =============================================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import ConnectionPatch
from scipy.stats import norm
import warnings

# Ignorar advertencias de fuentes para una salida más limpia
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

# =============================================================================
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# =============================================================================
# Parámetros para la distribución original de la variable aleatoria X
mu_x = 10
sigma_x = 2

# Parámetros para la distribución estandarizada de la variable Z (por definición)
mu_z = 0
sigma_z = 1

# Generar los datos para el eje x de ambas distribuciones
# Se usan suficientes puntos para que las curvas se vean suaves
x_values = np.linspace(mu_x - 4 * sigma_x, mu_x + 4 * sigma_x, 1000)
z_values = np.linspace(mu_z - 4 * sigma_z, mu_z + 4 * sigma_z, 1000)

# Calcular las funciones de densidad de probabilidad (PDF) para cada distribución
pdf_x = norm.pdf(x_values, mu_x, sigma_x)
pdf_z = norm.pdf(z_values, mu_z, sigma_z)

# =============================================================================
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# =============================================================================
def crear_grafico_estandarizacion():
    """
    Genera y configura el gráfico que visualiza la estandarización de una
    variable aleatoria normal.
    """
    # --- Configuración General del Estilo ---
    plt.style.use('seaborn-v0_8-whitegrid') # Estilo profesional y limpio
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial'] # Fuentes claras y aceptadas
    plt.rcParams['axes.labelcolor'] = '#333333'
    plt.rcParams['xtick.color'] = '#333333'
    plt.rcParams['ytick.color'] = '#333333'
    plt.rcParams['axes.titlecolor'] = '#333333'
    plt.rcParams['axes.edgecolor'] = '#CCCCCC'
    plt.rcParams['grid.color'] = '#EAEAEA'
    
    # --- Creación de la Figura y Subplots ---
    # Se usa GridSpec para un control más fino sobre la disposición
    # Proporción 16:9 ideal para presentaciones
    fig = plt.figure(figsize=(12.8, 7.2)) 
    gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1], hspace=0.05)
    
    ax1 = fig.add_subplot(gs[0]) # Gráfico superior para X (con su propio eje x)
    ax2 = fig.add_subplot(gs[1]) # Gráfico inferior para Z (con su propio eje x)

    # --- Paleta de Colores Armónica (amigable con daltonismo) ---
    color_x = '#0072B2' # Azul
    color_z = '#D55E00' # Bermellón
    color_anotacion = '#555555'

    # --- Gráfico Superior: Distribución Original (X) ---
    ax1.plot(x_values, pdf_x, color=color_x, lw=2.5, label=f'X ~ N(μ={mu_x}, σ²={sigma_x**2})')
    ax1.fill_between(x_values, pdf_x, color=color_x, alpha=0.15)
    
    # Título y etiquetas
    ax1.set_title('Visualización del Proceso de Estandarización', fontsize=18, pad=20, weight='bold')
    ax1.set_ylabel('Densidad de Probabilidad', fontsize=12)
    ax1.legend(loc='upper right', fontsize=11)
    
    # Ocultar etiquetas del eje x para el gráfico superior para un look más limpio
    ax1.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    
    # --- Gráfico Inferior: Distribución Estandarizada (Z) ---
    ax2.plot(z_values, pdf_z, color=color_z, lw=2.5, label=f'Z ~ N(μ={mu_z}, σ²={sigma_z**2})')
    ax2.fill_between(z_values, pdf_z, color=color_z, alpha=0.15)
    
    # Etiquetas
    ax2.set_xlabel('Valor de la Variable Aleatoria', fontsize=12)
    ax2.set_ylabel('Densidad de Probabilidad', fontsize=12)
    ax2.legend(loc='upper right', fontsize=11)

    # --- Anotaciones y Conexiones Visuales ---
    puntos_x = [mu_x - 2*sigma_x, mu_x - sigma_x, mu_x, mu_x + sigma_x, mu_x + 2*sigma_x]
    etiquetas_x = ['μ - 2σ', 'μ - σ', 'μ', 'μ + σ', 'μ + 2σ']
    puntos_z = [-2, -1, 0, 1, 2]
    
    for i, (px, pz, label_x) in enumerate(zip(puntos_x, puntos_z, etiquetas_x)):
        # Marcar puntos en el gráfico de X
        y_ax1 = norm.pdf(px, mu_x, sigma_x)
        ax1.plot([px, px], [0, y_ax1], color=color_x, linestyle='--', lw=1) # Línea vertical desde el eje x hasta la curva
        ax1.text(px, 0.01, label_x, ha='center', va='bottom', fontsize=11, color=color_anotacion) # Etiqueta ligeramente por encima del eje x de ax1

        # Marcar puntos en el gráfico de Z
        y_ax2 = norm.pdf(pz, mu_z, sigma_z)
        ax2.plot([pz, pz], [0, y_ax2], color=color_z, linestyle='--', lw=1)
        ax2.text(pz, -0.03, str(pz), ha='center', va='top', fontsize=11, color=color_anotacion)
        
        # Añadir flechas de conexión entre los gráficos
        # Se usa 'con' para la conexión y se transforma la coordenada del eje y
        con = ConnectionPatch(xyA=(px, 0), xyB=(pz, 0), # Conectar al eje x de ax2
                                  coordsA=ax1.transData, coordsB=ax2.transData,
                                  axesA=ax1, axesB=ax2,
                                  arrowstyle="->", shrinkA=5, shrinkB=5,
                                  mutation_scale=20, fc="0.4", color='gray', lw=1.2)
        fig.add_artist(con)

    # Fórmula de estandarización como anotación central
    formula = r'$Z = \frac{X - \mu}{\sigma}$'
    fig.text(0.5, 0.5, formula, ha='center', va='center', fontsize=22, 
             bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='gray', lw=1, alpha=0.9))

    # Ajustar límites para que todo encaje bien
    ax1.set_ylim(bottom=0)
    ax2.set_ylim(bottom=0)
    ax1.set_xlim(x_values.min(), x_values.max())
    ax2.set_xlim(z_values.min(), z_values.max())
    
    # Ajustar el layout para evitar solapamientos
    plt.tight_layout(rect=[0, 0.05, 1, 0.95]) # Deja espacio en la parte inferior para el copyright

    return fig, (ax1, ax2)

# =============================================================================
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# =============================================================================
def anadir_copyright(fig):
    """
    Añade una marca de agua/copyright discreta en la parte inferior central
    de la figura.
    """
    fig.text(0.5, 0.01, '© Alejandro Quintero Ruiz. Generado con Python.',
             ha='center', va='bottom', fontsize=10, color='#888888')

# =============================================================================
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# =============================================================================
def guardar_grafico(fig, nombre_archivo_base):
    """
    Guarda la figura en formatos de alta calidad (SVG, PDF, PNG).
    """
    # Guardar en formato SVG (Vectorial, ideal para escalabilidad)
    fig.savefig(f'{nombre_archivo_base}.svg', format='svg', bbox_inches='tight')
    
    # Guardar en formato PDF (Vectorial, ideal para publicaciones)
    fig.savefig(f'{nombre_archivo_base}.pdf', format='pdf', bbox_inches='tight')
    
    # Guardar en formato PNG (Ráster de alta resolución, para compatibilidad)
    fig.savefig(f'{nombre_archivo_base}.png', format='png', dpi=300, bbox_inches='tight')
    
    print(f"Gráfico guardado exitosamente como:\n"
          f"- {nombre_archivo_base}.svg\n"
          f"- {nombre_archivo_base}.pdf\n"
          f"- {nombre_archivo_base}.png")

# --- Ejecución Principal del Script ---
if __name__ == '__main__':
    # Generar el gráfico
    figura, ejes = crear_grafico_estandarizacion()
    
    # Añadir el copyright
    anadir_copyright(figura)
    
    # Mostrar el gráfico (opcional, útil para desarrollo)
    plt.show()
    
    # Guardar el gráfico en múltiples formatos
    guardar_grafico(figura, 'grafico_estandarizacion_alta_calidad')
