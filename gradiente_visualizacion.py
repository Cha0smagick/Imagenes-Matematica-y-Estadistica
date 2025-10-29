# -----------------------------------------------------------------------------
# SCRIPT PARA LA VISUALIZACIÓN DEL GRADIENTE DE UNA FUNCIÓN ESCALAR
# Autor: Alejandro Quintero Ruiz (Generado con asistencia de IA)
# Objetivo: Crear un gráfico de calidad editorial para ilustrar el concepto
#           del gradiente como la dirección de máximo cambio.
# -----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
#    Se define la función escalar y se calcula su gradiente analíticamente.

# Definimos la función escalar f(x, y)
def f(x, y):
    """Función escalar de dos variables para la visualización."""
    return np.sin(x) * np.cos(y)

# Calculamos las derivadas parciales para obtener el gradiente ∇f = [∂f/∂x, ∂f/∂y]
# ∂f/∂x = cos(x) * cos(y)
# ∂f/∂y = -sin(x) * sin(y)
def grad_f(x, y):
    """Calcula el vector gradiente de la función f(x, y)."""
    df_dx = np.cos(x) * np.cos(y)
    df_dy = -np.sin(x) * np.sin(y)
    return df_dx, df_dy

# Creamos una malla de puntos (x, y) para evaluar la función y el gradiente.
x = np.linspace(-np.pi, np.pi, 40)
y = np.linspace(-np.pi, np.pi, 40)
X, Y = np.meshgrid(x, y)

# Calculamos el valor de la función Z = f(X, Y) en cada punto de la malla.
Z = f(X, Y)

# Seleccionamos un subconjunto de puntos para dibujar los vectores del gradiente
# y evitar saturar el gráfico.
skip = 4  # Tomaremos 1 de cada 'skip' puntos.
X_grad = X[::skip, ::skip]
Y_grad = Y[::skip, ::skip]

# Calculamos los componentes (U, V) del gradiente en los puntos seleccionados.
U, V = grad_f(X_grad, Y_grad)

# -----------------------------------------------------------------------------
# 3. FUNCIÓN O BLOQUE DE GENERACIÓN DEL GRÁFICO

# Configuramos el estilo general del gráfico para una apariencia profesional.
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'], # Fuentes claras y comunes
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'figure.titlesize': 18,
    'legend.fontsize': 12,
})

# Creamos la figura y los ejes, con una relación de aspecto 16:9 para PowerPoint.
fig, ax = plt.subplots(figsize=(16, 9))

# a) Dibujamos el mapa de contornos (curvas de nivel) de la función f(x, y).
#    'viridis' es una paleta de colores amigable con el daltonismo.
contour = ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.85)
contour_lines = ax.contour(X, Y, Z, levels=20, colors='white', linewidths=0.5, alpha=0.7)

# b) Añadimos una barra de color para indicar los valores de la función.
cbar = fig.colorbar(contour, ax=ax)
cbar.set_label('Valor de la función f(x, y)', rotation=270, labelpad=20)

# c) Dibujamos los vectores del gradiente usando 'quiver'.
#    Los vectores se normalizan para que todos tengan la misma longitud visual
#    y solo indiquen la dirección, lo cual es el objetivo principal.
norm = np.sqrt(U**2 + V**2)
# Evitamos la división por cero en puntos donde el gradiente es nulo.
U_norm = np.divide(U, norm, out=np.zeros_like(U), where=norm!=0)
V_norm = np.divide(V, norm, out=np.zeros_like(V), where=norm!=0)

ax.quiver(X_grad, Y_grad, U_norm, V_norm, color='red', scale=30, headwidth=4, headlength=5, width=0.003)

# d) Configuramos etiquetas, título y límites del gráfico.
ax.set_xlabel('Variable x')
ax.set_ylabel('Variable y')
ax.set_title('Visualización del Gradiente (∇f) como Dirección de Máximo Cambio', pad=20)
ax.set_aspect('equal', adjustable='box') # Asegura que los ejes tengan la misma escala.

# -----------------------------------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT

# Añadimos la marca de agua de forma discreta en la parte inferior derecha.
fig.text(0.95, 0.03, '© Alejandro Quintero Ruiz. Generado con Python.',
         fontsize=10, color='gray',
         ha='right', va='bottom', alpha=0.7)

# -----------------------------------------------------------------------------
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO

# Ajustamos el layout para que todos los elementos encajen perfectamente.
fig.tight_layout(rect=[0, 0.05, 1, 0.95]) # Dejamos espacio para el copyright y título

# Guardamos el gráfico en formato SVG (vectorial, ideal para escalar) y PNG (alta resolución).
output_filename_svg = "gradiente_visualizacion.svg"
output_filename_png = "gradiente_visualizacion.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Mostramos el gráfico en pantalla (opcional).
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

