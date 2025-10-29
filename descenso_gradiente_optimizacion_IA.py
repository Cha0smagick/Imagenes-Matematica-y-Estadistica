# ----------------------------------------------------------------------------
# 1. IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyArrowPatch

# ----------------------------------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ----------------------------------------------------------------------------
# Función de coste J(θ) = a*θ₀^2 + b*θ₁^2 (un paraboloide elíptico)
# Esta es una función convexa simple, ideal para ilustrar el descenso del gradiente.
def cost_function(theta0, theta1):
    return 0.5 * theta0**2 + 2.5 * theta1**2

# Gradiente de la función de coste: ∇J(θ) = [∂J/∂θ₀, ∂J/∂θ₁]
def gradient(theta0, theta1):
    return np.array([theta0, 5 * theta1])

# Parámetros para el algoritmo de Descenso del Gradiente
learning_rate = 0.3  # Tasa de aprendizaje (α)
n_iterations = 6     # Número de pasos a visualizar
theta_initial = np.array([-3.5, 1.8]) # Punto de inicio

# Generar la trayectoria del descenso del gradiente
theta_path = [theta_initial]
current_theta = theta_initial
for i in range(n_iterations):
    grad = gradient(current_theta[0], current_theta[1])
    current_theta = current_theta - learning_rate * grad
    theta_path.append(current_theta)
theta_path = np.array(theta_path)

# ----------------------------------------------------------------------------
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ----------------------------------------------------------------------------
def create_gradient_descent_plot():
    """
    Genera y estiliza un gráfico de alta calidad que ilustra el concepto
    de Descenso del Gradiente.
    """
    # --- Configuración Estética Inicial ---
    plt.style.use('seaborn-v0_8-whitegrid') # Estilo base limpio y profesional
    fig, ax = plt.subplots(figsize=(12, 6.75)) # Aspect ratio 16:9 para PowerPoint

    # --- Creación de la Malla y las Curvas de Nivel ---
    theta0_vals = np.linspace(-4, 4, 400)
    theta1_vals = np.linspace(-2, 2, 400)
    T0, T1 = np.meshgrid(theta0_vals, theta1_vals)
    Z = cost_function(T0, T1)

    # Paleta de colores amigable con el daltonismo (Viridis)
    contour = ax.contour(T0, T1, Z, levels=np.logspace(0, 2, 15), cmap='viridis_r')
    ax.clabel(contour, inline=True, fontsize=9, fmt='%.1f')
    
    # --- Dibujo de la Trayectoria y Puntos ---
    ax.plot(theta_path[:, 0], theta_path[:, 1], 'o-', 
            color='#c42121', # Rojo oscuro para alta visibilidad
            markersize=8, 
            linewidth=2, 
            label='Ruta de Optimización (Descenso del Gradiente)')
    
    # Marcar punto de inicio y mínimo
    ax.plot(theta_path[0, 0], theta_path[0, 1], 'D', markersize=10, color='#0d3b66', label='Inicio')
    ax.plot(0, 0, '*', markersize=15, color='#f9a602', label='Mínimo Global J(θ)')

    # --- Anotaciones Clave (Gradiente y Dirección de Descenso) ---
    # Seleccionamos un punto intermedio para la anotación
    point_for_annotation = theta_path[1]
    grad_vector = gradient(point_for_annotation[0], point_for_annotation[1])
    
    # Normalizar para visualización
    grad_vector_norm = grad_vector / np.linalg.norm(grad_vector) * 1.2

    # Flecha para el Gradiente (máximo ascenso)
    arrow_grad = FancyArrowPatch(
        (point_for_annotation[0], point_for_annotation[1]),
        (point_for_annotation[0] + grad_vector_norm[0], point_for_annotation[1] + grad_vector_norm[1]),
        arrowstyle='->,head_length=8,head_width=4', color='#348234', mutation_scale=20, lw=1.5
    )
    ax.add_patch(arrow_grad)
    ax.text(point_for_annotation[0] + grad_vector_norm[0] + 0.1, 
            point_for_annotation[1] + grad_vector_norm[1],
            'Gradiente ∇J(θ)\n(Máximo Ascenso)',
            color='#348234', fontsize=11, fontweight='bold', verticalalignment='center')

    # Flecha para el paso de descenso (dirección opuesta)
    step_vector = -learning_rate * grad_vector
    arrow_desc = FancyArrowPatch(
        (point_for_annotation[0], point_for_annotation[1]),
        (point_for_annotation[0] + step_vector[0], point_for_annotation[1] + step_vector[1]),
        arrowstyle='->,head_length=8,head_width=4', color='#c42121', mutation_scale=20, lw=1.5
    )
    ax.add_patch(arrow_desc)
    ax.text(point_for_annotation[0] + step_vector[0] - 0.8, 
            point_for_annotation[1] + step_vector[1] - 0.4,
            'Paso de Descenso\n-α∇J(θ)',
            color='#c42121', fontsize=11, fontweight='bold', horizontalalignment='right')

    # --- Títulos, Etiquetas y Leyenda ---
    # Usar una fuente Sans-Serif profesional como 'Carlito' o 'Calibri' si está disponible
    font_properties = {'family': 'sans-serif', 'sans-serif': ['Carlito', 'Calibri', 'Arial'], 'size': 12}
    plt.rc('font', **font_properties)

    ax.set_title('Visualización del Descenso del Gradiente para Optimización en IA', fontsize=18, fontweight='bold', pad=20)
    ax.set_xlabel('Parámetro del Modelo (θ₀)', fontsize=14)
    ax.set_ylabel('Parámetro del Modelo (θ₁)', fontsize=14)
    
    # Colocar la leyenda de forma elegante
    ax.legend(loc='upper right', fontsize=11, frameon=True, fancybox=True, shadow=True, borderpad=1)
    
    # Ajustar límites para una mejor visualización
    ax.set_xlim(-4, 4)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal', adjustable='box') # Asegura que los gradientes se vean perpendiculares

    return fig, ax

# ----------------------------------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ----------------------------------------------------------------------------
def add_copyright(fig):
    """Añade una marca de agua de copyright a la figura."""
    fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.',
             ha='right', va='bottom', fontsize=9, color='gray',
             fontstyle='italic')

# ----------------------------------------------------------------------------
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    # Generar el gráfico
    main_fig, main_ax = create_gradient_descent_plot()
    
    # Añadir el copyright
    add_copyright(main_fig)
    
    # Ajustar el layout para evitar que los elementos se superpongan
    main_fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # Deja espacio para título y copyright
    
    # Guardar en formatos de alta calidad
    output_filename_svg = "descenso_gradiente_optimizacion_IA.svg"
    output_filename_pdf = "descenso_gradiente_optimizacion_IA.pdf"
    output_filename_png = "descenso_gradiente_optimizacion_IA.png"
    
    main_fig.savefig(output_filename_svg, format='svg', bbox_inches='tight')
    main_fig.savefig(output_filename_pdf, format='pdf', bbox_inches='tight')
    main_fig.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')
    
    print(f"Gráfico guardado exitosamente en los siguientes formatos:")
    print(f"- {output_filename_svg} (Vectorial, recomendado para PowerPoint)")
    print(f"- {output_filename_pdf} (Vectorial)")
    print(f"- {output_filename_png} (Alta resolución, 300 DPI)")
    
    # Opcional: mostrar el gráfico en pantalla
    plt.show()

