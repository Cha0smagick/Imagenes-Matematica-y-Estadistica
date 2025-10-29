import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Importación de Librerías ---
# numpy: Para operaciones numéricas y creación de arreglos de datos.
# matplotlib.pyplot: La librería principal para la creación de gráficos.
# mpl_toolkits.mplot3d.Axes3D: Necesario para la creación de gráficos 3D.

# --- 2. Definición de Datos/Parámetros Matemáticos ---

# Definimos la función multivariable f(x, y) = x^2 + y^2.
# Esta función es un paraboloide, ideal para visualizar el concepto de cambio
# en múltiples dimensiones de manera intuitiva.
def f(x, y):
    """Calcula el valor de la función f(x, y) = x^2 + y^2."""
    return x**2 + y**2

# Definimos el rango para las variables x e y.
# Un rango simétrico alrededor de cero ayuda a visualizar la simetría de la función.
x_range = np.linspace(-2, 2, 100)
y_range = np.linspace(-2, 2, 100)

# Creamos una malla (grid) para generar la superficie 3D.
# np.meshgrid crea matrices de coordenadas a partir de vectores de coordenadas.
X, Y = np.meshgrid(x_range, y_range)
Z = f(X, Y) # Calculamos los valores de Z para cada punto (X, Y) en la malla.

# Punto específico (x0, y0) en el dominio para ilustrar las derivadas parciales.
# Este punto será el centro de nuestras "rebanadas" de la superficie.
x0 = 1.0
y0 = 1.0
z0 = f(x0, y0) # Valor de la función en el punto (x0, y0).

# --- 3. Función o Bloque de Generación del Gráfico ---

