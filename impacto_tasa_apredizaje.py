# d:\0. Universidad Iberoamericana\10. fundamentos estadisticos y matematicos para la IA\Graficas\script-graficas.py

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# --- 1. Importación de Librerías ---
# matplotlib.pyplot para la creación de gráficos.
# numpy para operaciones numéricas, especialmente para generar rangos de datos.
# seaborn para mejorar la estética de los gráficos de matplotlib, haciéndolos más profesionales y atractivos.

# --- 2. Definición de Datos/Parámetros Matemáticos ---

# Función de costo: Una función cuadrática simple (f(x) = x^2)
# Es ideal para ilustrar el descenso de gradiente debido a su único mínimo global.
def cost_function(x):
    """Calcula el valor de la función de costo f(x) = x^2."""
    return x**2

# Derivada de la función de costo: f'(x) = 2x
# Necesaria para calcular el gradiente en cada paso del algoritmo.
def gradient(x):
    """Calcula el gradiente de la función de costo f(x) = x^2."""
    return 2 * x

# Parámetros de simulación para el Descenso de Gradiente
initial_x = 3.0  # Punto de inicio arbitrario para el algoritmo.
iterations = 20  # Número de pasos que el algoritmo tomará.

# Tasas de aprendizaje (η) para demostrar diferentes escenarios
# Cada valor de η ilustra un comportamiento distinto del algoritmo.
learning_rates = {
    "η pequeña (0.05)": 0.05,  # Convergencia lenta.
    "η óptima (0.2)": 0.2,     # Convergencia eficiente.
    "η grande (0.6)": 0.6,     # Oscilación alrededor del mínimo.
    "η muy grande (0.8)": 0.8  # Divergencia (se aleja del mínimo).
}

# --- 3. Función o Bloque de Generación del Gráfico ---

