# -----------------------------------------------------------------------------
# Script para la Visualización de Autovalores y Autovectores
# Objetivo: Ilustrar el concepto para una presentación científica.
# Autor: Gemini Code Assist, para Alejandro Quintero Ruiz
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Arrow

# -----------------------------------------------------------------------------

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# Matriz de transformación A. Podemos elegir una que rote y escale los datos.
A = np.array([
    [2.5, 0.5],
    [0.5, 1.5]
])

# Calculamos sus autovalores y autovectores
autovalores, autovectores = np.linalg.eig(A)
v1, v2 = autovectores[:, 0], autovectores[:, 1]
lambda1, lambda2 = autovalores

# Generamos un conjunto de vectores en un círculo unitario para visualizar la transformación
theta = np.linspace(0, 2 * np.pi, 100)
vectores_circulo = np.array([np.cos(theta), np.sin(theta)])

# Aplicamos la transformación A a cada vector del círculo
vectores_transformados = A @ vectores_circulo

# -----------------------------------------------------------------------------

# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO

def generar_grafico_autovectores():
    """
    Crea y estiliza una figura que muestra el efecto de una transformación
    matricial, destacando los autovalores y autovectores.
    """
    # --- Configuración Inicial del Estilo ---
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans'] # Fuente clara y profesional
    plt.rcParams['axes.labelcolor'] = '#333333'
    plt.rcParams['xtick.color'] = '#333333'
    plt.rcParams['ytick.color'] = '#333333'

    # Paleta de colores amigable con daltonismo (Azul, Naranja)
    color_v1 = '#0072B2'
    color_v2 = '#D55E00'
    color_vectores = 'gray'

    # --- Creación de la Figura y Subplots (Formato 16:9) ---
    fig, axes = plt.subplots(1, 2, figsize=(16, 9))
    (ax1, ax2) = axes

    # --- Subplot 1: Antes de la Transformación ---
    ax1.plot(vectores_circulo[0, :], vectores_circulo[1, :], color=color_vectores, alpha=0.4)
    ax1.arrow(0, 0, v1[0], v1[1], head_width=0.1, head_length=0.1, fc=color_v1, ec=color_v1, lw=2.5, zorder=10, label=f'Autovector v₁')
    ax1.arrow(0, 0, v2[0], v2[1], head_width=0.1, head_length=0.1, fc=color_v2, ec=color_v2, lw=2.5, zorder=10, label=f'Autovector v₂')

    # Estética del subplot 1
    ax1.set_title('Espacio Original (Antes de la Transformación)', fontsize=16, pad=20, color='#333333')
    ax1.set_xlabel('Eje X', fontsize=12)
    ax1.set_ylabel('Eje Y', fontsize=12)
    ax1.set_aspect('equal', adjustable='box')
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.legend(fontsize=12, loc='upper right')
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

    # --- Subplot 2: Después de la Transformación ---
    ax2.plot(vectores_transformados[0, :], vectores_transformados[1, :], color=color_vectores, alpha=0.4)

    # Autovectores transformados: v' = A @ v = λ * v
    v1_transformado = A @ v1
    v2_transformado = A @ v2

    # Dibujar líneas de dirección originales (discretas)
    ax2.plot([-v1[0]*4, v1[0]*4], [-v1[1]*4, v1[1]*4], color=color_v1, linestyle='--', alpha=0.5, lw=1.5)
    ax2.plot([-v2[0]*4, v2[0]*4], [-v2[1]*4, v2[1]*4], color=color_v2, linestyle='--', alpha=0.5, lw=1.5)

    # Dibujar los autovectores transformados
    ax2.arrow(0, 0, v1_transformado[0], v1_transformado[1], head_width=0.1, head_length=0.1, fc=color_v1, ec=color_v1, lw=2.5, zorder=10)
    ax2.arrow(0, 0, v2_transformado[0], v2_transformado[1], head_width=0.1, head_length=0.1, fc=color_v2, ec=color_v2, lw=2.5, zorder=10)

    # Anotaciones para los autovalores
    ax2.annotate(f'v\'₁ = λ₁v₁\nλ₁ ≈ {lambda1:.2f}',
                 xy=(v1_transformado[0], v1_transformado[1]),
                 xytext=(v1_transformado[0] + 0.4, v1_transformado[1]),
                 fontsize=14, color=color_v1,
                 arrowprops=dict(arrowstyle="->", color=color_v1))

    ax2.annotate(f'v\'₂ = λ₂v₂\nλ₂ ≈ {lambda2:.2f}',
                 xy=(v2_transformado[0], v2_transformado[1]),
                 xytext=(v2_transformado[0] - 1.5, v2_transformado[1] + 0.5),
                 fontsize=14, color=color_v2,
                 arrowprops=dict(arrowstyle="->", color=color_v2))

    # Estética del subplot 2
    ax2.set_title('Espacio Transformado por la Matriz A', fontsize=16, pad=20, color='#333333')
    ax2.set_xlabel('Eje X', fontsize=12)
    ax2.set_ylabel('Eje Y', fontsize=12)
    ax2.set_aspect('equal', adjustable='box')
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)

    # --- Título General y Ajustes Finales ---
    fig.suptitle('Visualización de Autovectores y Autovalores', fontsize=22, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95]) # Ajustar para dar espacio al título y copyright

    return fig, axes

# -----------------------------------------------------------------------------

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT

def agregar_copyright(fig):
    """Añade una marca de agua de copyright a la figura."""
    fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.',
             fontsize=10, color='gray',
             ha='right', va='bottom', alpha=0.7)

# -----------------------------------------------------------------------------

# --- Ejecución Principal ---
if __name__ == '__main__':
    # Generar el gráfico
    figura, ejes = generar_grafico_autovectores()

    # Añadir el copyright
    agregar_copyright(figura)

    # 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
    nombre_archivo_svg = 'visualizacion_autovectores.svg'
    nombre_archivo_png = 'visualizacion_autovectores.png'

    # Guardar en formato vectorial SVG (recomendado para PowerPoint)
    figura.savefig(nombre_archivo_svg, format='svg', bbox_inches='tight')

    # Guardar también en formato PNG de alta resolución (300 DPI) como alternativa
    figura.savefig(nombre_archivo_png, format='png', dpi=300, bbox_inches='tight')

    print(f"Gráfico guardado exitosamente como '{nombre_archivo_svg}' y '{nombre_archivo_png}'.")

    # Opcional: mostrar el gráfico en pantalla
    plt.show()
