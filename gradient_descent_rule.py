# -----------------------------------------------------------------------------
# SCRIPT PARA VISUALIZAR LA REGLA DE ACTUALIZACIÓN DEL DESCENSO DEL GRADIENTE
#
# Objetivo: Generar un gráfico de calidad editorial para explicar el concepto
#           matemático del descenso del gradiente.
# Autor:    Alejandro Quintero Ruiz (Generado con asistencia de Gemini Code Assist)
# Fecha:    2023-10-27
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# Función de pérdida cuadrática J(θ) = θ^2 (un ejemplo simple y claro)
def loss_function(theta):
    return theta**2

# Gradiente (derivada) de la función de pérdida: dJ/dθ = 2θ
def gradient(theta):
    return 2 * theta

# Parámetros del algoritmo
learning_rate = 0.3  # Tasa de aprendizaje (η)
theta_initial = -3.5 # Valor inicial del parámetro θ

# Generar datos para la curva de la función de pérdida
theta_range = np.linspace(-4.5, 4.5, 400)
J_values = loss_function(theta_range)

# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
def create_gradient_descent_plot():
    """
    Crea y personaliza el gráfico del descenso del gradiente.
    """
    # --- Configuración inicial del gráfico (Estilo y Proporciones) ---
    # Usamos un estilo limpio y profesional. 'seaborn-v0_8-whitegrid' es una buena base.
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 6.75)) # Proporción 16:9 para PowerPoint

    # --- Dibujo de la función de pérdida ---
    ax.plot(theta_range, J_values, color='#003f5c', linewidth=2.5, label='Función de Pérdida J(θ)')

    # --- Iteración 1 del Descenso del Gradiente ---
    # Punto inicial
    theta_0 = theta_initial
    J_0 = loss_function(theta_0)
    ax.scatter(theta_0, J_0, color='#ffa600', s=100, zorder=5, label='Parámetro inicial (θ₀)')

    # Gradiente en el punto inicial
    grad_0 = gradient(theta_0)

    # Línea tangente para visualizar el gradiente
    tangent_range = np.linspace(theta_0 - 1, theta_0 + 1, 10)
    tangent_line = grad_0 * (tangent_range - theta_0) + J_0
    ax.plot(tangent_range, tangent_line, color='#ff6361', linestyle='--', linewidth=2, label='Gradiente en θ₀ (∇J(θ₀))')

    # Cálculo del nuevo punto
    theta_1 = theta_0 - learning_rate * grad_0
    J_1 = loss_function(theta_1)
    ax.scatter(theta_1, J_1, color='#bc5090', s=100, zorder=5, label='Parámetro actualizado (θ₁)')

    # --- Anotaciones y flechas para explicar el proceso ---
    # Flecha que muestra el paso de actualización
    arrow = patches.FancyArrowPatch(
        (theta_0, J_0 + 2), (theta_1, J_0 + 2),
        arrowstyle='->', mutation_scale=20,
        color='#58508d', linewidth=2
    )
    ax.add_patch(arrow)
    ax.text(
        (theta_0 + theta_1) / 2, J_0 + 2.5,
        'Paso de actualización: -η ⋅ ∇J(θ₀)',
        ha='center', va='bottom', fontsize=12, color='#58508d', weight='bold'
    )

    # Anotación del punto inicial
    ax.text(theta_0, J_0 - 2, 'θ₀', ha='center', va='top', fontsize=14, weight='bold')
    # Anotación del punto actualizado
    ax.text(theta_1, J_1 - 2, 'θ₁', ha='center', va='top', fontsize=14, weight='bold')

    # --- Ajustes Estéticos Finales ---
    # Título y etiquetas con tipografía clara (sans-serif)
    ax.set_title('Visualización de la Regla de Actualización del Descenso del Gradiente', fontsize=18, weight='bold', pad=20)
    ax.set_xlabel('Parámetro (θ)', fontsize=14)
    ax.set_ylabel('Función de Pérdida J(θ)', fontsize=14)

    # Ajuste de límites para una mejor visualización
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-5, 20)

    # Leyenda
    ax.legend(loc='upper right', fontsize=11, frameon=True, fancybox=True, shadow=True)

    # Ajustar el layout para que no se corten las etiquetas
    plt.tight_layout(rect=[0, 0.05, 1, 1]) # Deja espacio en la parte inferior para el copyright

    return fig, ax

# --- Llamada a la función principal ---
fig, ax = create_gradient_descent_plot()

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# Añadir marca de agua/copyright en la parte inferior central
fig.text(
    0.5, 0.02, # Posición (x, y) en coordenadas de la figura
    '© Alejandro Quintero Ruiz. Generado con Python.',
    ha='center', va='bottom', fontsize=10, color='gray', alpha=0.8
)

# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# Guardar en formato SVG (vectorial, ideal para escalabilidad) y PNG de alta resolución
output_filename_svg = "gradient_descent_rule.svg"
output_filename_png = "gradient_descent_rule.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Opcional: Mostrar el gráfico en pantalla
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