def generate_gradient_descent_plot(initial_x, iterations, learning_rates, cost_func, grad_func):
    """
    Genera un gráfico que ilustra el impacto de diferentes tasas de aprendizaje
    en el algoritmo de Descenso de Gradiente.

    Args:
        initial_x (float): El valor inicial de 'x' para el descenso de gradiente.
        iterations (int): El número de iteraciones para cada simulación.
        learning_rates (dict): Un diccionario con etiquetas y valores de tasas de aprendizaje.
        cost_func (function): La función de costo a minimizar.
        grad_func (function): La función que calcula el gradiente de la función de costo.

    Returns:
        matplotlib.figure.Figure: El objeto figura de matplotlib con el gráfico generado.
    """
    # Configuración estética con Seaborn para un estilo profesional y moderno.
    # 'whitegrid' proporciona un fondo limpio con cuadrícula.
    # 'viridis' es una paleta de colores perceptualmente uniforme y amigable con el daltonismo.
    sns.set_theme(style="whitegrid", palette="viridis")
    
    # Crear la figura y el eje con una proporción 16:9, ideal para presentaciones en PowerPoint.
    fig, ax = plt.subplots(figsize=(16, 9))

    # Rango de x para graficar la función de costo completa.
    x_vals = np.linspace(-4, 4, 400)
    y_vals = cost_func(x_vals)
    ax.plot(x_vals, y_vals, label="Función de Costo f(x) = x²", color='gray', linestyle='--', linewidth=1.5)

    # Marcar el punto mínimo global de la función de costo.
    ax.plot(0, 0, 'o', color='red', markersize=8, label="Mínimo Global")

    # Simular y graficar el descenso de gradiente para cada tasa de aprendizaje definida.
    for label, eta in learning_rates.items():
        x_history = [initial_x]
        y_history = [cost_func(initial_x)]

        current_x = initial_x
        for _ in range(iterations):
            # Fórmula de actualización del descenso de gradiente: x_nuevo = x_actual - η * gradiente(x_actual)
            current_x = current_x - eta * grad_func(current_x)
            x_history.append(current_x)
            y_history.append(cost_func(current_x))
        
        # Graficar la trayectoria del descenso de gradiente.
        # Se usan marcadores 'o' para cada paso y líneas para conectar la trayectoria.
        ax.plot(x_history, y_history, marker='o', linestyle='-', linewidth=2, markersize=6, label=f"{label} (η={eta})")
        
        # Añadir anotaciones con flechas para los primeros pasos.
        # Esto visualiza el "tamaño del paso" que toma el algoritmo en cada iteración.
        if len(x_history) > 1:
            for i in range(min(3, len(x_history) - 1)): # Anotar los primeros 3 pasos para no saturar
                ax.annotate('', xy=(x_history[i+1], y_history[i+1]), xytext=(x_history[i], y_history[i]),
                            arrowprops=dict(facecolor=ax.lines[-1].get_color(), shrink=0.05, width=1.5, headwidth=8, headlength=8),
                            zorder=5) # Asegura que las flechas se dibujen sobre las líneas

    # Título del gráfico: Claro, descriptivo y con tamaño de fuente adecuado para presentaciones.
    ax.set_title("Impacto de la Tasa de Aprendizaje (η) en el Descenso de Gradiente", fontsize=22, fontweight='bold', pad=20)
    
    # Etiquetas de los ejes: Descriptivas y con tamaño de fuente legible.
    ax.set_xlabel("Parámetro (x)", fontsize=16)
    ax.set_ylabel("Función de Costo f(x)", fontsize=16)
    
    # Ajustes de los límites de los ejes para asegurar que todos los datos sean visibles y el gráfico sea estético.
    ax.set_xlim(min(x_vals)-0.5, max(x_vals)+0.5)
    ax.set_ylim(-0.5, max(y_vals)+2)
    
    # Leyenda: Muestra qué trayectoria corresponde a cada tasa de aprendizaje.
    # 'loc='upper left'' para no obstruir las trayectorias.
    # 'frameon=True' y 'shadow=True' para mejorar la visibilidad.
    ax.legend(fontsize=12, loc='upper left', frameon=True, shadow=True)
    
    # Cuadrícula: Mejora la legibilidad de los valores en los ejes.
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Anotaciones descriptivas: Explican el significado de cada escenario de tasa de aprendizaje,
    # haciendo el gráfico más intuitivo y autoexplicativo.
    # Se usan cajas de texto para mayor claridad y contraste.
    ax.text(0.02, 0.95, "η pequeña: Convergencia lenta, requiere muchas iteraciones.", transform=ax.transAxes,
            fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="lightgray", lw=0.5, alpha=0.8))
    ax.text(0.02, 0.88, "η óptima: Convergencia eficiente hacia el mínimo.", transform=ax.transAxes,
            fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="lightgray", lw=0.5, alpha=0.8))
    ax.text(0.02, 0.81, "η grande: Oscilación alrededor del mínimo o divergencia.", transform=ax.transAxes,
            fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="lightgray", lw=0.5, alpha=0.8))

    # --- 4. Bloque de Adición del Copyright ---
    # Texto de copyright visible pero discreto en la parte inferior derecha.
    fig.text(0.99, 0.01, "© Alejandro Quintero Ruiz. Generado con Python.",
             ha='right', va='bottom', fontsize=10, color='gray', alpha=0.7)

    # Ajustar el layout para asegurar que todos los elementos (título, etiquetas, copyright)
    # sean visibles y no se superpongan.
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # [left, bottom, right, top] para el área del plot
    
    return fig

# Generar el gráfico llamando a la función principal
fig = generate_gradient_descent_plot(initial_x, iterations, learning_rates, cost_function, gradient)

# --- 5. Bloque de Guardado/Exportación del Archivo ---
# Guardar la imagen en formato SVG (Scalable Vector Graphics).
# SVG es ideal para gráficos vectoriales de alta fidelidad y escalables,
# perfectos para publicaciones y presentaciones sin pérdida de calidad.
output_filename = "impacto_tasa_aprendizaje.svg"
fig.savefig(output_filename, format="svg", bbox_inches="tight")

print(f"Gráfico de alta calidad guardado como '{output_filename}'")
