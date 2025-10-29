# -----------------------------------------------------------------------------
# SCRIPT PARA VISUALIZACIÓN DEL ALGORITMO DE DESCENSO DEL GRADIENTE
#
# Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
# Objetivo: Crear un gráfico de calidad editorial para ilustrar el
#           funcionamiento del Descenso del Gradiente.
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS

# --- Parámetros del Algoritmo de Descenso del Gradiente ---
learning_rate = 0.15  # Tasa de aprendizaje (alpha)
initial_theta = 3.8   # Valor inicial arbitrario para el parámetro theta
n_iterations = 5      # Número de iteraciones a visualizar

# --- Definición de la Función de Costo y su Gradiente ---
# Usaremos una función cuadrática simple J(theta) = theta^2 como ejemplo.
# Es una función convexa con un mínimo global en theta = 0.
def cost_function(theta):
    """Función de costo J(theta)."""
    return theta**2

def gradient(theta):
    """Gradiente (derivada) de la función de costo."""
    return 2 * theta

# --- Generación de datos para la gráfica ---
# Creamos un rango de valores de theta para graficar la curva de la función.
theta_range = np.linspace(-4.5, 4.5, 400)
cost_values = cost_function(theta_range)

# --- Simulación de las iteraciones del Descenso del Gradiente ---
thetas = [initial_theta]
costs = [cost_function(initial_theta)]

current_theta = initial_theta
for i in range(n_iterations):
    # Calculamos el gradiente en el punto actual
    grad = gradient(current_theta)
    # Actualizamos theta moviéndonos en la dirección opuesta al gradiente
    current_theta = current_theta - learning_rate * grad
    
    thetas.append(current_theta)
    costs.append(cost_function(current_theta))

# 3. FUNCIÓN O BLOQUE DE GENERACIÓN DEL GRÁFICO

# --- Configuración del Estilo del Gráfico (Estética Profesional) ---
# Usamos un estilo limpio y profesional.
plt.style.use('seaborn-v0_8-whitegrid')

# Configuración de la tipografía para legibilidad y profesionalismo.
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
mpl.rcParams['font.size'] = 14
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['legend.fontsize'] = 14

# Creación de la figura y los ejes, con proporción 16:9 para PowerPoint.
fig, ax = plt.subplots(figsize=(12, 6.75)) # 12x6.75 es una buena proporción 16:9

# --- Graficación de la Función de Costo ---
ax.plot(theta_range, cost_values, color='#00529B', linewidth=2.5, label='Función de Costo J(θ) = θ²')

# --- Visualización de las Iteraciones del Descenso del Gradiente ---
# Graficamos los puntos de cada iteración.
ax.scatter(thetas, costs, color='#D95319', s=60, zorder=5, label='Pasos de Iteración')

# Dibujamos flechas para mostrar la dirección y magnitud de cada paso.
for i in range(n_iterations):
    ax.annotate('', 
                xy=(thetas[i+1], costs[i+1]), 
                xytext=(thetas[i], costs[i]),
                arrowprops=dict(arrowstyle='->', color='#D95319', lw=2),
                va='center')

# --- Anotaciones y Etiquetas para Claridad Científica ---
# Anotar el punto de inicio.
ax.annotate('1. Inicio (θ₀)', 
            xy=(thetas[0], costs[0]), 
            xytext=(thetas[0] + 0.3, costs[0] + 2),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color='black'),
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1, alpha=0.8))

# Anotar el mínimo de la función.
ax.annotate('Mínimo Global\n(Objetivo)', 
            xy=(0, 0), 
            xytext=(-2.5, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color='black'),
            fontsize=12,
            ha='center',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1, alpha=0.8))

# --- Ajustes Finales del Gráfico (Títulos, Etiquetas, Límites) ---
ax.set_title('Visualización del Algoritmo de Descenso del Gradiente', pad=20)
ax.set_xlabel('Parámetro (θ)')
ax.set_ylabel('Función de Costo J(θ)')
ax.legend(loc='upper center')

# Ajustar límites para una mejor visualización.
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-1, 18)

# Remover bordes innecesarios para un look más limpio.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT

# Añadir la marca de agua/copyright de forma discreta.
fig.text(0.98, 0.02, '© Alejandro Quintero Ruiz. Generado con Python.', 
         ha='right', va='bottom', fontsize=10, color='gray', style='italic')

# Ajustar el layout para que no se corten las etiquetas ni el copyright.
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Deja espacio para el título y copyright

# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO

# Guardar el gráfico en formato vectorial SVG (escalable y de alta calidad).
# También se guarda en PNG con alta resolución como alternativa.
output_filename_svg = "descenso_del_gradiente.svg"
output_filename_png = "descenso_del_gradiente.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Opcional: Mostrar el gráfico en pantalla.
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