def generate_partial_derivative_plot(x_data, y_data, z_data, x_point, y_point, z_point):
    """
    Genera un gráfico 3D de una función f(x,y) y resalta las "rebanadas"
    que ilustran las derivadas parciales en un punto dado (x_point, y_point).

    Args:
        x_data (np.array): Matriz de coordenadas X para la superficie.
        y_data (np.array): Matriz de coordenadas Y para la superficie.
        z_data (np.array): Matriz de valores Z (f(X,Y)) para la superficie.
        x_point (float): Valor de x en el punto de interés.
        y_point (float): Valor de y en el punto de interés.
        z_point (float): Valor de z (f(x_point, y_point)) en el punto de interés.

    Returns:
        matplotlib.figure.Figure: El objeto figura de Matplotlib con el gráfico.
    """
    # Configuración global de Matplotlib para una estética científica y profesional.
    # Se utilizan fuentes sans-serif para mayor legibilidad en pantallas y presentaciones.
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans', 'Liberation Sans'],
        'font.size': 12,
        'axes.labelsize': 14,
        'axes.titlesize': 16,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 12,
        'figure.titlesize': 18,
        'grid.color': 'lightgray',
        'grid.linestyle': '--',
        'grid.linewidth': 0.5,
        'axes.edgecolor': 'gray',
        'axes.linewidth': 0.8
    })

    # Crear la figura y el eje 3D.
    # El tamaño de la figura se ajusta a una proporción 16:9, ideal para PowerPoint.
    # 'constrained_layout=True' ayuda a ajustar automáticamente los elementos para evitar solapamientos.
    fig = plt.figure(figsize=(12, 6.75), constrained_layout=True)
    ax = fig.add_subplot(111, projection='3d')

    # Título principal del gráfico, descriptivo y claro.
    fig.suptitle('Derivadas Parciales: Midiendo el Cambio Local', fontsize=18, weight='bold')

    # Plotear la superficie 3D de la función f(x, y).
    # 'cmap='viridis'' es una paleta de colores perceptualmente uniforme y amigable para daltónicos.
    # 'alpha=0.8' para permitir ver a través de la superficie si hay elementos detrás.
    surface = ax.plot_surface(x_data, y_data, z_data, cmap='viridis', alpha=0.8, edgecolor='none')

    # Resaltar el punto específico (x0, y0, f(x0, y0)) en la superficie.
    # 's=100' para un tamaño visible, 'color='red'' para destacarlo.
    # 'zorder=5' asegura que el punto se dibuje encima de otros elementos.
    ax.scatter([x_point], [y_point], [z_point], color='red', s=100, label=f'Punto de Interés ({x_point}, {y_point})', zorder=5)

    # --- Ilustración de la derivada parcial con respecto a x (manteniendo y constante) ---
    # Creamos una "rebanada" de la superficie donde y = y_point.
    # Esto representa la curva que se obtiene al movernos solo en la dirección de x.
    x_slice = np.linspace(x_data.min(), x_data.max(), 100)
    y_slice_const = np.full_like(x_slice, y_point) # y es constante
    z_slice_x = f(x_slice, y_slice_const)
    ax.plot(x_slice, y_slice_const, z_slice_x, color='blue', linewidth=3, label=f'Curva con y = {y_point} (constante)', zorder=4)

    # --- Ilustración de la derivada parcial con respecto a y (manteniendo x constante) ---
    # Creamos una "rebanada" de la superficie donde x = x_point.
    # Esto representa la curva que se obtiene al movernos solo en la dirección de y.
    y_slice = np.linspace(y_data.min(), y_data.max(), 100)
    x_slice_const = np.full_like(y_slice, x_point) # x es constante
    z_slice_y = f(x_slice_const, y_slice)
    ax.plot(x_slice_const, y_slice, z_slice_y, color='green', linewidth=3, label=f'Curva con x = {x_point} (constante)', zorder=4)

    # Etiquetas de los ejes, con 'labelpad' para una mejor separación visual.
    ax.set_xlabel('Variable x', labelpad=10)
    ax.set_ylabel('Variable y', labelpad=10)
    ax.set_zlabel('Función f(x, y)', labelpad=10)

    # Título específico del subplot 3D.
    ax.set_title(f'Superficie $f(x,y) = x^2 + y^2$ y sus Secciones en ({x_point}, {y_point})', fontsize=14)

    # Leyenda para identificar los elementos del gráfico.
    ax.legend(loc='upper left', bbox_to_anchor=(0.05, 0.95))

    # Ajustes de la vista 3D para una perspectiva óptima.
    # 'elev' (elevación) y 'azim' (azimut) controlan el ángulo de la cámara.
    # 'dist' controla la distancia de la cámara al objeto.
    ax.view_init(elev=25, azim=-120)
    ax.dist = 10

    # Anotaciones explicativas para reforzar el concepto, colocadas en coordenadas 2D
    # relativas al eje ('transform=ax.transAxes').
    ax.text2D(0.02, 0.95, "• La curva azul muestra el cambio de f(x,y) cuando 'y' es constante.",
              transform=ax.transAxes, color='blue', fontsize=10, ha='left', va='top')
    ax.text2D(0.02, 0.90, "• La curva verde muestra el cambio de f(x,y) cuando 'x' es constante.",
              transform=ax.transAxes, color='green', fontsize=10, ha='left', va='top')
    ax.text2D(0.02, 0.85, "• La pendiente de estas curvas en el punto rojo representa las derivadas parciales.",
              transform=ax.transAxes, color='black', fontsize=10, ha='left', va='top')

    # --- 4. Bloque de Adición del Copyright ---
    # Añadir marca de agua/copyright en la parte inferior derecha de la figura completa.
    # 'transform=fig.transFigure' asegura que las coordenadas sean relativas a la figura.
    fig.text(0.99, 0.01, '© Alejandro Quintero Ruiz. Generado con Python.',
             fontsize=9, color='gray', ha='right', va='bottom', alpha=0.7)

    return fig

# Generar el gráfico llamando a la función.
fig = generate_partial_derivative_plot(X, Y, Z, x0, y0, z0)

# --- 5. Bloque de Guardado/Exportación del Archivo ---
# Definimos la ruta completa para guardar el archivo.
# Se prefiere .svg por ser un formato vectorial escalable de alta fidelidad.
output_filename = 'd:/0. Universidad Iberoamericana/10. fundamentos estadisticos y matematicos para la IA/Graficas/derivadas_parciales.svg'
plt.savefig(output_filename, format='svg', dpi=300, bbox_inches='tight')

print(f"Gráfico guardado como '{output_filename}'")

# Para visualizar el gráfico en una ventana emergente (descomentar si es necesario):
# plt.show()
