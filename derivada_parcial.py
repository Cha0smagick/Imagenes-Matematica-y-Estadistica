# ----------------------------------------------------------------------------
# SCRIPT PARA VISUALIZACIÓN DE DERIVADA PARCIAL
#
# Objetivo: Generar un gráfico 3D de calidad editorial para ilustrar el
#           concepto de derivada parcial de la función f(x,y) = x^2 + y^2.
# Autor:    Alejandro Quintero Ruiz (Generado con asistencia de IA)
# ----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ----------------------------------------------------------------------------

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# Función a graficar: f(x, y) = x^2 + y^2
def f(x, y):
    return x**2 + y**2

# Rango de los ejes x e y para la superficie
x_range = np.linspace(-5, 5, 100)
y_range = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = f(X, Y)

# Parámetros para el corte y la derivada parcial
y_fijo = 3
x_punto_tangente = 2

# Curva de intersección (parábola g(x) = x^2 + 9)
x_curva = np.linspace(-4, 4, 100)
y_curva = np.full_like(x_curva, y_fijo)
z_curva = f(x_curva, y_curva)

# Punto de tangencia P(x, y, z)
z_punto_tangente = f(x_punto_tangente, y_fijo)

# Derivada parcial ∂f/∂x = 2x. La pendiente en x=2 es 4.
# Ecuación de la línea tangente en el plano x-z: z_tan = 4*(x - 2) + 13
x_tangente = np.linspace(x_punto_tangente - 1, x_punto_tangente + 1, 10)
y_tangente = np.full_like(x_tangente, y_fijo)
pendiente = 2 * x_punto_tangente
z_tangente = pendiente * (x_tangente - x_punto_tangente) + z_punto_tangente

# ----------------------------------------------------------------------------

# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
def generar_grafico():
    """
    Crea y personaliza el gráfico 3D completo.
    """
    # Configuración del estilo y la figura
    # Usamos un estilo limpio y profesional. 'seaborn-v0_8-whitegrid' es una buena base.
    plt.style.use('seaborn-v0_8-whitegrid')
    fig = plt.figure(figsize=(12.8, 7.2)) # Proporción 16:9 para PowerPoint
    ax = fig.add_subplot(111, projection='3d')

    # Paleta de colores (amigable con daltonismo y profesional)
    # Azul para la superficie, Naranja para el corte, Rojo para la tangente
    color_superficie = '#3B75AF' # Azul acero
    color_corte = '#E69F00'      # Naranja
    color_tangente = '#D55E00'   # Rojo anaranjado
    color_plano = '#56B4E9'      # Azul cielo

    # A. Graficar la superficie principal f(x,y)
    ax.plot_surface(X, Y, Z, alpha=0.4, cmap='viridis', rstride=10, cstride=10, edgecolor='none')

    # B. Graficar el plano de corte y=3
    # Creamos un meshgrid para el plano
    plane_x, plane_z = np.meshgrid(np.linspace(-5, 5, 2), np.linspace(0, 50, 2))
    plane_y = np.full_like(plane_x, y_fijo)
    ax.plot_surface(plane_x, plane_y, plane_z, alpha=0.2, color=color_plano, rstride=1, cstride=1)

    # C. Graficar la curva de intersección (parábola)
    ax.plot(x_curva, y_curva, z_curva, color=color_corte, linewidth=3, label=f'Corte en y={y_fijo}: z = x² + {y_fijo**2}')

    # D. Graficar el punto de tangencia
    ax.scatter(x_punto_tangente, y_fijo, z_punto_tangente, color=color_tangente, s=100, depthshade=True, label=f'Punto ({x_punto_tangente}, {y_fijo}, {int(z_punto_tangente)})')

    # E. Graficar la línea tangente (representación de la derivada parcial)
    ax.plot(x_tangente, y_tangente, z_tangente, color=color_tangente, linewidth=3.5, linestyle='--', label=f'Tangente (∂f/∂x en x={x_punto_tangente})')

    # Ajustes estéticos y de legibilidad
    ax.set_title('Visualización de la Derivada Parcial ∂f/∂x', fontsize=18, pad=20, fontname='Arial')
    ax.set_xlabel('Eje X', fontsize=12, fontname='Arial', labelpad=10)
    ax.set_ylabel('Eje Y', fontsize=12, fontname='Arial', labelpad=10)
    ax.set_zlabel('Eje Z = f(x,y)', fontsize=12, fontname='Arial', labelpad=10)

    # Mejorar la legibilidad de los ticks
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.set_tick_params(labelsize=10)

    # Ajustar la vista de la cámara para una mejor perspectiva
    ax.view_init(elev=25, azim=-50)
    ax.dist = 11 # Alejar un poco la cámara para que todo quepa

    # Añadir leyenda
    ax.legend(fontsize=11, loc='upper left', frameon=True, facecolor='white', framealpha=0.8)
    
    return fig, ax

# ----------------------------------------------------------------------------

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
def anadir_copyright(fig):
    """
    Añade una marca de agua/copyright a la figura.
    """
    fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.',
             ha='right', va='bottom', fontsize=9, color='gray',
             fontname='Arial')

# ----------------------------------------------------------------------------

# 5. BLOQUE PRINCIPAL Y DE GUARDADO/EXPORTACIÓN
if __name__ == '__main__':
    # Generar el gráfico
    figura, eje = generar_grafico()

    # Añadir el copyright
    anadir_copyright(figura)

    # Ajustar el layout para evitar que los elementos se corten
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Guardar la imagen en formatos de alta calidad
    # SVG (Vectorial, ideal para escalabilidad y edición)
    nombre_archivo_svg = 'derivada_parcial_concepto.svg'
    figura.savefig(nombre_archivo_svg, format='svg', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado como: {nombre_archivo_svg}")

    # PDF (Vectorial, excelente para documentos y publicaciones)
    nombre_archivo_pdf = 'derivada_parcial_concepto.pdf'
    figura.savefig(nombre_archivo_pdf, format='pdf', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado como: {nombre_archivo_pdf}")

    # PNG (Alta resolución, para compatibilidad)
    nombre_archivo_png = 'derivada_parcial_concepto.png'
    figura.savefig(nombre_archivo_png, format='png', dpi=300, bbox_inches='tight')
    print(f"Gráfico guardado como: {nombre_archivo_png}")

    # Mostrar el gráfico (opcional)
    plt.show()

