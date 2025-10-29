# ----------------------------------------------------------------------------
# SCRIPT PARA VISUALIZAR EL DESCENSO DEL GRADIENTE EN UNA FUNCIÓN DE PÉRDIDA
# ----------------------------------------------------------------------------
# Este script genera un gráfico 3D de calidad editorial que ilustra el
# concepto de optimización de algoritmos de IA mediante el descenso del
# gradiente.
#
# Autor: Gemini Code Assist (para Alejandro Quintero Ruiz)
# Fecha: 2023-10-27
# ----------------------------------------------------------------------------

# 1. IMPORTACIÓN DE LIBRERÍAS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm # Colormaps

# ----------------------------------------------------------------------------
# 2. DEFINICIÓN DE DATOS Y PARÁMETROS MATEMÁTICOS
# ----------------------------------------------------------------------------

# Definimos una función de pérdida convexa de dos variables (parámetros w1 y w2).
# Esta es una función paraboloide simple que simula una función de coste.
def funcion_de_perdida(w1, w2):
    """Calcula el valor de la función de pérdida para los parámetros w1 y w2."""
    return w1**2 + w2**2 + 2 * np.sin(1.5 * w1) + 2 * np.sin(1.5 * w2)

# Definimos el gradiente de la función de pérdida.
# El gradiente es un vector de derivadas parciales [df/dw1, df/dw2].
def gradiente(w1, w2):
    """Calcula el gradiente (derivadas parciales) de la función de pérdida."""
    grad_w1 = 2 * w1 + 3 * np.cos(1.5 * w1)
    grad_w2 = 2 * w2 + 3 * np.cos(1.5 * w2)
    return np.array([grad_w1, grad_w2])

# Parámetros para el algoritmo de Descenso del Gradiente
tasa_aprendizaje = 0.1
n_iteraciones = 25
punto_inicial = np.array([-3.8, 3.5]) # Punto de partida para la optimización

# Calculamos la trayectoria del descenso del gradiente
trayectoria = [punto_inicial]
punto_actual = punto_inicial.copy()

for _ in range(n_iteraciones):
    grad = gradiente(punto_actual[0], punto_actual[1])
    punto_actual = punto_actual - tasa_aprendizaje * grad
    trayectoria.append(punto_actual)

trayectoria = np.array(trayectoria)

# ----------------------------------------------------------------------------
# 3. FUNCIÓN DE GENERACIÓN DEL GRÁFICO
# ----------------------------------------------------------------------------

# --- Configuración de Estilo Profesional ---
# Usamos un estilo predefinido y lo personalizamos para mayor claridad.
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': 'Arial', # Fuente clara y profesional
    'axes.labelcolor': '#333333',
    'xtick.color': '#333333',
    'ytick.color': '#333333',
    'axes.edgecolor': '#DDDDDD',
    'axes.titlepad': 20,
    'figure.dpi': 150 # Buena resolución para la visualización en pantalla
})

# --- Creación de la Figura y Ejes 3D ---
# Proporción 16:9 ideal para PowerPoint
fig = plt.figure(figsize=(12.8, 7.2))
ax = fig.add_subplot(111, projection='3d')

# --- Preparación de la Malla para la Superficie 3D ---
w1_vals = np.linspace(-4, 4, 100)
w2_vals = np.linspace(-4, 4, 100)
W1, W2 = np.meshgrid(w1_vals, w2_vals)
Z = funcion_de_perdida(W1, W2)

# --- Dibujo de la Superficie (Función de Pérdida) ---
# Usamos un colormap amigable con el daltonismo (viridis) y transparencia.
surf = ax.plot_surface(W1, W2, Z, cmap=cm.viridis, alpha=0.6, antialiased=True)

# --- Dibujo de la Trayectoria del Descenso del Gradiente ---
# Extraemos los puntos de la trayectoria para graficarlos.
trayectoria_w1 = trayectoria[:, 0]
trayectoria_w2 = trayectoria[:, 1]
trayectoria_z = funcion_de_perdida(trayectoria_w1, trayectoria_w2)

# Dibujamos la línea que une los pasos
ax.plot(trayectoria_w1, trayectoria_w2, trayectoria_z,
        color='#E63946', # Rojo contrastante
        marker='o',      # Círculos para marcar cada paso
        markersize=5,
        linewidth=2,
        label='Trayectoria del Descenso del Gradiente')

# Marcamos el punto inicial y final para mayor claridad
ax.scatter(trayectoria_w1[0], trayectoria_w2[0], trayectoria_z[0],
           color='#003F5C', s=100, ec='w', lw=1.5, zorder=10, label='Punto Inicial')
ax.scatter(trayectoria_w1[-1], trayectoria_w2[-1], trayectoria_z[-1],
           color='#FFA600', s=150, ec='w', lw=1.5, marker='*', zorder=10, label='Mínimo Encontrado')


# --- Ajustes Estéticos y Etiquetas ---
ax.set_title('Optimización de una Función de Pérdida mediante Descenso del Gradiente',
             fontsize=18, fontweight='bold', color='#222222')
ax.set_xlabel('Parámetro 1 (w1)', fontsize=12, labelpad=10)
ax.set_ylabel('Parámetro 2 (w2)', fontsize=12, labelpad=10)
ax.set_zlabel('Valor de la Función de Pérdida (Error)', fontsize=12, labelpad=10)

# Ajustamos la perspectiva para una mejor visualización
ax.view_init(elev=30, azim=-50)

# Añadimos una leyenda clara y bien ubicada
ax.legend(loc='upper left', fontsize=10, frameon=True, facecolor='white', framealpha=0.8)

# Ajustamos los límites del eje Z para enfocar la parte relevante
ax.set_zlim(0, 40)

# Eliminamos el relleno gris de los paneles para un look más limpio
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# ----------------------------------------------------------------------------
# 4. BLOQUE DE ADICIÓN DEL COPYRIGHT
# ----------------------------------------------------------------------------
copyright_text = "© Alejandro Quintero Ruiz. Generado con Python."
fig.text(0.98, 0.02, copyright_text,
         ha='right', va='bottom',
         fontsize=9, color='gray',
         style='italic')

# ----------------------------------------------------------------------------
# 5. BLOQUE DE GUARDADO/EXPORTACIÓN DEL ARCHIVO
# ----------------------------------------------------------------------------
# Ajustamos el layout para que no se corten las etiquetas o el título
fig.tight_layout(rect=[0, 0.03, 1, 0.97])

# Guardamos en formato SVG (vectorial, ideal para escalar) y PNG (alta resolución)
output_filename_svg = "descenso_del_gradiente.svg"
output_filename_png = "descenso_del_gradiente.png"

plt.savefig(output_filename_svg, format='svg', bbox_inches='tight')
plt.savefig(output_filename_png, format='png', dpi=300, bbox_inches='tight')

# Mostramos el gráfico (opcional)
plt.show()

print(f"Gráfico guardado exitosamente como '{output_filename_svg}' y '{output_filename_png}'.")

